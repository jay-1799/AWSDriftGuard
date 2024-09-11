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
elasticbeanstalk_client = boto3.client('elasticbeanstalk')
autoscaling_client = boto3.client('autoscaling')
elasticache_client = boto3.client('elasticache')
secretsmanager_client = boto3.client('secretsmanager')
glue_client = boto3.client('glue')
redshift_client = boto3.client('redshift')
sagemaker_client = boto3.client('sagemaker')
stepfunctions_client = boto3.client('stepfunctions')

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



def get_elastic_beanstalk_environments():
    response = elasticbeanstalk_client.describe_environments()
    environments = []
    for env in response['Environments']:
        environments.append({
            'EnvironmentName': env.get('EnvironmentName'),
            'ApplicationName': env.get('ApplicationName'),
            'EnvironmentId': env.get('EnvironmentId'),
            'Status': env.get('Status'),
        })
    return environments

def get_step_functions():
    response = stepfunctions_client.list_state_machines()
    state_machines = []
    for sm in response['stateMachines']:
        state_machines.append({
            'Name': sm.get('name'),
            'StateMachineArn': sm.get('stateMachineArn'),
            'CreationDate': sm.get('creationDate')
        })
    return state_machines

def get_sagemaker_models():
    response = sagemaker_client.list_models()
    models = []
    for model in response['Models']:
        models.append({
            'ModelName': model.get('ModelName'),
            'CreationTime': model.get('CreationTime'),
            'ModelArn': model.get('ModelArn')
        })
    return models

def get_redshift_clusters():
    response = redshift_client.describe_clusters()
    clusters = []
    for cluster in response['Clusters']:
        clusters.append({
            'ClusterIdentifier': cluster.get('ClusterIdentifier'),
            'NodeType': cluster.get('NodeType'),
            'ClusterStatus': cluster.get('ClusterStatus'),
            'ClusterCreateTime': cluster.get('ClusterCreateTime')
        })
    return clusters

def get_auto_scaling_groups():
    response = autoscaling_client.describe_auto_scaling_groups()
    autoscaling_groups = []
    for group in response['AutoScalingGroups']:
        autoscaling_groups.append({
            'AutoScalingGroupName': group.get('AutoScalingGroupName'),
            'LaunchConfigurationName': group.get('LaunchConfigurationName'),
            'MinSize': group.get('MinSize'),
            'MaxSize': group.get('MaxSize'),
            'DesiredCapacity': group.get('DesiredCapacity')
        })
    return autoscaling_groups

def get_elasticache_clusters():
    response = elasticache_client.describe_cache_clusters()
    clusters = []
    for cluster in response['CacheClusters']:
        clusters.append({
            'CacheClusterId': cluster.get('CacheClusterId'),
            'Engine': cluster.get('Engine'),
            'CacheNodeType': cluster.get('CacheNodeType'),
            'CacheClusterStatus': cluster.get('CacheClusterStatus')
        })
    return clusters

def get_secrets_manager_secrets():
    response = secretsmanager_client.list_secrets()
    secrets = []
    for secret in response['SecretList']:
        secrets.append({
            'Name': secret.get('Name'),
            'SecretArn': secret.get('ARN'),
            'LastChangedDate': secret.get('LastChangedDate')
        })
    return secrets

def get_glue_jobs():
    response = glue_client.get_jobs()
    jobs = []
    for job in response['Jobs']:
        jobs.append({
            'JobName': job.get('Name'),
            'JobArn': job.get('Role'),
            'CreatedOn': job.get('CreatedOn')
        })
    return jobs

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
    print("elastic beanstalk environments:", get_elastic_beanstalk_environments())
    print("step functions:", get_step_functions())
    print("glue jobs:", get_glue_jobs())
    print("secrets:", get_secrets_manager_secrets())
    print("elastic cache clusters:", get_elasticache_clusters())
    print("redshift clusters:", get_redshift_clusters())
    print("auto scaling groups:", get_auto_scaling_groups())
    print("sagemaker models:", get_sagemaker_models())

