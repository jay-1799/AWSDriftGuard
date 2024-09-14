from aws import get_aws_resources
from state import get_state_file_resources

def compare_resources(aws_resources, state_file_resources, resource_type):
    aws_resource_ids = set(aws_resources[resource_type].keys())
    state_resource_ids = set(state_file_resources[resource_type].keys())

    only_in_aws = aws_resource_ids - state_resource_ids
    only_in_state = state_resource_ids - aws_resource_ids
    common_resources = aws_resource_ids & state_resource_ids

    differences = {}
    for resource_id in common_resources:
        aws_resource = aws_resources[resource_type][resource_id]
        state_resource = state_file_resources[resource_type][resource_id]
        # Comparing each field and storing differences
        if aws_resource != state_resource:
            differences[resource_id] = {'AWS': aws_resource, 'StateFile': state_resource}

    return only_in_aws, only_in_state, differences

aws_resources=get_aws_resources()
state_file_resources = get_state_file_resources()
only_in_aws, only_in_state, differences = compare_resources(aws_resources, state_file_resources, 'aws_instance')
print("Only in AWS:", only_in_aws)
print("Only in State File:", only_in_state)
print("Differences in Common Resources:", differences)
 