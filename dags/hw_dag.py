import datetime as dt
import os
import sys

from airflow.models import DAG
from airflow.operators.python import PythonOperator

path = os.path.expanduser('~/airflow_hw')
# Add the project code path to an environment variable so that it is available to the Python process.
os.environ['PROJECT_PATH'] = path
# Add the project code path to $PATH, to import functions
sys.path.insert(0, path)

from modules.pipeline import pipeline
from modules.predict import predict


args = {
    'owner': 'airflow',
    'start_date': dt.datetime(2023, 3, 20),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=1),
    'depends_on_past': False,
}

with DAG(
        dag_id='car_price_prediction',
        schedule_interval=dt.timedelta(hours=1),
        default_args=args,
        catchup=False,
) as dag:

    run_pipeline = PythonOperator(
        task_id='pipeline',
        python_callable=pipeline,
        dag=dag,
    )

    make_prediction = PythonOperator(
        task_id='prediction',
        python_callable=predict,
        dag=dag,
    )

    run_pipeline >> make_prediction
