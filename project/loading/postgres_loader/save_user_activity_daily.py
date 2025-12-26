import os
import psycopg2
from datetime import date


def save_user_activity_daily(
    summary: dict[int, int],
    activity_date: str,
) -> None:
    conn = psycopg2.connect(
        host=os.getenv("ANALYTICS_DB_HOST"),
        port=os.getenv("ANALYTICS_DB_PORT"),
        dbname=os.getenv("ANALYTICS_DB_NAME"),
        user=os.getenv("ANALYTICS_DB_USER"),
        password=os.getenv("ANALYTICS_DB_PASSWORD"),
    )

    insert_sql = """
        INSERT INTO user_activity_daily (
            activity_date,
            user_id,
            action_count
        )
        VALUES (%s, %s, %s)
        ON CONFLICT (activity_date, user_id)
        DO UPDATE SET action_count = EXCLUDED.action_count;
    """

    with conn.cursor() as cur:
        for user_id, action_count in summary.items():
            cur.execute(
                insert_sql,
                (activity_date, user_id, action_count)
            )

    conn.commit()
    conn.close()
