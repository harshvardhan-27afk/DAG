from datetime import datetime

dag_id = "dag10"
schedule_interval = "0 0 * * 0"  # weekly on Sunday midnight
start_date = datetime(2025, 10, 1)

def snapshot_db():
    print("Taking DB snapshot")

def transfer_snapshot():
    print("Transferring snapshot to archive")

def cleanup_old_snapshots():
    print("Cleaning up old snapshots")

tasks = [
    {"task_id": "snapshot_db", "callable": snapshot_db, "dependencies": []},
    {"task_id": "transfer_snapshot", "callable": transfer_snapshot, "dependencies": ["snapshot_db"]},
    {"task_id": "cleanup_old_snapshots", "callable": cleanup_old_snapshots, "dependencies": ["transfer_snapshot"]},
]
