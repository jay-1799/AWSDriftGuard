import requests
import json
import os
from detector import get_drift_data

# Slack webhook URL (replace with your own URL)
# SLACK_WEBHOOK_URL = ""

def format_drift_report(drift_data):
    
    message = ""
    for resource_type, details in drift_data.items():
        message += f"*{resource_type}*\n"
        if details['only_in_aws']:
            message += f"_Only in AWS_: {', '.join(details['only_in_aws'])}\n"
        if details['only_in_state']:
            message += f"_Only in State File_: {', '.join(details['only_in_state'])}\n"
        if details['differences']:
            message += f"_Differences in Common Resources_: {json.dumps(details['differences'], indent=2)}\n"
        message += "_______________________________________________________\n"
    return message

def send_to_slack(message,SLACK_WEBHOOK_URL):
    slack_data = {
        "text": message
    }

    response = requests.post(
        SLACK_WEBHOOK_URL, data=json.dumps(slack_data),
        headers={'Content-Type': 'application/json'}
    )

    if response.status_code != 200:
        raise ValueError(f"Request to Slack returned an error {response.status_code}, the response is:\n{response.text}")

if __name__ == "__main__":
    
    drift_data = get_drift_data()

    drift_report_message = format_drift_report(drift_data)
    slack_webhook_url = os.getenv("SLACK_WEBHOOK_URL", None)
    if not slack_webhook_url:
        raise ValueError("Slack webhook URL is not provided.")
    
    send_to_slack(drift_report_message)  