Automating EC2 Start/Stop with AWS Lambda
Project Overview

This project automates the start and stop of EC2 instances on a schedule using AWS Lambda, CloudWatch Events, IAM, and SNS.

⏰ Start EC2 at 10:00 AM IST

⏰ Stop EC2 at 7:00 PM IST

📩 Send email/SNS notifications for actions taken.

This helps reduce costs by running instances only during working hours.

<img width="1024" height="1024" alt="architecture" src="https://github.com/user-attachments/assets/a2834114-f560-42d7-a8c6-36b698bb9d4d" />

⚙️ How It Works

Lambda Functions: Two functions (lambda_start.py and lambda_stop.py) to start/stop EC2 instances.

CloudWatch Event Rules: Cron expressions to trigger Lambda at 10 AM (start) and 7 PM (stop).

IAM Role & Policy: Custom policy with permissions for EC2 and SNS.

SNS Notification: Sends email notification whenever EC2 is started/stopped.

📂 Repository Contents

lambda_start.py → Lambda function to start EC2 instances.

lambda_stop.py → Lambda function to stop EC2 instances.

iam-policy.json → IAM policy with required permissions.

cron-expressions.txt → CloudWatch schedule expressions.

architecture.png → Project architecture diagram.

⏳ Cron Expressions Used
# Start EC2 at 10 AM IST (4:30 UTC)
cron(30 4 * * ? *)

# Stop EC2 at 7 PM IST (13:30 UTC)
cron(30 13 * * ? *)

✅ IAM Policy Example
{
  "Effect": "Allow",
  "Action": [
    "ec2:StartInstances",
    "ec2:StopInstances",
    "ec2:DescribeInstances",
    "sns:Publish"
  ],
  "Resource": "*"
}

Key AWS Services Used

AWS Lambda → Automation logic

Amazon CloudWatch → Scheduling with cron

Amazon SNS → Notifications

Amazon EC2 → Target instances

IAM → Access control
 
Use Case

Automatically manage EC2 running hours.

Save AWS costs.

Ensure EC2 is only active during working hours.
