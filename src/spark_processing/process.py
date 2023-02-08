import os
import logging
import argparse
from pyspark.sql import SparkSession

logging.basicConfig(level=logging.INFO)


def prepare_data(args):
    spark = SparkSession.builder.appName("PySparkApp").getOrCreate()

    # DOWNLOAD DATA FROM S3 PATH
    print("DOWNLOADING DATA NOW")
    print(os.environ["file_name"])
    # df = spark.read.csv(args.s3_input, header=True)

    # ==================================================
    # ============= DO PROCESSING HERE =================
    # ==================================================

    # UPLOAD PROCESSED DATA TO S3
    # df.write.save(args.s3_output, format='csv', header=True)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--s3_input", type=str, help="s3 input path")
    parser.add_argument("--s3_output", type=str, help="s3 output path")
    args, _ = parser.parse_known_args()

    prepare_data(args)
