import os
import sys
import yaml
import logging
import sagemaker
from utils import get_training_job

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    # IAM ROLE
    iam_role = sagemaker.get_execution_role()

    # CONFIG
    with open("cfg/cfg.yaml") as f:
        config = yaml.load(f, Loader=yaml.SafeLoader)

    # RUN TRAINING JOB
    logging.info("RUN TRAINING JOB")
    training_job = get_training_job(iam_role=iam_role, cfg=config["training"])
    training_job.fit()
