import json
import os

from project.common.config import SILVER_EVENTS_DIR, EVENTS_FILENAME


def check_silver_not_empty(execution_date: str) -> None:
    silver_file = os.path.join(
        SILVER_EVENTS_DIR,
        f"date={execution_date}",
        EVENTS_FILENAME,
    )

    with open(silver_file) as f:
        events = json.load(f)

    if not events:
        raise ValueError(
            f"[DQ FAIL] SILVER is empty for {execution_date}"
        )

    print(f"[DQ PASS] SILVER has {len(events)} events for {execution_date}")
