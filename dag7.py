from datetime import datetime

dag_id = "dag7"
schedule_interval = "@daily"
start_date = datetime(2025, 7, 1)

def scrape_site():
    print("Scraping website A")

def parse_html():
    print("Parsing HTML and extracting items")

def save_items():
    print("Saving items to DB")

tasks = [
    {"task_id": "scrape_site", "callable": scrape_site, "dependencies": []},
    {"task_id": "parse_html", "callable": parse_html, "dependencies": ["scrape_site"]},
    {"task_id": "save_items", "callable": save_items, "dependencies": ["parse_html"]},
]
