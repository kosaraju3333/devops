https://docs.google.com/document/d/1-34IR_hz1ngwLWET9t5XSwOWEPULcDByQTp0buqJvqk/edit?pli=1

**`Youtube link Boto3 and Lambda(I Learnt from This)-channel NAME- A Monk in Cloud** : https://www.youtube.com/watch?v=Ld1_vb1fH6c&list=PLjl2dJMjkDjlcI3SQErSq4UMX3okzafvO&index=1`

**`Youtube Link Boto3**: https://www.youtube.com/playlist?list=PLckUzKjgYDgbVbrLPpPl_MsDHQnKovLuH`

- https://devopslearning.medium.com/10-boto3-scripts-to-simplify-your-aws-journey-ad6ce6f99852
- https://techblogs.42gears.com/aws-automation-with-python-boto3/
- https://medium.com/@rahulsharan512/automating-aws-tasks-with-python-and-boto3-a-step-by-step-guide-1d4c7c93c773

Concepts of Boto3:

- Session
- Resources
- Client
- Meta
- Collections
- Waiters
- Paginators

1: Session:

- In simple words, it is just the **AWS Management Console**.
- Store configuration information (Credentials of Default user etc…).
- Allows us to create Service, Clients and Resources.
- It creates a default session for us when we need it.
- We can create multiple sessions in the same script!

2: Resource/Services(like s3 , ec2, iam…ect.. resource is northing but AWS services )

- You can choose anyone depending on your use case.
- Resource is **Higher Level Object** oriented service access.
- Resource objects are only available for a few AWS Services.
- Let us check which AWS Service has a Resource Object!!! - DEM😉
- **['cloudformation', 'cloudwatch', 'dynamodb', 'ec2', 'glacier', 'iam', 'opsworks', 's3', 'sns', 'sqs'] - Resource Object Available.**

3: Client/Service(like s3 , ec2, iam…ect.. resource is northing but AWS services):

- Client is **Low Level Service Access**.
- In simple terms, the output/response in case of Client will be in Dictionary, which needs more effort in implementing boto3 scripts.
- Whereas Resource is an object, we can use simple (.) operation.
- **All operations that we see in AWS Management Console can be done in Client whereas Resource does not guarantee you that. Some operations may not be supported.**
- If we do not have some operations in Resource we can enter into Client by using the **“Meta”** concept. Let us talk about this later! 😉
- Let us see how much effort is needed for both Resource and Client. - DEM😀

4: Meta

5: Collections:

6: Waiters:

- **It allows you to block the code until the process in completed**

7: Paginators:

- **If we have more than one page results then we use paginators**
- eg: For IAM service CLIENT method will list only 100 users. If we want to list more we use Paginators
- For S3 it has 1000 results, if want to print more than 1000 use Paginator.
- **The man advantage of Paginators is we get the result quickly**
