from sagemaker.estimator import Framework
from sagemaker.processing import ScriptProcessor
from sagemaker.processing import FrameworkProcessor
from sagemaker.spark.processing import PySparkProcessor


def get_training_job(iam_role, cfg):
    estimator = ContainerEstimator(
        role=iam_role,
        image_uri=cfg["image_uri"],
        entry_point=cfg["entry_point"],
        source_dir=cfg["source_dir"],
        hyperparameters=cfg["hyperparameters"],
        instance_count=cfg["instance_count"],
        instance_type=cfg["instance_type"],
        disable_profiler=True,
    )
    return estimator


def get_spark_job(iam_role, cfg):
    spark_processor = PySparkProcessor(
        role=iam_role,
        framework_version="3.1",
        env=cfg["parameters"],
        instance_count=cfg["instance_count"],
        instance_type=cfg["instance_type"],
    )
    return spark_processor


def get_processing_job(iam_role, cfg):
    processor = ScriptProcessor(
        role=iam_role,
        image_uri=cfg["image_uri"],
        command=["python3"],
        env=cfg["parameters"],
        instance_count=cfg["instance_count"],
        instance_type=cfg["instance_type"],
    )
    return processor


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
