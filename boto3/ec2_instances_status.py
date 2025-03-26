import boto3
from pprint import pprint

## Open AWS Consloe
iam_console = boto3.Session(profile_name='boto3-user')

## Open Ec2 service/Client
ec2_console_client = iam_console.client(service_name='ec2', region_name='us-east-1')

## Created empty list to store the all the instances Id's
all_instances = []

## Created emply list to store all the stoped instances Id's
stopped_instances = []

## Created emply list to store all the running instances Id's
running_instances = []

list_ec2_instances = ec2_console_client.describe_instances()['Reservations']

### Listing all the Instance 
for ec2_instances in list_ec2_instances:
    for instance_id in ec2_instances['Instances']:
        instances = instance_id['InstanceId']
        ## append instacnes to all_instacnes list
        all_instances.append(instances)
    
print('Listing all Available instances: \n', all_instances)

ec2_instances_status = ec2_console_client.describe_instance_status(
    InstanceIds = all_instances,
    IncludeAllInstances = True
)['InstanceStatuses']

for value in ec2_instances_status:
    instance_id_value = value['InstanceId']
    status = value['InstanceState']['Name']
    if status == 'stopped':
        ## appending instacnes_id to stopped_instances list
        stopped_instances.append(instance_id_value)
    else:
        running_instances.append(instance_id_value)

print('Listing all stopped instances: \n',stopped_instances)
print('Listing all Running instances: \n',running_instances)
