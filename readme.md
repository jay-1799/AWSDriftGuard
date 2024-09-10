awsdriftguard/
│
├── drift/ # Main package directory
│ ├── **init**.py # Package initialization file
│ ├── cli.py # CLI command definitions
│ ├── aws.py # Functions for interacting with AWS
│ ├── state.py # Functions for parsing Terraform state
│ ├── detector.py # Drift detection logic
│ ├── reporter.py # Reporting and output generation
│ └── utils.py # Utility functions and helpers
│
├── tests/ # Directory for test cases
│ ├── **init**.py # Package initialization file
│ ├── test_aws.py # Tests for AWS resource functions
│ ├── test_state.py # Tests for Terraform state parsing
│ ├── test_detector.py # Tests for drift detection logic
│ └── test_reporter.py # Tests for reporting functions
│
├── .gitignore # Git ignore file
├── requirements.txt # Python package dependencies
├── setup.py # Setup script for packaging
├── README.md # Project description and usage
└── LICENSE # License information

1. Get an active account list for the organisation
2. For each account, retrieve the state file locations
3. Assume the role in each account, and perform a DriftCtl scan
4. Convert the scan output into an event and forward on for storage and analytics
