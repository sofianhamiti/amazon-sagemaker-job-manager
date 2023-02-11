import os
import sys
import yaml
import sagemaker
from sagemaker.pytorch import PyTorch
from sagemaker.estimator import Framework
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
        framework_version="3.1",
        env=cfg["parameters"],
        instance_count=cfg["instance_count"],
        instance_type=cfg["instance_type"],
    )
    return spark_processor


def get_training_job(iam_role, cfg):
    estimator = ContainerEstimator(
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


class ContainerEstimator(Framework):
    def __init__(
        self,
        entry_point,
        framework_version=None,
        py_version=None,
        source_dir=None,
        hyperparameters=None,
        image_uri=None,
        distribution=None,
        **kwargs
    ):
        super(ContainerEstimator, self).__init__(
            entry_point, source_dir, hyperparameters, image_uri=image_uri, **kwargs
        )
        self.framework_version = framework_version
        self.py_version = None

    def _configure_distribution(self, distributions):
        return None

    def create_model(
        self,
        model_server_workers=None,
        role=None,
        vpc_config_override=None,
        entry_point=None,
        source_dir=None,
        dependencies=None,
        image_uri=None,
        **kwargs
    ):
        return None
