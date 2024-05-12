import boto3 as bt

ec2 = bt.resource('ec2')

def delete_key_pair(key_name):
    response = ec2.delete_key_pair(KeyName=key_name)
    print(response)