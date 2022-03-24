from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator

from utils.constants import START_DATE, URL, DATA_ROOT_PATH, default_args
from utils.request_gbg_air import query_and_save_results_to_disc


with DAG(
    dag_id="gbg_air_quality_request_to_disc",
    default_args=default_args,
    start_date=START_DATE,
    schedule_interval="0 3 * * *",
) as dag:

    start = DummyOperator(task_id="start")
    stop = DummyOperator(task_id="stop")

    request_to_disc = PythonOperator(
        task_id="request_to_disc",
        python_callable=query_and_save_results_to_disc,
        op_kwargs={
            "date": "{{ ds }}",
            "url": URL,
            "data_root": DATA_ROOT_PATH,
        },
    )

    start >> request_to_disc >> stop
