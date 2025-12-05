from datetime import datetime, timedelta

# This is a dummy DAG for Pi-Flow testing.
# It is NOT actually executed like Airflow, but Pi-Flow will parse it.

DAG = {
    "dag_id": "sample_dag",
    "description": "A simple test DAG for Pi-Flow GitHub sync",
    "schedule_interval": "@daily",
    "start_date": str(datetime(2024, 1, 1)),
    "tasks": [
        {
            "task_id": "task_1",
            "type": "bash",
            "command": "echo 'Task 1 running'",
            "upstream": []
        },
        {
            "task_id": "task_2",
            "type": "bash",
            "command": "echo 'Task 2 depends on Task 1'",
            "upstream": ["task_1"]
        }
    ]
}
