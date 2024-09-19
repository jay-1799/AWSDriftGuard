# AWS Drift Detection CLI Tool

## Overview

This CLI tool helps detect and report drift in AWS resources by comparing the current state of resources with those defined in Terraform state files. The tool supports a comprehensive list of AWS services and can send drift reports to Slack for easy monitoring.

## Features

- Detects drift between AWS resources and Terraform state.
- Groups resources by types such as EC2, S3, RDS, IAM Roles, and VPCs.
- Option to send the drift report to a Slack channel.
- Simple command-line interface (CLI) for easy use.

## Supported Services

The CLI tool supports the following AWS services:

- **EC2 Instances**
- **S3 Buckets**
- **RDS Instances**
- **IAM Roles**
- **Auto Scaling Groups**
- **VPCs**
- **Lambda Functions**
- **DynamoDB Tables**
- **Load Balancers**
- **EBS Volumes**
- **Elastic IPs**
- **ECR Repositories**
- **CloudFront Distributions**
- **EFS Filesystems**
- **SNS Topics**
- **SQS Queues**
- **Elastic Beanstalk Environments**
- **Step Functions**
- **Glue Jobs**
- **Secrets Manager Secrets**
- **ElastiCache Clusters**
- **Redshift Clusters**
- **SageMaker Models**
- **Kinesis Streams**
- **CodePipeline Pipelines**
- **CodeBuild Projects**
- **CodeDeploy Applications**
- **MQ Brokers**
- **Workspaces**

## Usage

### Command Line Arguments:

- **`--state`**: (Required) Path to the directory containing Terraform state files.
- **`--webhook`**: (Optional) Slack webhook URL to send the drift report.
- **`action`**: (Required) The action to perform, either:
  - **`detect`**: To run the drift detection and output the results in the console.
  - **`report`**: To send the drift report to Slack (requires `--webhook`).

## Arguments

### Required Arguments:

- **`--state`**: Path to the directory containing Terraform state files.

### Optional Arguments:

- **`--webhook`**: Slack webhook URL for sending the drift report to a Slack channel.

### Positional Arguments:

- **`action`**:
  - **`detect`**: Detect drift and print the report.
  - **`report`**: Send the drift report to a Slack channel (requires `--webhook` argument).

## Detecting Drift in Terraform State:

```bash
python cli.py --state /path/to/state/files detect
```

## Sending drift report to slack:

```bash
python cli.py --state /path/to/state/files --webhook https://hooks.slack.com/services/your-webhook-url report

```
