import time
import boto3
import os

import load_balancer
from load_balancer import LoadBalancer, ListLoadBalancer, S3ops

os.environ['AWS_DEFAULT_REGION'] = 'us-east-2'
os.environ['AWS_SHARED_CREDENTIALS_FILE'] = '.aws/credentials'

"""boto3.set_stream_logger('botocore', level='DEBUG')"""

"""
Delete Az based on the lb_name , lb_zone
"""
if ListLoadBalancer().load():
    # print("inside job")
    delete_az = LoadBalancer('test-lb-classic', 'na', 'us-east-2a')
    print(delete_az.delete_lb_az())
else:
    print("No AZ available")

# time.sleep(2)
# print(f"Reverting job...")
# time.sleep(2)
#
# # """
# # Reverting back the operation
# # """
#
# if ListLoadBalancer().load():
#     add_az = LoadBalancer('test-lb-classic', 'na', 'us-east-2b')
#     print(add_az.attach_lb_az())
# else:
#     print("Something went wrong")

