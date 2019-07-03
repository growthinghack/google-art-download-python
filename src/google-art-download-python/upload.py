import logging
import boto3
from botocore.exceptions import ClientError
import os

def upload_file(file_name, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    bucket = os.environ['AWS_S3_BUCKET']

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        logging.info('Going to upload:')
        logging.info(file_name)
        logging.info(bucket)
        logging.info(object_name)
        
        response = s3_client.upload_file(file_name, bucket, object_name, ExtraArgs={'ACL': 'public-read'})
        bucket_location = boto3.client('s3').get_bucket_location(Bucket=bucket)
        object_url = "https://s3-{0}.amazonaws.com/{1}/{2}".format(
          bucket_location['LocationConstraint'],
          bucket,
          object_name)
        logging.info(object_url)
        return object_url
    except ClientError as e:
        logging.error(e)
        return False