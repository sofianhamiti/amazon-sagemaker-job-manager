from utils import get_config, get_iam_role, get_training_job


if __name__ == "__main__":
    # IAM ROLE
    iam_role = get_iam_role()

    # CONFIG
    config = get_config()

    # RUN TRAINING JOB
    print("RUN TRAINING JOB")
    training_job = get_training_job(iam_role=iam_role, cfg=config["training"])
    training_job.fit()
