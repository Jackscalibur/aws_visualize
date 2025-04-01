import boto3


def get_ec2_client(region_name: str):
    """
    Create an EC2 client for the specified region.
    """
    return boto3.client('ec2', region_name=region_name)

def get_ec2_instances(ec2_client):
    """
    Retrieve a list of EC2 instances and their details.
    """
    instances = []
    try:
        response = ec2_client.describe_instances()
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instances.append({
                    'InstanceId': instance['InstanceId'],
                    'InstanceType': instance['InstanceType'],
                    'State': instance['State']['Name'],
                    'LaunchTime': instance['LaunchTime'].strftime("%Y-%m-%d %H:%M:%S"),
                    'PublicIpAddress': instance.get('PublicIpAddress', 'N/A'),
                    'PrivateIpAddress': instance.get('PrivateIpAddress', 'N/A')
                })
    except Exception as e:
        print(f"Error retrieving EC2 instances: {e}")
    return instances

def get_ec2_volumes(ec2_client):
    """
    Retrieve a list of EC2 volumes and their details.
    """
    volumes = []
    try:
        response = ec2_client.describe_volumes()
        for volume in response['Volumes']:
            volumes.append({
                'VolumeId': volume['VolumeId'],
                'Size': volume['Size'],
                'State': volume['State'],
                'CreateTime': volume['CreateTime'].strftime("%Y-%m-%d %H:%M:%S"),
                'Attachments': volume.get('Attachments', [])
            })
    except Exception as e:
        print(f"Error retrieving EC2 volumes: {e}")
    return volumes

def get_ec2_security_groups(ec2_client):
    """
    Retrieve a list of EC2 security groups and their details.
    """
    security_groups = []
    try:
        response = ec2_client.describe_security_groups()
        for group in response['SecurityGroups']:
            security_groups.append({
                'GroupId': group['GroupId'],
                'GroupName': group['GroupName'],
                'Description': group['Description'],
                'VpcId': group.get('VpcId', 'N/A'),
                'IpPermissions': group.get('IpPermissions', [])
            })
    except Exception as e:
        print(f"Error retrieving EC2 security groups: {e}")
    return security_groups
