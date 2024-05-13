import boto3 as bt

ec2 = bt.resource('ec2')

def create_instance(ami_id, min_count, max_count, instance_type, key_name):
    instances = ec2.create_instances(
        ImageId=ami_id, 
        MinCount=min_count,
        MaxCount=max_count,
        InstanceType=instance_type,  
        KeyName=key_name 
    )

    print("instances are launched successfully")