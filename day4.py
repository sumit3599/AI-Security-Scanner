# Sumit Kumar - Security Scanner
# Day 1 - My First Python Code

import socket

# Variables
name = "Sumit"
age = 28
goal = "Network Security Engineer"
target_ip = "192.168.1.1"

# Print
print("Developer:", name)
print("Age:", age)
print("Goal:", goal)
print("Target IP:", target_ip)

# Input
scan_target = input("Enter IP address to scan: ")
print("Scanning target:", scan_target)
print("Scanner initialized successfully!")

# Conditions

# Loop - scan multiple ports
print("\n--- Scanning Common Ports ---")

dangerous_ports = range(1, 101)

def check_port(port, scan_target):
    port_info = {
        21: f"Scanning {scan_target} - Port {port}: WARNING - FTP unencrypted!",
        22:f"Scanning {scan_target} - Port {port}: SSH",
        23: f"Scanning {scan_target} - Port {port}: DANGER - Telnet!",
        80: f"Scanning {scan_target} - Port {port}: HTTP - should use HTTPS",
        3389: f"Scanning {scan_target} - Port {port}: WARNING - RDP!",
    }
    return port_info.get(port, f"Scanning {scan_target} - Port {port}: Noted")

def is_dangerous(port):
    if port in [21, 23, 3389]:
        return True
    else:
        return False
    
def is_port_open(ip, port):
    sock = socket.socket()
    sock.settimeout(1)
    result = sock.connect_ex((ip, port))
    if result == 0:
        return True
    else:
        return False

scan_report = []

for port in dangerous_ports:
    if is_port_open(scan_target, port):
        result = check_port(port, scan_target)
        print(result)
        if is_dangerous(port):
            scan_report.append(port)
print(f"Total ports scanned: {len(dangerous_ports)}")
print(f"Dangerous ports found: {len(scan_report)}")
print(f"Dangerous ports: {scan_report}")

file = open("scan_history.txt", "a")
file.write(f"Scanned {scan_target} - Dangerous ports: {scan_report}\n")
file.close()