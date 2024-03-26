# Port Scanner Python Script

## Overview
This Python script is designed to perform a port scan on a specified target host IP address within a given range of ports. It uses TCP connections to check for open ports and reports back the open ports found during the scan.

## Requirements
- Python 3.x
- Standard library modules: `socket`

## Usage
1. Clone or download the repository containing the script.
2. Navigate to the directory containing the script in your terminal or command prompt.

### Running the Script
To run the script, execute the following command:
```bash
python port_scanner.py

### Input
- **Target Host IP Address:** Enter the IP address of the target host. For example: `192.168.1.1`.
- **Port Range:** Enter the maximum port number to scan. The script will scan ports from 1 to the specified maximum port number.

### Output
The script will display a message for each open port found during the scan, indicating that the port is open.

'''bash
Input target host IP address. Example: 10.0.12.123
192.168.1.1
How many ports do you want to be scanned? Enter a number from 1 to 65,535.
100
Port 80 is open
Port 443 is open

Port Scanning is Complete.


## Notes
- This script uses TCP connections to determine open ports. It may not accurately detect UDP or stealthily closed ports.
- For comprehensive network scanning or more advanced features, consider using specialized tools such as Nmap.
