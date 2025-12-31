from datetime import datetime

dag_id = "dag9"
schedule_interval = "@daily"
start_date = datetime(2025, 9, 1)

def compute_stats():
    print("Computing daily stats")

def publish_stats():
    print("Publishing stats to dashboard")

tasks = [
    {"task_id": "compute_stats", "callable": compute_stats, "dependencies": []},
    {"task_id": "publish_stats", "callable": publish_stats, "dependencies": ["compute_stats"]},
]
