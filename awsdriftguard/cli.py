import argparse
from detector import get_drift_data
from reporter import format_drift_report, send_to_slack


def run_drift_detection(state_directory):
    drift_data = get_drift_data(state_directory)
    drift_report = format_drift_report(drift_data)
    
    print("Drift detection completed:")
    print(drift_report)
    return drift_report


def send_report_to_slack(state_directory, slack_webhook_url):
    drift_report = run_drift_detection(state_directory)
    
    send_to_slack(drift_report, slack_webhook_url)
    print("Drift report sent to Slack!")


def main():
    parser = argparse.ArgumentParser(description="AWS Terraform Drift Detection Tool")
    
    parser.add_argument(
        '--state', 
        type=str, 
        required=True, 
        help="Path to the directory containing Terraform state files"
    )
    
    parser.add_argument(
        '--webhook', 
        type=str, 
        help="Slack webhook URL for sending the drift report"
    )

    parser.add_argument(
        'action', 
        choices=['detect', 'report'],
        help="The action to perform: 'detect' to run drift detection, 'report' to send the report to Slack"
    )
    
    args = parser.parse_args()

    if args.action == 'detect':
        run_drift_detection(args.state)
    elif args.action == 'report':
        if not args.webhook:
            raise ValueError("The --webhook argument is required when using the 'report' action.")
        send_report_to_slack(args.state, args.webhook)


if __name__ == "__main__":
    main()

