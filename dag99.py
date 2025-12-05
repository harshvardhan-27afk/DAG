from datetime import datetime, timedelta

# Pi-Flow Dummy DAG
dag_id = "daily_sales_pipeline"

schedule_interval = "@daily"
start_date = datetime(2024, 1, 1)

def extract_sales_data():
    print("Extracting sales data...")

def transform_sales_data():
    print("Transforming sales data...")

tasks = [
    {
        "task_id": "extract_sales_data",
        "callable": extract_sales_data,
        "dependencies": []
    },
    {
        "task_id": "transform_sales_data",
        "callable": transform_sales_data,
        "dependencies": ["extract_sales_data"]
    }
]
