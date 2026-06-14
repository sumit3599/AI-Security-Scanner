# Sumit Kumar - Security Scanner
# Day 1 - My First Python Code

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

dangerous_ports = [21, 22, 23, 80, 443, 3389, 8080]

def check_port(port, scan_target):
    if port == 23:
        return f"Scanning {scan_target} - Port {port}: DANGER - Telnet!"
    elif port == 3389:
        return f"Scanning {scan_target} - Port {port}: WARNING - RDP!"
    elif port == 21:
        return f"Scanning {scan_target} - Port {port}: WARNING - FTP unencrypted!"
    else:
        return f"Scanning {scan_target} - Port {port}: Noted"
    
def is_dangerous(port):
    if port in [21, 23, 3389]:
        return True
    else:
        return False

for port in dangerous_ports:
    if is_dangerous(port):
        result = check_port(port, scan_target)
        print(result)