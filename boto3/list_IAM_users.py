# Import all the modules and libraries
import boto3
from pprint import pprint

# Open AWS Management Console
aws_managment_console = boto3.Session(profile_name='boto3-user')

# Open IAM Console
iam_console = aws_managment_console.client(service_name='iam')

# List IAM USERS
# Listing First USER from USERS list
user = iam_console.list_users()['Users'][0]['UserName']
pprint(user)

## Listing all the USERS through Iterating(for loop)
users_list = iam_console.list_users()
for each_user in users_list['Users']:
    pprint(each_user['UserName'])
