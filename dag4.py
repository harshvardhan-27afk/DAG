from datetime import datetime

dag_id = "dag4"
schedule_interval = "@weekly"
start_date = datetime(2025, 4, 1)

def backup_db():
    print("Backing up database")

def verify_backup():
    print("Verifying backup integrity")

tasks = [
    {"task_id": "backup_db", "callable": backup_db, "dependencies": []},
    {"task_id": "verify_backup", "callable": verify_backup, "dependencies": ["backup_db"]},
]
