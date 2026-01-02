# --------------------------------------------------
# DATA LAKE (shared storage)
# --------------------------------------------------

BASE_DATA_DIR = "/opt/airflow/data"

# BRONZE — raw, immutable
RAW_EVENTS_DIR = f"{BASE_DATA_DIR}/bronze/events"

# SILVER — cleaned / normalized
SILVER_EVENTS_DIR = f"{BASE_DATA_DIR}/silver/events"

# GOLD — analytics-ready
GOLD_DIR = f"{BASE_DATA_DIR}/gold"

EVENTS_FILENAME = "events.json"

# --------------------------------------------------
# API
# --------------------------------------------------

API_URL = "https://dummyjson.com/c/f975-aded-4b95-aeea"
