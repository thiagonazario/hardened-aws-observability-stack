import pulumi
import pulumi_aws as aws

class HardenedNetwork:
    def __init__(self, name: str):
        # VPC with DNS and Hostnames
        self.vpc = aws.ec2.Vpc(f"{name}-vpc",
            cidr_block="10.0.0.0/16",
            enable_dns_hostnames=True,
            enable_dns_support=True,
            tags={"Name": f"{name}-hardened-vpc", "Security": "High"})

        # Private Subnet
        self.private_subnet = aws.ec2.Subnet(f"{name}-private-subnet",
            vpc_id=self.vpc.id,
            cidr_block="10.0.1.0/24",
            map_public_ip_on_launch=False, # Zero Trust Rule
            tags={"Name": f"{name}-private-obs"})