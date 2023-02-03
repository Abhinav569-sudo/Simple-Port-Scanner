# This a python3 port scanning program made using python3 socket library.
import socket
import sys
import threading
from datetime import datetime


# Space for banner printing.
def ascii_art(text):
    # split the text into lines.
    lines = text.split("\n")

    # Find the longest line.
    max_length = max(len(line) for line in lines)

    # Create a horizontal rule
    horizontal_rule = "+" + "-" * (max_length + 2) + "+"

    # Create the output string
    output = horizontal_rule + "\n"
    for line in lines:
        output += "| " + line.ljust(max_length) + " |\n"
    output += horizontal_rule
    return output


print(ascii_art("!! Port Scanner !!"))

# Defining a target
host = sys.argv[1]
start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

# Add Banner
print("-" * 50)
print("Scanning Target: " + host)
print("Scanning started at: " + str(datetime.now()))
print("-" * 50)


# defining a function for a thread.
def scan_port(port_num):
    try:
        # socket.AF_INET = use IPv4,
        # socket.SOCK_STREAM = Use TCP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        # Return an error marker.
        result = s.connect_ex((host, port_num))
        if result == 0:
            service = socket.getservbyport(port_num)
            print("Port {0} is open: {1}".format(port_num, service))
        s.close()

    except KeyboardInterrupt:
        print("\n Exiting Program !!")
        sys.exit()
    except socket.gaierror:
        print("\n Hostname could not be resolved !!")
        sys.exit()
    except socket.error:
        print("\n Server not responding !!")
        sys.exit()


# Using the multi-Threading to improve its speed.
# Create a thread list.
threads = []

# Scan port between 1 to 65,535
for port in range(start_port, end_port + 1):
    # Creating new thread for each port.
    t = threading.Thread(target=scan_port,
                         args=(port, ))
    threads.append(t)

# Start all the threads
for t in threads:
    t.start()

# Wait for all the threads to complete.
for t in threads:
    t.join()
