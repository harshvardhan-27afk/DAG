from datetime import datetime

dag_id = "dag1"
schedule_interval = "@daily"
start_date = datetime(2025, 1, 1)

def extract():
    print("Extracting data for dag1")

def transform():
    print("Transforming data for dag1")

def load():
    print("Loading data for dag1")

tasks = [
    {"task_id": "extract", "callable": extract, "dependencies": []},
    {"task_id": "transform", "callable": transform, "dependencies": ["extract"]},
    {"task_id": "load", "callable": load, "dependencies": ["transform"]},
]
