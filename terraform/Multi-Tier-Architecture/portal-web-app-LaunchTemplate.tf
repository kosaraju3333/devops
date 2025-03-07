## Creating AWS Launch Template

### Filtering or Getting our pre backed AMI

data "aws_ami" "portal-app-LT-ami" {

    filter {
        name = "tag:Name"
        values = ["Portal-app-AMI-V-03-spontansolutions.com"]
    }
}

resource "aws_launch_template" "portal-web-LT" {
    name = "portal-web-LT"
    image_id = data.aws_ami.portal-app-LT-ami.id
    key_name = "my_work"
    instance_type = var.portal-web-instance-type
    security_group_names = [ aws_security_group.portal-web-sg.id ]

    tags = {
        Name = var.portal-web-LT-name
        Owner = var.owner
    }
}