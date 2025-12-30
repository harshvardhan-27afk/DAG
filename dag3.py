from datetime import datetime

dag_id = "dag3"
schedule_interval = "@hourly"
start_date = datetime(2025, 3, 1)

def poll_api():
    print("Polling external API")

def update_index():
    print("Updating search index")

tasks = [
    {"task_id": "poll_api", "callable": poll_api, "dependencies": []},
    {"task_id": "update_index", "callable": update_index, "dependencies": ["poll_api"]},
]
