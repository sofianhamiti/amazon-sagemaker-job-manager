# all: processing-job spark-job training-job
all: processing-job

processing-job:
	python run/processing_job.py

# spark-job:
# 	python run/spark_job.py

# training-job:
# 	python run/training_job.py
