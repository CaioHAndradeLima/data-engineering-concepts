import csv
import os
from typing import Dict


def save_user_activity_summary(
    summary: Dict[int, int],
    output_dir: str,
    filename: str,
    execution_date: str
) -> None:
    """
    Save user activity summary partitioned by execution date.
    This makes the pipeline idempotent and backfill-safe.
    """
    dated_output_dir = os.path.join(output_dir, execution_date)
    os.makedirs(dated_output_dir, exist_ok=True)

    file_path = os.path.join(dated_output_dir, filename)

    print(f"[LOADER] Writing CSV to {file_path}")

    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["user_id", "total_actions"])

        for user_id, total_actions in summary.items():
            writer.writerow([user_id, total_actions])
