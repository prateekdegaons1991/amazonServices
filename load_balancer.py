import boto3


class S3ops:
    def __init__(self):
        self.s3 = 's3'

    def list_s3(self):
        s3 = boto3.resource(self.s3)
        client = boto3.client(self.s3)
        buckets = client.list_buckets()
        response = s3.buckets.all()
        for item in buckets["Buckets"]:
            return item

    def delet_s3(self):
        s3 = boto3.client(self.s3)
        for item in self.list_s3():
            response = s3.delete_bucket(
                Bucket=item
            )
        print(response)


class ListLoadBalancer:
    def __init__(self):
        self.elb = 'elb'

    def load(self) -> str:
        elb = boto3.client(self.elb)
        return elb.describe_load_balancers()['LoadBalancerDescriptions']


class LoadBalancer:
    def __init__(self, lb_name, lb_arn, lb_zone):
        self.lb_name = lb_name
        self.lb_arn = lb_arn
        self.lb_zone = lb_zone
        self.elb = 'elb'     # Mention This is for traditional load balancer
        self.elbv2 = 'elbv2'  # Mention This is for the modern load balancer

    def delete_lb_az(self):
        client = boto3.client(self.elb)
        try:
            response = client.disable_availability_zones_for_load_balancer(
                LoadBalancerName=self.lb_name,
                AvailabilityZones=[
                    self.lb_zone,
                ]
            )
            return response

        except (client.exceptions.AccessPointNotFoundException, client.exceptions.InvalidConfigurationRequestException) as e:
            return e

    def attach_lb_az(self):
        client = boto3.client(self.elb)
        try:
            response = client.enable_availability_zones_for_load_balancer(
                LoadBalancerName=self.lb_name,
                AvailabilityZones=[
                    self.lb_zone,
                ]
            )
            return response
        except (client.exceptions.AccessPointNotFoundException, client.exceptions.InvalidConfigurationRequestException) as e:
            return e
