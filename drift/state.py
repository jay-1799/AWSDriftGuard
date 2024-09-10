import json

def load_state_file(state_file_path):
    """Load the Terraform state file from the specified path."""
    with open(state_file_path, 'r') as file:
        state_data = json.load(file)
    return state_data

def parse_resources(state_data):
    """Parse resources from the Terraform state data."""
    resources = state_data.get('resources', [])
    parsed_resources = []
    for resource in resources:
        resource_type = resource.get('type')
        resource_name = resource.get('name')
        resource_id = resource.get('instances', [{}])[0].get('attributes', {}).get('id', 'N/A')
        parsed_resources.append({
            'Type': resource_type,
            'Name': resource_name,
            'ID': resource_id,
        })
    return parsed_resources

def get_resource_by_type(resources, resource_type):
    """Filter resources by type."""
    return [resource for resource in resources if resource['Type'] == resource_type]

if __name__ == "__main__":
    # Example usage
    state_file_path = 'terraform.tfstate'
    state_data = load_state_file(state_file_path)
    parsed_resources = parse_resources(state_data)
    
    print("All Resources:", parsed_resources)
    
    # Example of filtering resources by type
    ec2_instances = get_resource_by_type(parsed_resources, 'aws_instance')
    print("EC2 Instances:", ec2_instances)
