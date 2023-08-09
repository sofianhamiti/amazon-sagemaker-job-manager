from utils import get_config, get_iam_role, get_spark_job


if __name__ == "__main__":
    # IAM ROLE
    iam_role = get_iam_role()

    # CONFIG
    config = get_config()

    # RUN SPARK JOB
    print("RUN SPARK JOB")
    spark_job = get_spark_job(iam_role=iam_role, cfg=config["spark"])

    spark_job.run(
        submit_app=config["spark"]["entry_point"],
        submit_files=[config["spark"]["sql_script"]],
        logs=False,
    )
