from project.extraction.api_extractor import fetch_user_events
from project.extraction.raw_reader import load_raw_events
from project.extraction.raw_writer import save_raw_events
from project.common.config import API_URL


def extract_raw_events(execution_date: str) -> None:
    """
    BRONZE layer ingestion.

    Guarantees that raw events exist for execution_date.
    Prefers existing raw data, otherwise fetches from API.
    """

    try:
        events = load_raw_events(execution_date)
        print(f"[BRONZE] Using existing raw data for {execution_date}")

    except FileNotFoundError:
        print(f"[BRONZE] No raw data for {execution_date}, fetching from API")
        events = fetch_user_events(API_URL)
        save_raw_events(execution_date, events)

        print(f"[BRONZE] Saved {len(events)} raw events")

    # Important: NO return
