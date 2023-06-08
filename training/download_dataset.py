"""download_dataset.py

This script downloads the dataset from AWS S3 buckets. 

Usage
-----
    python download_dataset.py.

Returns
-------
    Download dataset in "Dataset" folder.
"""

# Os library.
import os

# Other libraries.
import boto3
from cloudpathlib import CloudPath
from dotenv import load_dotenv

# Loads environment variables and fetch credentials.
load_dotenv()
aws_access_key_id = os.environ.get("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")

# Sets an AWS resource and point thr bucket.
s3 = boto3.resource(
    "s3",
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)
bucket = s3.Bucket("anyoneai-datasets")


# Shows the files inside the bucket.
print("Available files:")

for file in bucket.objects.filter(Prefix="credit-data-2010"):
    print("=>",file)

# download dataset
dataset = CloudPath("s3://anyoneai-datasets/credit-data-2010/")
dataset.download_to("dataset")