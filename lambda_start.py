import boto3
import os

# AWS Clients
ec2 = boto3.client('ec2')
sns = boto3.client('sns')

# Environment Variables (set in Lambda)
TAG_KEY = os.environ.get("TAG_KEY", "AutoStartStop")
TAG_VALUE = os.environ.get("TAG_VALUE", "true")
SNS_TOPIC_ARN = os.environ.get("SNS_TOPIC_ARN", "")

def lambda_handler(event, context):
    # Get EC2 instances by tag
    instances = ec2.describe_instances(
        Filters=[{'Name': f'tag:{TAG_KEY}', 'Values': [TAG_VALUE]}]
    )
    ids = [
        i["InstanceId"]
        for r in instances["Reservations"]
        for i in r["Instances"]
    ]

    if not ids:
        msg = "⚠️ No matching instances found to start."
        print(msg)
        return {"statusCode": 200, "body": msg}

    # Start instances
    ec2.start_instances(InstanceIds=ids)
    message = f"✅ Started instances: {ids}"
    print(message)

    # Send SNS notification if configured
    if SNS_TOPIC_ARN:
        sns.publish(TopicArn=SNS_TOPIC_ARN, Message=message)

    return {"statusCode": 200, "body": message}

