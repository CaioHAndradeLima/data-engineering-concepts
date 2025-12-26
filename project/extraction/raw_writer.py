import json
import os
from project.common.config import RAW_EVENTS_DIR, EVENTS_FILENAME


def save_raw_events(execution_date: str, events: list[dict]) -> None:
    dir_path = os.path.join(
        RAW_EVENTS_DIR,
        f"date={execution_date}"
    )
    os.makedirs(dir_path, exist_ok=True)

    with open(os.path.join(dir_path, EVENTS_FILENAME), "w") as f:
        json.dump(events, f)
