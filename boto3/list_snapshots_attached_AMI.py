import boto3
from pprint import pprint

aws_console = boto3.Session(profile_name='boto3-user')
ec2_client = aws_console.client(service_name='ec2', region_name='us-east-1')

ami_response = ec2_client.describe_images(Owners=['self'])['Images']

for value in ami_response:
    AMI_ID = value['ImageId']
    for ebs in value['BlockDeviceMappings']:
        for key, value in ebs.items():
            if key == 'Ebs':
                snapshot_Id = value['SnapshotId']
                print(f'AMI_Id: {AMI_ID} and Snapshot_Id: {snapshot_Id}')


