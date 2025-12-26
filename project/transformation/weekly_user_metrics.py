from datetime import datetime, timedelta
from typing import List, Dict


def users_with_first_week_purchase(events: List[Dict]) -> int:
    """
    Count users who made their first purchase within 7 days of their first event.
    """
    user_first_event = {}
    user_first_purchase = {}

    for event in events:
        user_id = event["user_id"]
        event_time = datetime.fromisoformat(event["timestamp"])

        if user_id not in user_first_event:
            user_first_event[user_id] = event_time

        if event["action"] == "purchase" and user_id not in user_first_purchase:
            user_first_purchase[user_id] = event_time

    count = 0
    for user_id in user_first_purchase:
        if user_first_purchase[user_id] - user_first_event[user_id] <= timedelta(days=7):
            count += 1

    return count
