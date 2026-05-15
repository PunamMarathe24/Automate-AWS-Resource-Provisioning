import boto3

s3 = boto3.client('s3')

bucket_name = "punam-demo-bucket-12345"  # must be unique

response = s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1'
    }
)

print("S3 Bucket Created:", bucket_name)
