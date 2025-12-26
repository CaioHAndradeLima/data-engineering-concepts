import json
import os

from project.common.config import RAW_EVENTS_DIR, SILVER_EVENTS_DIR, EVENTS_FILENAME
from project.transformation.clean_events import clean_events


def transform_event(execution_date: str) -> None:
    """
    SILVER layer transformation.

    Reads raw events from BRONZE,
    cleans / normalizes them,
    writes SILVER events.
    """

    # 1️⃣ Read from BRONZE
    raw_file = os.path.join(
        RAW_EVENTS_DIR,
        f"date={execution_date}",
        EVENTS_FILENAME,
    )

    with open(raw_file) as f:
        events = json.load(f)

    # 2️⃣ Clean / normalize
    cleaned = clean_events(events)

    # 3️⃣ Write to SILVER
    silver_dir = os.path.join(
        SILVER_EVENTS_DIR,
        f"date={execution_date}",
    )
    os.makedirs(silver_dir, exist_ok=True)

    silver_file = os.path.join(silver_dir, EVENTS_FILENAME)

    with open(silver_file, "w") as f:
        json.dump(cleaned, f)

    print(f"[SILVER] Stored {len(cleaned)} cleaned events for {execution_date}")
