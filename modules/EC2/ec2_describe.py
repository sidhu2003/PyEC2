import boto3 as bt

client = bt.client('ec2')

def describe_instance(instance_id):
    response = client.describe_instances(
    InstanceIds=[
        instance_id,
    ],
)

    print(response)