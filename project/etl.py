import json
import os

from project.common.config import SILVER_EVENTS_DIR, EVENTS_FILENAME
from project.extraction.extract import extract_raw_events
from project.transformation.transform_event import transform_event
from project.transformation.user_activity_transformer import count_actions_per_user
from project.loading.postgres_loader.save_user_activity_daily import save_user_activity_daily


def extract(execution_date: str) -> None:
    """
    BRONZE layer entrypoint.
    """
    extract_raw_events(execution_date)


def transform(execution_date: str) -> None:
    """
    SILVER layer entrypoint.
    """
    transform_event(execution_date)


def load(execution_date: str) -> None:
    """
    GOLD layer load.

    Reads SILVER events,
    aggregates user activity,
    loads analytics-ready data into Postgres.
    """

    # 1️⃣ Read SILVER
    silver_file = os.path.join(
        SILVER_EVENTS_DIR,
        f"date={execution_date}",
        EVENTS_FILENAME,
    )

    with open(silver_file) as f:
        events = json.load(f)

    # 2️⃣ Aggregate
    summary: dict[int, int] = count_actions_per_user(events)

    # 3️⃣ Load into warehouse
    save_user_activity_daily(
        summary=summary,
        activity_date=execution_date,
    )

    print(f"[GOLD] Loaded {len(summary)} user metrics for {execution_date}")
