# Import all the modules and libraries
import boto3
from pprint import pprint

# Open AWS Management Console
iam_management_console = boto3.Session(profile_name='boto3-user')

# Open ec2 service console
ec2_console_client = iam_management_console.client(service_name='ec2', region_name='us-east-1')

#ec2 insatnce list
ec2 = ec2_console_client.describe_instances()['Reservations'][0]['Instances'][0]['InstanceId']
print(ec2)

print("################# Iteration ##############")

## Iteration
ec2_list = ec2_console_client.describe_instances()['Reservations']
for ec2_id in ec2_list:
    for value in ec2_id['Instances']:
        print(value['InstanceId'])

