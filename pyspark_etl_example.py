from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("CSV_ETL_Pipeline") \
    .getOrCreate()

# Step 1: Read input CSV file
# Replace "input_data.csv" with your actual file name
df = spark.read.csv("input_data.csv", header=True, inferSchema=True)

# Step 2: Basic transformation
# Example: compute average value per category
result = df.groupBy("category").agg(avg(col("value")).alias("avg_value"))

# Step 3: Show results in console
print("=== Aggregated Results ===")
result.show()

# Step 4: Save to output CSV
result.toPandas().to_csv("output_data.csv", index=False)

# Stop Spark
spark.stop()
