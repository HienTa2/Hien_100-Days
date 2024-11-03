# Churn ETL Pipeline Project

## Overview
This project demonstrates an ETL (Extract, Transform, Load) pipeline for analyzing churn data. The pipeline extracts data from a CSV file, transforms it, and loads it into a new CSV file for further analysis and visualization.

## Project Structure
- **etl_pipeline.bat**: Batch file to run the entire ETL process with error handling.
- **Step 1_extract_data.py/**: Script for extracting data.
- **Step 2_transform_data.py/**: Script for transforming data.
- **Step 3_load_data.py/**: Script for loading data into a CSV file.
- **Step 4_dashboard.py/**: Script for dashboard.
- **Step 5_Automation.py/**: Script for automation.
- **analysis/**: Jupyter notebooks for data analysis and visualization.
- **dataset/**: Directory containing the raw data.
- **transformed_data.csv**: File containing the transformed data.
- **final_output.csv**: File containing the final output data.
- **README.md**: Project documentation.
- **requirements.txt**: List of dependencies.

## How to Install
1. Create a virtual environment and activate it.
2. Upgrade pip:
   ```bash
   python -m pip install --upgrade pip
