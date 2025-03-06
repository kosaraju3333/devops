variable "vpc-cidr-block" {
    description = "CIDR Block for VPC"
}

variable "vpc-name" {
    description = "Name of VPC"
}

variable "owner" {
    description = "Owner for this resource" 
}

variable "public-subnet-1-cidir" {
    description = "CIDR block for public-subnet-1"
}  

variable "public-subnet-1-name" {
    description = "Name of public-subnet-1"
}

variable "public-subnet-2-cidir" {
    description = "CIDR block for public-subnet-2"
}

variable "public-subnet-2-name" {
    description = "Name of public-subnet-2"
}

variable "private-subnet-1-cidir" {
    description = "CIDR block for private-subnet-1"
}

variable "private-subnet-1-name" {
    description = "Name of private-subnet-1"
}

variable "private-subnet-2-cidir" {
    description = "CIDR block for private-subnet-2"
}

variable "private-subnet-2-name" {
    description = "Name of private-subnet-2"
}

variable "availability-zone-1" {
    description = "AZ 1 for Portal VPC"
}

variable "availability-zone-2" {
    description = "AZ 2 for Portal VPC"
}

variable "portal-vpc-igw-name" {
    description = "Name of portal-vpc IGW"
}

variable "portal-vpc-public-main-RT-name" {
    description = "Name of portal-vpc-public Main RT"
}

variable "portal-vpc-private-main-RT-name" {
    description = "Name of portal-vpc-private RT"
}

variable "elastic-ip-NAT-name" {
    description = "Elastic ip for NAT Gatway"
}

variable "portal-vpc-NAT-gateway-name" {
    description = "Name of Portal-vpc-NAT"
}