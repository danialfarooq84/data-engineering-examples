@echo off
REM ==========================================
REM PySpark ETL Runner - Windows Batch Script
REM ==========================================

REM --- Navigate to your project folder ---
cd /d C:\Users\dania\Desktop\data-engineering-examples

REM --- Activate the virtual environment ---
call venv\Scripts\activate

REM --- Set PySpark environment variables ---
set PYSPARK_PYTHON=%CD%\venv\Scripts\python.exe
set PYSPARK_DRIVER_PYTHON=%CD%\venv\Scripts\python.exe

echo Running PySpark ETL job...
echo ------------------------------------------

REM --- Run your ETL script ---
python pyspark_etl_example.py

REM --- Check if the job succeeded ---
if exist "%CD%\output_data.csv" (
    echo.
    echo ✅ ETL job completed successfully!
    echo Opening output_data.csv ...
    start "" "%CD%\output_data.csv"
) else (
    echo.
    echo ⚠️  ETL job completed, but output_data.csv was not found.
)

echo ------------------------------------------
pause
