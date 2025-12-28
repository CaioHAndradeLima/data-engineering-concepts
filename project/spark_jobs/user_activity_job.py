from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count

from project.common.config import SILVER_EVENTS_DIR


def run_user_activity_job(execution_date: str):
    spark = (
        SparkSession.builder
        .appName("UserActivityJob")
        .getOrCreate()
    )

    silver_path = f"{SILVER_EVENTS_DIR}/date={execution_date}"

    # 1️⃣ READ
    df = spark.read.json(silver_path)

    # 2️⃣ TRANSFORM
    result = (
        df
        .groupBy(col("user_id"))
        .agg(count("*").alias("action_count"))
    )

    # 3️⃣ SHOW (for now)
    result.show()

    spark.stop()
