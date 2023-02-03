# Network Scanner
A Python script to perform network scanning similar to Nmap and display the port number and service name running on that port. This script is designed to be faster with basic multithreading.

## Usage
```bash
python network_scanner.py <hostname or IP> <start port no> <ending port>
```
## Requirements
Python 3
  
## Features
Perform network scanning on a host or IP
Display port number and service name running on that port
Basic multithreading for improved speed
  
## Example Output
```bash
+--------------------+
| !! Port Scanner !! |
+--------------------+
--------------------------------------------------
Scanning Target: 192.168.1.6
Scanning started at: 2023-02-03 12:08:48.785490
--------------------------------------------------
Port 139 is open: netbios-ssn
Port 135 is open: epmap
Port 445 is open: microsoft-ds
```
