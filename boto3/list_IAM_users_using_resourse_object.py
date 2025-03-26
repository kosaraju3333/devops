import boto3

## Creating AWS managment console session
aws_managment_console = boto3.session.Session(profile_name="boto3-user")

## Listing USER and ROLES names using resourse object.
#Creating resourese object 
iam_console = aws_managment_console.resource('iam')

## Listing all the USER names 
print("-----------Listing all the USERS-----------")
for each_user in iam_console.users.all():
    print(each_user.name)
 
## Listing all the ROLES names 
print("----------Listing all the ROLES----------")
for each_role in iam_console.roles.all():
    print(each_role.name)

## Listing all the Policies names
# print("----------Listing all the Policies--------------")
# for each_policies in iam_console.policies.all():
#     print(each_policies.arn)
