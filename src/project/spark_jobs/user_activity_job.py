import sys
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count


def run_user_activity_job(execution_date: str) -> None:
    spark = (
        SparkSession.builder
        .appName("UserActivityJob")
        .master("local[*]")
        .getOrCreate()
    )

    # 📂 Paths INSIDE the Spark container
    silver_path = f"/opt/spark/project/data/silver/events/date={execution_date}"
    gold_path = f"/opt/spark/project/data/gold/user_activity/date={execution_date}"

    # 1️⃣ READ SILVER (JSON)
    df = spark.read.json(silver_path)

    # 2️⃣ TRANSFORM
    result_df = (
        df
        .groupBy(col("user_id"))
        .agg(count("*").alias("action_count"))
    )

    # 3️⃣ WRITE GOLD (Parquet)
    (
        result_df
        .write
        .mode("overwrite")
        .parquet(gold_path)
    )

    print(f"[SPARK] Wrote GOLD Parquet to {gold_path}")

    spark.stop()


if __name__ == "__main__":
    execution_date = sys.argv[1]
    run_user_activity_job(execution_date)
