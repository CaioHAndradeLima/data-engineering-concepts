import requests
import time
from typing import List, Dict


class RemoteDataUnavailable(Exception):
    """Raised when remote data cannot be fetched."""


def fetch_user_events(
    url: str,
    timeout_seconds: int = 10,
    max_retries: int = 3,
    retry_delay_seconds: int = 2
) -> List[Dict]:
    """
    Fetch raw user event data from a remote API.

    This function assumes NO local fallback.
    If the API is down, the pipeline must fail loudly.
    """

    for attempt in range(1, max_retries + 1):
        try:
            print(f"[EXTRACT] Fetching data (attempt {attempt}/{max_retries})")

            response = requests.get(url, timeout=timeout_seconds)
            response.raise_for_status()

            data = response.json()

            if not isinstance(data, list):
                raise ValueError("API response is not a list")

            print(f"[EXTRACT] Retrieved {len(data)} events")
            return data

        except Exception as error:
            print(f"[ERROR] Fetch failed: {error}")

            if attempt == max_retries:
                raise RemoteDataUnavailable(
                    "Remote API unavailable after retries"
                ) from error

            time.sleep(retry_delay_seconds)
