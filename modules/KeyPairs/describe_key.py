import boto3 as bt

ec2 = bt.resource('ec2')

def describe_key_pair(key_name):
    response = ec2.describe_key_pairs(KeyNames=[key_name])
    print(response)