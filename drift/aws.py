import boto3

ec2_client = boto3.client('ec2')
s3_client = boto3.client('s3')
rds_client = boto3.client('rds')
iam_client = boto3.client('iam')
lambda_client = boto3.client('lambda')
cloudformation_client = boto3.client('cloudformation')
dynamodb_client = boto3.client('dynamodb')
elb_client = boto3.client('elbv2')
ecr_client = boto3.client('ecr')
cloudfront_client = boto3.client('cloudfront')
efs_client = boto3.client('efs')
sns_client = boto3.client('sns')
sqs_client = boto3.client('sqs')

def get_ec2_instances():
    response = ec2_client.describe_instances()
    instances = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append({
                'InstanceId': instance.get('InstanceId'),
                'InstanceType': instance.get('InstanceType'),
                'State': instance['State'].get('Name'),
                'Tags': {tag['Key']: tag['Value'] for tag in instance.get('Tags', [])}
            })
    return instances

def get_s3_buckets():
    response = s3_client.list_buckets()
    buckets = [{'BucketName': bucket['Name']} for bucket in response['Buckets']]
    return buckets

def get_rds_instances():
    response = rds_client.describe_db_instances()
    instances = []
    for instance in response['DBInstances']:
        instances.append({
            'DBInstanceIdentifier': instance.get('DBInstanceIdentifier'),
            'DBInstanceArn': instance.get('DBInstanceArn'),
            'DBInstanceClass': instance.get('DBInstanceClass'),
            'Engine': instance.get('Engine'),
            'Status': instance.get('DBInstanceStatus')
        })
    return instances

def get_iam_roles():
    response = iam_client.list_roles()
    roles = [{'RoleName': role['RoleName'], 'RoleArn': role['Arn']} for role in response['Roles']]
    return roles

def get_vpcs():
    response = ec2_client.describe_vpcs()
    vpcs = [{'VpcId': vpc['VpcId'], 'CidrBlock': vpc['CidrBlock']} for vpc in response['Vpcs']]
    return vpcs

def get_lambda_functions():
    response = lambda_client.list_functions()
    functions = [{'functionName': function['FunctionName'],'Runtime':function['Runtime'],'Function ARN':function['FunctionArn']} for function in response['Functions']]
    return functions

def get_cloudformation_stacks():
    response = cloudformation_client.describe_stacks()
    stacks = [{'StackName': stack['StackName'], 'StackId': stack['StackId'], 'StackStatus': stack['StackStatus']} for stack in response['Stacks']]
    return stacks

def get_dynamodb_tables():
    response = dynamodb_client.list_tables()
    tables = [{
        'TableName': table,
        'TableArn': f'arn:aws:dynamodb:REGION:ACCOUNT_ID:table/{table}'  # Replace REGION and ACCOUNT_ID
    } for table in response['TableNames']]
    return tables
def get_load_balancers():
    response = elb_client.describe_load_balancers()
    load_balancers = [{
        'LoadBalancerName': lb['LoadBalancerName'],  # Name
        'LoadBalancerArn': lb['LoadBalancerArn'],  # ARN
        'DNSName': lb['DNSName']
    } for lb in response['LoadBalancers']]
    return load_balancers

def get_ebs_volumes():
    response = ec2_client.describe_volumes()
    volumes = [{
        'VolumeId': volume['VolumeId'],  # Unique ID
        'Size': volume['Size'],
        'State': volume['State']
    } for volume in response['Volumes']]
    return volumes
def get_elastic_ips():
    response = ec2_client.describe_addresses()
    eips = [{
        'PublicIp': address.get('PublicIp'),
        'AllocationId': address.get('AllocationId'),
        'AssociationId': address.get('AssociationId')
    } for address in response['Addresses']]
    return eips
def get_ecr_repositories():
    
    response = ecr_client.describe_repositories()
    repositories = [{
        'RepositoryName': repo['repositoryName'],
        'RepositoryArn': repo['repositoryArn'],
        'CreatedAt': repo['createdAt']
    } for repo in response['repositories']]
    return repositories
def get_cloudfront_distributions():
    
    response = cloudfront_client.list_distributions()
    distributions = []
    if 'DistributionList' in response:
        for dist in response['DistributionList']['Items']:
            distributions.append({
                'Id': dist['Id'],
                'ARN': dist['ARN'],
                'Status': dist['Status'],
                'DomainName': dist['DomainName'],
                'LastModifiedTime': dist['LastModifiedTime'].strftime('%Y-%m-%dT%H:%M:%S')
            })
    return distributions
def get_efs_filesystems():
    
    response = efs_client.describe_file_systems()
    filesystems = [{
        'FileSystemId': fs['FileSystemId'],
        'CreationToken': fs['CreationToken'],
        'SizeInBytes': fs['SizeInBytes']['Value'],
        'CreationTime': fs['CreationTime'].strftime('%Y-%m-%dT%H:%M:%S')
    } for fs in response['FileSystems']]
    return filesystems
def get_sns_topics():
    
    response = sns_client.list_topics()
    topics = [{'TopicArn': topic['TopicArn']} for topic in response['Topics']]
    return topics
def get_sqs_queues():
    
    response = sqs_client.list_queues()
    queues = [{'QueueUrl': queue_url} for queue_url in response.get('QueueUrls', [])]
    return queues







if __name__ == "__main__":
    
    print("EC2 Instances:", get_ec2_instances())
    print("S3 Buckets:", get_s3_buckets())
    print("RDS Instances:", get_rds_instances())
    print("IAM Roles:", get_iam_roles())
    print("VPCs:", get_vpcs())
    print("Lambda Functions:",get_lambda_functions())
    print("dynamodb tables:",get_dynamodb_tables())
    print("load balancers:",get_load_balancers())
    print("ebs volumes:",get_ebs_volumes())
    print("Elastic IPs:", get_elastic_ips())
    print("ECR Repositories:", get_ecr_repositories())
    print("Cloudfront Distributions:", get_cloudfront_distributions())
    print("efs filesystems:", get_efs_filesystems())
    print("SNS Topics:", get_sns_topics())
    print("SQS Queues:", get_sqs_queues())

