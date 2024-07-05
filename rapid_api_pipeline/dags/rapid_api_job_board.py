from airflow import DAG
from datetime import datetime
from airflow.operators.empty import EmptyOperator


# create a context manager
with DAG('rapid_api_job_board', start_date=datetime(2024, 7, 5), schedule="0 6 * * *", catchup=False) as dag:

    start_workflow =  EmptyOperator(task_id="start_workflow")