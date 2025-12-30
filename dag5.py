from datetime import datetime

dag_id = "dag5"
schedule_interval = "@monthly"
start_date = datetime(2025, 5, 1)

def export_reports():
    print("Exporting monthly reports")

def notify_team():
    print("Notifying team about reports")

tasks = [
    {"task_id": "export_reports", "callable": export_reports, "dependencies": []},
    {"task_id": "notify_team", "callable": notify_team, "dependencies": ["export_reports"]},
]
