from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.providers.google.cloud.operators.datafusion import CloudDataFusionStartPipelineOperator
import subprocess
import logging

# Function to run the Python script
def fetch_employee_data(**kwargs):
    script_path = kwargs.get('script_path', 'gs://us-central1-compser-dev-8777d142-bucket/dags/scripts/extract.py')
    local_script_path = '/tmp/extract.py'

    try:
        logging.info(f"Copying script from {script_path} to {local_script_path}")
        # Using gsutil to copy the file from GCS to a local path
        subprocess.run(["gsutil", "cp", script_path, local_script_path], check=True)

        logging.info(f"Running the script at {local_script_path}")
        # Running the local Python script
        result = subprocess.run(["python", local_script_path], check=True, capture_output=True, text=True)
        logging.info(f"Script executed successfully: {result.stdout}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Script execution failed: {str(e)}")
        logging.error(f"Error Output: {e.stderr}")
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        raise

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 8, 25),
    'depends_on_past': False,
    'email': ['Hienta@pm.me'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Defining the DAG
dag = DAG(
    'employee_data',
    default_args=default_args,
    description='Runs a Python script and triggers a Cloud Data Fusion pipeline',
    schedule_interval='@daily',
    catchup=False,
)

# Task to copy and run the Python script from GCS
run_script_task = BashOperator(
    task_id='extract_data',
    bash_command=f'gsutil cp gs://us-central1-compser-dev-8777d142-bucket/dags/scripts/extract.py /tmp/extract.py && python /tmp/extract.py',
    dag=dag,
)

# Task to start the Cloud Data Fusion pipeline
start_pipeline = CloudDataFusionStartPipelineOperator(
    location='us-central1',
    pipeline_name='etl-pipeline2',
    instance_name='datafusion-dev',
    task_id='start_pipeline',
    dag=dag,
)

# Define the task dependencies
run_script_task >> start_pipeline
