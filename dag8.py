from datetime import datetime

dag_id = "dag8"
schedule_interval = "*/15 * * * *"  # every 15 minutes
start_date = datetime(2025, 8, 1)

def heartbeat():
    print("Heartbeat ping")

def rotate_logs():
    print("Rotating logs")

tasks = [
    {"task_id": "heartbeat", "callable": heartbeat, "dependencies": []},
    {"task_id": "rotate_logs", "callable": rotate_logs, "dependencies": ["heartbeat"]},
]
