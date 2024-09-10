def detect_drift(aws_resources, terraform_resources):
    """Detects drift between AWS resources and Terraform state resources."""
    drift_report = []
    
    # Convert lists to dictionaries for easier comparison
    aws_resources_map = {resource['ID']: resource for resource in aws_resources}
    terraform_resources_map = {resource['ID']: resource for resource in terraform_resources}
    
    # Check for drift
    for resource_id, terraform_resource in terraform_resources_map.items():
        if resource_id not in aws_resources_map:
            drift_report.append({
                'ID': resource_id,
                'Type': terraform_resource['Type'],
                'Status': 'Missing in AWS'
            })
        else:
            aws_resource = aws_resources_map[resource_id]
            if not is_resource_matching(aws_resource, terraform_resource):
                drift_report.append({
                    'ID': resource_id,
                    'Type': terraform_resource['Type'],
                    'Status': 'Drift detected'
                })
    
    # Check for AWS resources not in Terraform state
    for resource_id in aws_resources_map:
        if resource_id not in terraform_resources_map:
            drift_report.append({
                'ID': resource_id,
                'Type': aws_resources_map[resource_id]['Type'],
                'Status': 'Extra in AWS'
            })
    
    return format_drift_report(drift_report)

def is_resource_matching(aws_resource, terraform_resource):
    """Compares if an AWS resource matches the Terraform resource."""
    # Here we assume a basic comparison. Adjust according to your needs.
    return aws_resource.get('Type') == terraform_resource.get('Type') and \
           aws_resource.get('Name') == terraform_resource.get('Name')

def format_drift_report(drift_report):
    """Formats the drift report for easier readability."""
    report_lines = []
    for item in drift_report:
        report_lines.append(f"Resource ID: {item['ID']}, Type: {item['Type']}, Status: {item['Status']}")
    return "\n".join(report_lines)
