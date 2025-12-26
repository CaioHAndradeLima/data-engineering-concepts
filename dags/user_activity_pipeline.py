from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from project.quality.silver_checks import check_silver_not_empty
from project.quality.gold_checks import check_gold_loaded

from project.etl import extract, transform, load


def extract_task(execution_date: str, **_):
    """
    BRONZE
    - Fetch data from API if needed
    - Persist raw data to data lake
    """
    extract(execution_date)


def transform_task(execution_date: str, **_):
    """
    SILVER
    - Read raw data from data lake
    - Clean / normalize
    - Persist silver data
    """
    transform(execution_date)


def load_task(execution_date: str, **_):
    """
    GOLD
    - Read silver data
    - Load analytics-ready data into Postgres
    """
    load(execution_date)


with DAG(
    dag_id="user_activity_pipeline",
    start_date=datetime(2025, 12, 20),
    schedule_interval="@daily",
    catchup=True,
    default_args={"retries": 2},
    tags=["etl", "learning", "lakehouse"],
) as dag:

    extract_op = PythonOperator(
        task_id="extract_raw_events",
        python_callable=extract_task,
        op_kwargs={"execution_date": "{{ ds }}"},
    )

    transform_op = PythonOperator(
        task_id="transform_to_silver",
        python_callable=transform_task,
        op_kwargs={"execution_date": "{{ ds }}"},
    )

    load_op = PythonOperator(
        task_id="load_to_warehouse",
        python_callable=load_task,
        op_kwargs={"execution_date": "{{ ds }}"},
    )

    silver_check_op = PythonOperator(
        task_id="check_silver_quality",
        python_callable=check_silver_not_empty,
        op_kwargs={"execution_date": "{{ ds }}"},
    )

    gold_check_op = PythonOperator(
        task_id="check_gold_quality",
        python_callable=check_gold_loaded,
        op_kwargs={"execution_date": "{{ ds }}"},
    )

    extract_op >> transform_op >> load_op >> silver_check_op >> gold_check_op
