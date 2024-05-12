import boto3 as bt

client = bt.client('ec2')

def stop_instance(instance_id):
    response = client.stop_instances(
        InstanceIds=[
            instance_id,
        ],
    )
    print(response)
