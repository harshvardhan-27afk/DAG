from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator


def task_func():
    print("hello")


# ❌ ERROR 1: Multiple DAG definitions
dag1 = DAG(
    dag_id="bad_dag_1",
    schedule_interval="61 * * * *",   # ❌ ERROR 2: Invalid cron
    start_date=datetime("2024", 1, 1), # ❌ ERROR 3: start_date invalid
    catchup="False"                   # ❌ ERROR 4: catchup not boolean
)

dag2 = DAG(
    dag_id="bad_dag_2",
    schedule_interval="@yearly"       # ❌ ERROR 5: unsupported preset
)


# ❌ ERROR 6: Missing task_id
task_a = PythonOperator(
    python_callable=task_func,
    dag=dag1
)

# ❌ ERROR 7: Duplicate task_id
task_b = PythonOperator(
    task_id="task_1",
    python_callable=task_func,
    dag=dag1
)

task_c = PythonOperator(
    task_id="task_1",   # duplicate
    python_callable=task_func,
    dag=dag1
)

# ❌ ERROR 8: Dependency on undefined task
task_b >> task_x

# ❌ ERROR 9: Self dependency
task_b >> task_b

# ❌ ERROR 10: Cycle in DAG
task_b >> task_c
task_c >> task_b
