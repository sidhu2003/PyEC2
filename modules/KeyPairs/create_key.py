import boto3

ec2 = boto3.client('ec2')

def create_key_pair(key_name):
    response = ec2.create_key_pair(KeyName=key_name)
    print(response)