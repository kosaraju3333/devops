#!/bin/bash

#################################################################
                                                                #
#This Script will restore the Jenkins from Jenkins backup file  #
                                                                #
#################################################################

set -x
set -e

if [ "$#" -ne 1 ]
then
   echo "Pass ONE argumet to script that is JENKINS BACKUP FILE NAME"
   exit
fi

jenkins_backup_file=$1

## Check if JENKINS status
jenkins_status=$(sudo service jenkins status | awk -F ' ' '/Active/ {print $2}')

if [ $jenkins_status == active ]
then
   echo "Print Jenkins is runing"
   echo "Stopping jenkins"
   sudo service jenkins stop
   if [ $? -eq 0 ]
   then
      echo "Jenkins Stopped"
   else
      echo "Jenkins NOT Stopped"
      exit
   fi
else
   echo "Jenkins already stopped"
fi

# Downloading JENKISN backup file from AWS S3
aws s3 cp s3://jenkins-spontansolutions/jenkins-backups/$jenkins_backup_file .

# Deleting /var/lib/jenkins
sudo rm -rf /var/lib/jenkins

# untar the download jenkins file
sudo tar -zxvf $jenkins_backup_file -C /

# Starting Jenkins
sudo service jenkins start

if [ $? -eq 0 ]
then
   echo "Jenkins Started"
else
   echo "Jenkins NOT Started"
   echo "Please start Jenkins Manually"
fi
