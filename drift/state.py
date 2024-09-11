import os
import json
from collections import defaultdict

def load_state_file(state_file_path):
    with open(state_file_path, 'r') as file:
        state_data = json.load(file)
    return state_data

def parse_resources(state_data):
    resources = state_data.get('resources', [])
    parsed_resources = defaultdict(set)  # Using defaultdict with sets to group by resource type
    
    for resource in resources:
        resource_type = resource.get('type')
        resource_name = resource.get('name')
        resource_id = resource.get('instances', [{}])[0].get('attributes', {}).get('id', 'N/A')
        
        if resource_type and resource_id != 'N/A':
            parsed_resources[resource_type].add(resource_id)
    
    return parsed_resources

def merge_parsed_resources(all_parsed_resources, parsed_resources):
    for resource_type, ids in parsed_resources.items():
        all_parsed_resources[resource_type].update(ids)  # Merge sets to ensure unique IDs

def parse_all_state_files(directory_path):
    all_parsed_resources = defaultdict(set)  # Main dictionary to store all resources grouped by type
    
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.tfstate'):
                state_file_path = os.path.join(root, file)
                print(f"Parsing file: {state_file_path}")
                try:
                    state_data = load_state_file(state_file_path)
                    parsed_resources = parse_resources(state_data)
                    merge_parsed_resources(all_parsed_resources, parsed_resources)
                except Exception as e:
                    print(f"Error parsing {state_file_path}: {e}")
    
    return all_parsed_resources

if __name__ == "__main__":
    # Directory path containing Terraform state files
    directory_path = 'C:/Users/Jay Patel/Downloads/state files'
    
    # Parse all state files in the directory
    all_resources = parse_all_state_files(directory_path)
    
    print("All Resources Grouped by Type:")
    for resource_type, ids in all_resources.items():
        print(f"{resource_type}: {ids}")
