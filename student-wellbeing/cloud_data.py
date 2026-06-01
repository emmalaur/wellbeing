import os
import pandas as pd
from google.cloud import storage

PROJECT_ID = "student-wellbeing-project"
BUCKET_NAME = "student-wellbeing-effect"
FILE_NAME = "student_productivity_distraction_dataset_20000.csv"


def upload_to_bucket(bucket_name, source_file_name):
    client = storage.Client(project=PROJECT_ID)
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(source_file_name)
    blob.upload_from_filename(source_file_name)
    print(f"File {source_file_name} uploaded to bucket {bucket_name}")


def load_from_bucket(bucket_name, file_name):
    client = storage.Client(project=PROJECT_ID)
    bucket = client.bucket(bucket_name)
    blob = bucket.blob(file_name)
    local_path = os.path.join(os.path.dirname(__file__), "data_from_cloud.csv")
    blob.download_to_filename(local_path)
    print(f"File downloaded from bucket {bucket_name}")
    return pd.read_csv(local_path)


# upload_to_bucket(BUCKET_NAME, FILE_NAME)

cleanedData = load_from_bucket(BUCKET_NAME, FILE_NAME)

print(f"Dataset loaded: {cleanedData.shape[0]} rows, {cleanedData.shape[1]} columns")
print(cleanedData.head())
