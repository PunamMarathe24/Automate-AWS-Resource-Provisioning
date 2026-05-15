import boto3

iam = boto3.client('iam')

user_name = "demo-user12"

response = iam.create_user(
    UserName=user_name
)

print("IAM User Created:", user_name)

iam.attach_user_policy(
    UserName="demo-user12",
    PolicyArn="arn:aws:iam::164885463874:user/demo-user12"
)

print("Policy Attached")
