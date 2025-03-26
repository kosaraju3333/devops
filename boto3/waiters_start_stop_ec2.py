import boto3

## Openong AWS console
aws_console = boto3.Session(profile_name='boto3-user')

## Opening ec2 Service/Client
ec2_console_client = aws_console.client(service_name='ec2', region_name='us-east-1')

############# Start Instance ##################
print('Starting Ec2 Instances')
## ec2 instance start clinet Methods 
instance_start = ec2_console_client.start_instances(
    InstanceIds=['string']
)
## Creating a waiter
instance_start_waiter = ec2_console_client.get_waiter('instance_running')
## Waiter Method
instance_start_waiter.wait(
    InstanceIds=['string']
)
print("Ec2 instance started")

############ Stop Instance #############
print('Ec2 instance Stopping ')
## ec2 instance stop Client Method
instance_stop = ec2_console_client.stop_instances(
    InstanceIds=['string']
)
## Create Waiter
instance_stop_waiter = ec2_console_client.get_waiter('instance_stopped')
## Waiter Method
instance_stop_waiter.wait(
    InstanceIds=['string']
)
print('Ec2 instance Stopped')