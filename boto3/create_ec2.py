import boto3
from  pprint import pprint
 # Open AWS console
aws_console = boto3.Session(profile_name='boto3-user')

# Opening EC2 console
ec2_console_client = aws_console.client(service_name='ec2', region_name='us-east-1')

response = ec2_console_client.run_instances(
    ImageId='string',
    InstanceType='t2.micro',
    KeyName='my_work',
    MaxCount=1,
    MinCount=1,
    SecurityGroupIds=[
        'string',
    ],
    # SecurityGroups=[
    #     'DevOps-SG',
    # ],
    SubnetId= 'string',
    IamInstanceProfile={
        # 'Arn': 'string',
        'Name': 'EC2-S3-Full_Access' 
        },
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'boto3-VM-IAM',
                },
            ],
        }
    ]    
)
