# import json
# import csv

# def generate_text_report(drift_report):
#     """Generates a plain text report from the drift detection results."""
#     report_lines = []
#     for item in drift_report:
#         report_lines.append(f"Resource ID: {item['ID']}, Type: {item['Type']}, Status: {item['Status']}")
#     return "\n".join(report_lines)

# def generate_json_report(drift_report):
#     """Generates a JSON report from the drift detection results."""
#     return json.dumps(drift_report, indent=4)

# def generate_csv_report(drift_report):
#     """Generates a CSV report from the drift detection results."""
#     output = []
#     writer = csv.writer(output)
#     writer.writerow(['Resource ID', 'Type', 'Status'])
    
#     for item in drift_report:
#         writer.writerow([item['ID'], item['Type'], item['Status']])
    
#     return '\n'.join(output)

# def save_report(report_content, file_path, format_type):
#     """Saves the generated report content to a file."""
#     with open(file_path, 'w') as file:
#         file.write(report_content)
#     print(f"Report saved to {file_path}.")

# def print_report(report_content):
#     """Prints the report content to the console."""
#     print(report_content)

# # Example usage
# if __name__ == "__main__":
#     sample_drift_report = [
#         {'ID': 'i-1234567890abcdef0', 'Type': 'aws_instance', 'Status': 'Drift detected'},
#         {'ID': 'bucket-name', 'Type': 'aws_s3_bucket', 'Status': 'Missing in AWS'},
#         {'ID': 'db-instance-id', 'Type': 'aws_rds_instance', 'Status': 'Extra in AWS'}
#     ]
    
#     # Generate and display reports
#     text_report = generate_text_report(sample_drift_report)
#     print_report(text_report)
    
#     json_report = generate_json_report(sample_drift_report)
#     save_report(json_report, 'drift_report.json', 'json')
    
#     csv_report = generate_csv_report(sample_drift_report)
#     save_report(csv_report, 'drift_report.csv', 'csv')
