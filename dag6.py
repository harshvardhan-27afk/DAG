from datetime import datetime

dag_id = "dag6"
schedule_interval = "0 */4 * * *"  # every 4 hours
start_date = datetime(2025, 6, 1)

def collect_metrics():
    print("Collecting metrics")

def aggregate_metrics():
    print("Aggregating metrics")

def store_metrics():
    print("Storing metrics to warehouse")

tasks = [
    {"task_id": "collect_metrics", "callable": collect_metrics, "dependencies": []},
    {"task_id": "aggregate_metrics", "callable": aggregate_metrics, "dependencies": ["collect_metrics"]},
    {"task_id": "store_metrics", "callable": store_metrics, "dependencies": ["aggregate_metrics"]},
]
