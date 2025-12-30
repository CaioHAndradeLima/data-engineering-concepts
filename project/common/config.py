import os

# --------------------------------------------------
# Base paths
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")

# --------------------------------------------------
# API
# --------------------------------------------------

API_URL = "https://dummyjson.com/c/f975-aded-4b95-aeea"

# --------------------------------------------------
# Business rules
# --------------------------------------------------

FIRST_WEEK_DAYS = 7

# --------------------------------------------------
# DATA LAKE (Bronze / Silver / Gold)
# --------------------------------------------------

# BRONZE — raw, immutable, source of truth
RAW_DIR = os.path.join(DATA_DIR, "raw")
RAW_EVENTS_DIR = os.path.join(RAW_DIR, "events")

# SILVER — cleaned / normalized
SILVER_EVENTS_DIR = "/opt/spark/data/silver/events"

# GOLD — analytics-ready (file-based if needed later)
GOLD_DIR = "/opt/spark/data/gold"
# Standard filenames
EVENTS_FILENAME = "events.json"

# --------------------------------------------------
# WAREHOUSE (Postgres)
# --------------------------------------------------

WAREHOUSE_SCHEMA = "public"
USER_ACTIVITY_TABLE = "user_activity_daily"

# --------------------------------------------------
# (Legacy — keep only if you want backward compatibility)
# --------------------------------------------------
# OUTPUT_DIR = os.path.join(BASE_DIR, "output")
# USER_ACTIVITY_FILE = "user_activity_summary.csv"
