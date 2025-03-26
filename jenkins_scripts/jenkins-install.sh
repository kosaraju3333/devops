#!/bin/bash

#################################################
						#
#This script will install JAVA and JENKINS 	#
						#
#################################################

set -x
set -e

sudo apt update -y

# Instaling JRE 17:
sudo apt install fontconfig openjdk-17-jre

# Instaling JRE from OpenJDK 11:
#sudo apt install default-jre -y

# Instaling the JDK
#sudo apt install default-jdk -y

sudo wget -O /usr/share/keyrings/jenkins-keyring.asc \
  https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null

# run apt update so that apt will use the new repository
sudo apt update -y

# install Jenkins and its dependencies
sudo apt install jenkins -y

# enable the Jenkins service to start at boot with the command
sudo systemctl enable jenkins

# Starting Jenkins 
sudo systemctl start jenkins


