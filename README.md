# Network Scanner
A Python script to perform network scanning similar to Nmap and display the port number and service name running on that port. This script is designed to be faster with basic multithreading.

# Usage

python network_scanner.py <hostname or IP>
  
# Requirements
Python 3
  
# Features
Perform network scanning on a host or IP
Display port number and service name running on that port
Basic multithreading for improved speed
  
# Example Output
$ python network_scanner.py 192.168.0.1

Scanning Host: 192.168.0.1

PORT   SERVICE
22     ssh
80     http
443    https
