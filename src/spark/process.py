import os
import logging
from string import Template
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
    # print("DOWNLOADING DATA NOW")
    # s3_input = os.environ["s3_input"]
    # df = spark.read.csv(s3_input, header=True)

    # ==================================================
    # ============= DO SQL PROCESSING HERE =================
    # ==================================================

    print("READING SQL QUERY FROM .SQL FILE")
    with open("/opt/ml/processing/input/files/script.sql", "r") as sql_script:
        sql_query_template = sql_script.read()

    print("ADDING ENVIRONMENT VARIABLES' VALUES TO THE SQL QUERY")
    template = Template(sql_query_template)
    sql_query = template.safe_substitute(
        first_name=f"'{os.environ['first_name']}'",
        last_name=f"'{os.environ['last_name']}'",
        age=f"'{os.environ['age']}'",
    )

    print(sql_query)

    print("RUNNING THE SQL QUERY")
    # Execute the SQL query using PySpark
    df = spark.sql(sql_query)

    # Show the results
    df.show()

    # UPLOAD PROCESSED DATA TO S3 OUTPUT LOCATION
    # print("UPLOADING DATA TO S3")
    # s3_output = os.environ["s3_output"]
    # df.write.parquet(s3_output, mode="overwrite")


if __name__ == "__main__":
    prepare_data()
