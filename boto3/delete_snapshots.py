import boto3
from pprint import pprint
## Open AWS Console
aws_console = boto3.Session(profile_name='boto3-user')
## Open ec2 Console
ec2_console_client = aws_console.client(service_name='ec2', region_name='us-east-1')
## empty_list
list_snapshots = []
## ec2_snapshot client method to list all available snapshots
snapshots_list = ec2_console_client.describe_snapshots(
     OwnerIds=[
        'self'
    ]
    # SnapshotIds=[
    #      ''
    # ]
     )['Snapshots']
for value in snapshots_list:
     snapshot_id = value['SnapshotId']
     volume_id = value['VolumeId']
    #  print('snapshot ids: ', value['SnapshotId'])
    #  list_snapshots.append(snapshot_id)
     if not volume_id:
            ## Deleting Snapshot
            ec2_console_client.delete_snapshot(SnapshotID = snapshot_id)
            print(f"Deleted EBS snapshot {snapshot_id} as it was not attached to any volume.")
     else:
           ## Checking Volume it exists 
           try:
                print("...1...")
                volume_response = ec2_console_client.describe_volumes(
                     VolumeIds= [
                          volume_id
                        ]
                    )
                print("...2...")
                if not volume_response['Volumes'][0]['Attachments']:
                      print("...2_1...")
                      ec2_console_client.delete_snapshot(SnapshotID = snapshot_id)
                      print(f"Deleted EBS snapshot {snapshot_id} as it was taken from a volume not attached to any running instance.")
           except ec2_console_client.exceptions.ClientError as e:
                print("...3...")
                if e.response['Error']['Code'] == 'InvalidVolume.NotFound':
                    print("...4...")
                    ec2_console_client.delete_snapshot(SnapshotId=snapshot_id)
                    print(f"Deleted EBS snapshot {snapshot_id} as its associated volume was not found.")            
# pprint(snapshots_list)