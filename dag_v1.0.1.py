from airflow import DAG
from airflow.operators.bash import BashOperator
import pendulum


my_dag = DAG(
    "dag_v1.0.1",
    schedule="0 * * * *",
    start_date=pendulum.datetime(2023, 1, 1, tz="UTC"),
    catchup=False,
)

hello = BashOperator(
    task_id="hello",
    dag=my_dag,
    bash_command='echo "hello"',
)

world = BashOperator(
    task_id="world",
    dag=my_dag,
    bash_command='echo "world"',
)

hello >> world
