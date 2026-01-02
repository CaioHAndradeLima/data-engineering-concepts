import json
import os
from collections import defaultdict

from project.common.config import SILVER_EVENTS_DIR, EVENTS_FILENAME


def spark_like_user_activity_job(execution_date: str) -> dict[int, int]:
    silver_file = os.path.join(
        SILVER_EVENTS_DIR,
        f"date={execution_date}",
        EVENTS_FILENAME,
    )

    with open(silver_file) as f:
        events = json.load(f)

    counts = defaultdict(int)

    for e in events:
        counts[e["user_id"]] += 1

    return dict(counts)
