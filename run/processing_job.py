from utils import get_config, get_iam_role, get_processing_job


if __name__ == "__main__":
    # IAM ROLE
    iam_role = get_iam_role()

    # CONFIG
    config = get_config()

    # RUN PROCESSING JOB
    print("RUN PROCESSING JOB")
    processing_job = get_processing_job(iam_role=iam_role, cfg=config["processing"])
    processing_job.run(
        code=config["processing"]["entry_point"],
        source_dir=config["processing"]["source_dir"],
    )
