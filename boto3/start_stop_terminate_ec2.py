import boto3

iam_console = boto3.Session(profile_name='boto3-user')
ec2_console_client = iam_console.client(service_name='ec2', region_name='us-east-1')

## Stop Instance
stop_instance = ec2_console_client.stop_instances(
    InstanceIds=[
        'string'
    ]
)
## Start Instance
start_instance = ec2_console_client.start_instances(
    InstanceIds=[
        'string'
    ]
)

## Terminate Instances
terminate_instance = ec2_console_client.terminate_instances(
    InstanceIds=[
        'string'
    ]
)