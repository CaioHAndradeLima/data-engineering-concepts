import os
import psycopg2

DB_CONFIG = {
    "host": os.getenv("ANALYTICS_DB_HOST", "localhost"),
    "port": os.getenv("ANALYTICS_DB_PORT", "5432"),
    "dbname": os.getenv("ANALYTICS_DB_NAME", "analytics"),
    "user": os.getenv("ANALYTICS_DB_USER", "airflow"),
    "password": os.getenv("ANALYTICS_DB_PASSWORD", "airflow"),
}

CREATE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS user_activity_daily (
    activity_date DATE NOT NULL,
    user_id INTEGER NOT NULL,
    action_count INTEGER NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT now(),

    CONSTRAINT user_activity_daily_pk
        PRIMARY KEY (activity_date, user_id)
);
"""


def main():
    print("Connecting to Postgres...")
    conn = psycopg2.connect(**DB_CONFIG)

    with conn.cursor() as cur:
        print("Creating table user_activity_daily (if not exists)...")
        cur.execute(CREATE_TABLE_SQL)

    conn.commit()
    conn.close()
    print("✅ Warehouse initialized")


if __name__ == "__main__":
    main()
