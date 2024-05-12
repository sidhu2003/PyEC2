import boto3 as bt

ec2 = bt.resource('ec2')

def delete_security_group(group_id, group_name):
    response = ec2.delete_security_group(
    GroupId=group_id,
    GroupName=group_name,
)