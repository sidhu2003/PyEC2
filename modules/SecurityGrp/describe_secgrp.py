import boto3 as bt

client = bt.client('ec2')

def describe_security_group(group_id):
    response = client.describe_security_groups(
    GroupIds=[
        group_id,
    ],
)
    print(response)