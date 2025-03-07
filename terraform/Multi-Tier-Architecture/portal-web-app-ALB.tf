### Creating ALB

resource "aws_lb" "portal-web-app-alb" {
    name = "Portal-web-app-ALB"
    internal = false
    load_balancer_type = "application"
    security_groups = [ aws_security_group.portal-web-sg.id ]
    subnets = [ aws_subnet.portal-vpc-public-subnet-1.id, aws_subnet.portal-vpc-public-subnet-2.id ]

    tags = {
      Owner = var.owner
    }
}

### Adding listiners to ALB


resource "aws_lb_listener" "portal-app-rule" {
  load_balancer_arn = aws_lb.portal-web-app-alb.arn
  port = "80"
  protocol = "HTTP"

  default_action {
    type = "forward"
    target_group_arn = aws_lb_target_group.portal-web-app-TG.arn
  }
}