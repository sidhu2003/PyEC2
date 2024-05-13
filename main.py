from  modules.EC2.ec2_create import *
from  modules.EC2.ec2_describe import *
from  modules.EC2.ec2_stop import *

from modules.KeyPairs.create_key import *
from modules.KeyPairs.delete_key import *
from modules.KeyPairs.describe_key import *

from modules.SecurityGrp.create_secgrp import *
from modules.SecurityGrp.delete_secgrp import *
from modules.SecurityGrp.describe_secgrp import *

import os , sys

print("Welcome to EC2 AWS Automation")

ascii_art = r"""
$$$$$$$\                  $$$$$$$$\  $$$$$$\   $$$$$$\  
$$  __$$\                 $$  _____|$$  __$$\ $$  __$$\ 
$$ |  $$ |$$\   $$\       $$ |      $$ /  \__|\__/  $$ |
$$$$$$$  |$$ |  $$ |      $$$$$\    $$ |       $$$$$$  |
$$  ____/ $$ |  $$ |      $$  __|   $$ |      $$  ____/ 
$$ |      $$ |  $$ |      $$ |      $$ |  $$\ $$ |      
$$ |      \$$$$$$$ |      $$$$$$$$\ \$$$$$$  |$$$$$$$$\ 
\__|       \____$$ |      \________| \______/ \________|
          $$\   $$ |                                    
          \$$$$$$  |                                    
           \______/                                     
              
    """
print(ascii_art)

print("1. Create EC2 Instance")
print("2. Describe EC2 Instances")
print("3. Stop EC2 Instance")
print("4. Create Key Pair")
print("5. Describe Key Pair")
print("6. Delete Key Pair")
print("7. Create Security Group")
print("8. Describe Security Group")
print("9. Delete Security Group")
print("10. Exit")

while True:
    print("Enter your choice: ", end="")
    ch = int(input())

    if ch == 1:
        ami_id = input("Enter AMI ID: ")
        min_count = int(input("Enter Min Count: "))
        max_count = int(input("Enter Max Count: "))
        instance_type = input("Enter Instance Type: ")
        key_name = input("Enter Key Name: ")
        create_instance(ami_id, min_count, max_count, instance_type, key_name)
    elif ch == 2:
        instance_id = input("Enter Instance ID: ")
        describe_instance(instance_id)
    elif ch == 3:
        instance_id = input("Enter Instance ID: ")
        stop_instance(instance_id)
    elif ch == 4:
        key_name = input("Enter Key Name: ")
        create_key_pair(key_name)
    elif ch == 5:
        key_name = input("Enter Key Name: ")
        describe_key_pair(key_name)
    elif ch == 6:
        key_name = input("Enter Key Name: ")
        delete_key_pair(key_name)
    elif ch == 7:
        vpc_id = input("Enter VPC ID: ")
        group_name = input("Enter Group Name: ")
        group_desc = input("Enter Group Description: ")
        create_security_group(vpc_id, group_name, group_desc)
    elif ch == 8:
        group_id = input("Enter Group ID: ")
        describe_security_group(group_id)
    elif ch == 9:
        group_id = input("Enter Group ID: ")
        group_name = input("Enter Group Name: ")
        delete_security_group(group_id, group_name)
    elif ch == 10:
        print("Exiting...")
        sys.exit(0)
    else:
        print("Invalid Choice")

