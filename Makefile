all: spark-job training-job

spark-job:
	python run/spark_job.py

training-job:
	python run/training_job.py
