import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
    ImageId='ami-05d2d839d4f73aafb',  # Ubuntu AMI (ap-south-1)
    MinCount=2,
    MaxCount=4,
    InstanceType='t3.micro',
    KeyName='new-key1'
)

print("EC2 Instance Launched:", instance[0].id)
