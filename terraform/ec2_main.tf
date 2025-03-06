
resource "aws_instance" "EKS-VM" {
    ami = "ami-0375a362a4deff13f"
    subnet_id = "subnet-084a18eae9dbb2283"
    security_groups = [ "sg-09ff92fcd6b3366cb" ]
    key_name = "my_work"
    instance_type = "t2.small"
    iam_instance_profile = "EC2-S3-Full_Access"
    tags = {
    "Name" = "EKS-terraform-VM"
    "Owner" = "DevOps"
    }
}