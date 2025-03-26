import boto3

## Creating AWS managemnt conslole session
aws_managment_console = boto3.Session(profile_name='boto3-user')

iam_console_client = aws_managment_console.client('iam')

# users_list = iam_console_client.list_users()['ResponseMetadata']['HTTPHeaders']['content-length']
#['Users'][0]['UserName']

# print(users_list)

for each_user in iam_console_client.list_users()['Users']:
    print(each_user['UserName'])

# for each_role in iam_console_client.list_roles()['Roles']:
#     print(each_role['RoleName'])

# print("data type :", type(each_user))




