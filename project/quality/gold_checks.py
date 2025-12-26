import os
import psycopg2


def check_gold_loaded(execution_date: str) -> None:
    conn = psycopg2.connect(
        host=os.getenv("ANALYTICS_DB_HOST"),
        port=os.getenv("ANALYTICS_DB_PORT"),
        dbname=os.getenv("ANALYTICS_DB_NAME"),
        user=os.getenv("ANALYTICS_DB_USER"),
        password=os.getenv("ANALYTICS_DB_PASSWORD"),
    )

    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT COUNT(*)
            FROM user_activity_daily
            WHERE activity_date = %s
            """,
            (execution_date,)
        )
        count = cur.fetchone()[0]

    conn.close()

    if count == 0:
        raise ValueError(
            f"[DQ FAIL] No GOLD rows for {execution_date}"
        )

    print(f"[DQ PASS] GOLD has {count} rows for {execution_date}")
