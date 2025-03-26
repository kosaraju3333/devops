import boto3
from pprint import pprint

def lambda_handler(event, context):
    ## Open AWS console session
    iam_console = boto3.Session(profile_name='boto3-user')

    ## Open EC2 Console
    ec2_console_client = iam_console.client(service_name='ec2', region_name='us-east-1')

    ## ec2 volumes client method
    list_volumes = ec2_console_client.describe_volumes()['Volumes']
    print('.......Not Found any Available Volumes___1.......')
    for volumes in list_volumes:
        print('.......Not Found any Available Volumes.......')
        volume_id = volumes['VolumeId']
        if volumes['State'] == 'available':
            print('Deleting Volume....: ', volume_id)
            ec2_console_client.delete_volume(VolumeId = volume_id)
            print('Deleted Volume: ', volume_id)
        else:
            print('.......Not Found any Available Volumes.......')
        