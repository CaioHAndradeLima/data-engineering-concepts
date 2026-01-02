import json
import os
from project.common.config import RAW_EVENTS_DIR, EVENTS_FILENAME


def load_raw_events(execution_date: str) -> list[dict]:
    path = os.path.join(
        RAW_EVENTS_DIR,
        f"date={execution_date}",
        EVENTS_FILENAME
    )

    with open(path) as f:
        return json.load(f)
