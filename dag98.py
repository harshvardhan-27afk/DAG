from datetime import datetime, timedelta

dag_id = "user_activity_etl"

schedule_interval = "0 */6 * * *"  # Every 6 hours
start_date = datetime(2024, 1, 1)

def extract_activity():
    print("Extracting user activity data...")

def clean_activity():
    print("Cleaning raw activity logs...")

def load_activity():
    print("Loading activity data into warehouse...")

tasks = [
    {
        "task_id": "extract_activity",
        "callable": extract_activity,
        "dependencies": []
    },
    {
        "task_id": "clean_activity",
        "callable": clean_activity,
        "dependencies": ["extract_activity"]
    },
    {
        "task_id": "load_activity",
        "callable": load_activity,
        "dependencies": ["clean_activity"]
    }
]
