import os
import sys
import yaml
import sagemaker
from sagemaker.pytorch import PyTorch
from sagemaker.estimator import Estimator
from sagemaker.processing import FrameworkProcessor
from sagemaker.spark.processing import PySparkProcessor

sys.path.append(os.path.join(os.path.dirname(__file__), ".."))


def get_config():
    with open("cfg/cfg.yaml") as f:
        config = yaml.load(f, Loader=yaml.SafeLoader)
    return config


def get_iam_role():
    iam_role = sagemaker.get_execution_role()
    return iam_role


def get_processing_job(iam_role, cfg):
    processor = FrameworkProcessor(
        role=iam_role,
        image_uri=cfg["base_image"],
        estimator_cls=PyTorch,
        env=cfg["parameters"],
        instance_count=cfg["instance_count"],
        instance_type=cfg["instance_type"],
        framework_version=None,
    )
    return processor


def get_spark_job(iam_role, cfg):
    spark_processor = PySparkProcessor(
        role=iam_role,
        framework_version="3.3",
        env=cfg["parameters"],
        instance_count=cfg["instance_count"],
        instance_type=cfg["instance_type"],
    )
    return spark_processor


def get_training_job(iam_role, cfg):
    estimator = Estimator(
        role=iam_role,
        image_uri=cfg["base_image"],
        entry_point=cfg["entry_point"],
        source_dir=cfg["source_dir"],
        hyperparameters=cfg["parameters"],
        instance_count=cfg["instance_count"],
        instance_type=cfg["instance_type"],
        disable_profiler=True,
    )
    return estimator