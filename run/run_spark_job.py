import os
import sys
import yaml
import logging
import sagemaker
from utils import get_spark_job

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    # IAM ROLE
    iam_role = sagemaker.get_execution_role()

    # CONFIG
    with open("cfg/cfg.yaml") as f:
        config = yaml.load(f, Loader=yaml.SafeLoader)

    # RUN SPARK JOB
    logging.info("RUN SPARK JOB")
    spark_job = get_spark_job(iam_role=iam_role, cfg=config["processing"])
    spark_job.run(submit_app=config["processing"]["entry_point"], logs=False)
