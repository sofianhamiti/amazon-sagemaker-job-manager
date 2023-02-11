import os
import logging
from pyspark.sql import SparkSession

logging.basicConfig(level=logging.INFO)


def prepare_data():
    spark = SparkSession.builder.appName("PySparkApp").getOrCreate()

    # DOWNLOAD DATA FROM S3 PATH
    print("DOWNLOADING DATA NOW")
    # df = spark.read.csv(args.s3_input, header=True)
    print(os.environ)
    # ==================================================
    # ============= DO PROCESSING HERE =================
    # ==================================================

    # UPLOAD PROCESSED DATA TO S3
    # df.write.save(args.s3_output, format='csv', header=True)


if __name__ == "__main__":
    prepare_data()
