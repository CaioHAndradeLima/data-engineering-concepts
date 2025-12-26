import json
from typing import List, Dict


def load_events_from_file(file_path: str) -> List[Dict]:
    """
    Extract user events from a local JSON file.

    This simulates reading data from an external source
    (API, data lake, S3, etc.) but keeps everything local
    for development and learning.
    """
    with open(file_path, "r") as file:
        return json.load(file)
