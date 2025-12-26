def clean_events(events: list[dict]) -> list[dict]:
    cleaned = []

    for e in events:
        if "user_id" not in e:
            continue

        cleaned.append({
            "user_id": int(e["user_id"]),
            "action": e.get("action"),
            "timestamp": e.get("timestamp"),
        })

    return cleaned
