import os
import pandas as pd
from dotenv import load_dotenv
from google.cloud import storage

load_dotenv()

PROJECT_ID = os.getenv("GCP_PROJECT_ID")
BUCKET_NAME = os.getenv("GCP_BUCKET_NAME")
FILE_NAME = "student_productivity_distraction_dataset_20000.csv"


def upload_to_bucket(bucket_name, source_file_name):
    try:
        client = storage.Client(project=PROJECT_ID)
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(source_file_name)
        blob.upload_from_filename(source_file_name)
        print(f"File {source_file_name} uploaded to bucket {bucket_name}")
    except Exception as e:
        print(f"Error uploading to bucket: {e}")
        raise


def upload_file_to_bucket(local_file_name):
    try:
        client = storage.Client(project=PROJECT_ID)
        bucket = client.bucket(BUCKET_NAME)
        blob = bucket.blob(local_file_name)
        blob.upload_from_filename(local_file_name)
        print(f"{local_file_name} uploaded to bucket {BUCKET_NAME}")
    except Exception as e:
        print(f"Error uploading {local_file_name}: {e}")
        raise


def load_from_bucket(bucket_name, file_name):
    try:
        client = storage.Client(project=PROJECT_ID)
        bucket = client.bucket(bucket_name)
        blob = bucket.blob(file_name)
        local_path = os.path.join(os.path.dirname(__file__), "data_from_cloud.csv")
        blob.download_to_filename(local_path)
        print(f"File downloaded from bucket {bucket_name}")
        return pd.read_csv(local_path)
    except Exception as e:
        print(f"Error loading from bucket: {e}")
        raise


# no longer needed code: upload_to_bucket(BUCKET_NAME, FILE_NAME)

cleanedData = load_from_bucket(BUCKET_NAME, FILE_NAME)

print(f"Dataset loaded: {cleanedData.shape[0]} rows, {cleanedData.shape[1]} columns")
print(cleanedData.head())
