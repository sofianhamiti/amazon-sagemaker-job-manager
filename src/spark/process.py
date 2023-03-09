import os
import logging
from pyspark.sql import SparkSession

logging.basicConfig(level=logging.INFO)


def prepare_data():
    spark = (
        SparkSession.builder.appName("PySparkApp")
        .config(
            "fs.s3a.aws.credentials.provider",
            "com.amazonaws.auth.ContainerCredentialsProvider",
        )
        .config(
            "spark.jars.packages",
            "org.apache.hadoop:hadoop-aws:3.2.2,com.amazonaws:aws-java-sdk-bundle:1.11.888",
        )
        .getOrCreate()
    )

    # DOWNLOAD DATA FROM S3 INPUT LOCATION
    print("DOWNLOADING DATA NOW")
    s3_input = os.environ["s3_input"]
    df = spark.read.csv(s3_input, header=True)

    # ==================================================
    # ============= DO PROCESSING HERE =================
    # ==================================================

    # UPLOAD PROCESSED DATA TO S3 OUTPUT LOCATION
    print("UPLOADING DATA TO S3")
    s3_output = os.environ["s3_output"]
    df.write.parquet(
        s3_output,
        mode="overwrite",
    )


if __name__ == "__main__":
    prepare_data()
