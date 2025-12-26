from typing import Dict, List
from collections import defaultdict


def count_actions_per_user(events: List[Dict]) -> Dict[int, int]:
    user_action_count = defaultdict(int)
    for event in events:
        user_id = event["user_id"]
        user_action_count[user_id] += 1

    return dict(user_action_count)