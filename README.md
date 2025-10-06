Data Engineering Examples

Hi! I’m Danial Farooq, and this repo is a collection of my data engineering projects and experiments.
I’ve worked with tools like PySpark, Hadoop, and Python to build and test different kinds of data pipelines, from small ETL examples to larger transformations.

🧠 What’s Inside
1. PySpark ETL Example

This project shows how to use PySpark for a simple ETL (Extract, Transform, Load) process.
It reads input data, performs transformations like grouping and aggregation, and saves the results as a clean CSV file.

Files included:

pyspark_etl_example.py – main ETL script

input_data.csv – sample input data

output_data.csv – generated output after processing

run_etl.bat – batch file for quick execution on Windows

⚙️ How to Run It

Make sure you have Python and Java installed, then run these commands:

# 1. Create and activate a virtual environment
py -3.11 -m venv venv
venv\Scripts\activate

# 2. Install dependencies
pip install pyspark pandas

# 3. Run the ETL script
python pyspark_etl_example.py


The processed output will be saved as output_data.csv in the same folder.

💬 Why I Built This

I built this project to put data engineering concepts into practice; focusing on how Spark handles large data transformations efficiently.
These examples help me sharpen my understanding of how distributed processing works in real-world data workflows.

🚀 What’s Next

I plan to extend this repo with:

More PySpark and Spark SQL examples

A small data pipeline project with scheduling and monitoring

Possibly a Dockerized version for easier deployment

📫 Connect with Me

If you’re into data engineering or Spark too, I’d love to connect and share ideas!
