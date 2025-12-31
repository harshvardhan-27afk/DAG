from datetime import datetime

dag_id = "dag2"
schedule_interval = "0 6 * * *"  # daily at 06:00
start_date = datetime(2025, 2, 1)

def fetch_users():
    print("Fetching users")

def clean_users():
    print("Cleaning user data")

tasks = [
    {"task_id": "fetch_users", "callable": fetch_users, "dependencies": []},
    {"task_id": "clean_users", "callable": clean_users, "dependencies": ["fetch_users"]},
]
