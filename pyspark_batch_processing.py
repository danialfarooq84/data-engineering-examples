from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg
import time

# Initialize Spark session
spark = SparkSession.builder \
    .appName("PySpark Batch Processing Example") \
    .getOrCreate()

print("🚀 Starting PySpark Batch Processing...")

# Read input CSV file
input_path = "input_data.csv"
print(f"📥 Reading data from {input_path}...")
df = spark.read.csv(input_path, header=True, inferSchema=True)

# Display the input data
print("🔍 Input Data:")
df.show()

# Perform transformations (example: calculate average value per category)
print("⚙️ Processing data...")
result = df.groupBy("category").agg(avg(col("value")).alias("avg_value"))

# Show result
print("✅ Aggregated Results:")
result.show()

# Save output with timestamp
timestamp = time.strftime("%Y%m%d_%H%M%S")
output_path = f"batch_output_{timestamp}.csv"
result.toPandas().to_csv(output_path, index=False)

print(f"💾 Results saved to {output_path}")

# Stop the Spark session
spark.stop()
print("🏁 Batch Processing Complete!")
