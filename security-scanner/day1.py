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
port = int(input("Enter a port number to check: "))

if port == 22:
    print("SSH detected - verify if needed")
elif port == 23:
    print("DANGER: Telnet is open - very insecure!")
elif port == 80:
    print("HTTP running - should use HTTPS")
elif port == 443:
    print("HTTPS - Good and secure!")
elif port == 3389:
    print("WARNING: RDP exposed - close immediately!")
else:
    print("Port", port, "noted - investigate further")

# Loop - scan multiple ports
print("\n--- Scanning Common Ports ---")

dangerous_ports = [21, 22, 23, 80, 443, 3389, 8080]

for port in dangerous_ports:
    if port == 23:
        print(f"Port {port}: DANGER - Telnet!")
    elif port == 3389:
        print(f"Port {port}: WARNING - RDP!")
    elif port == 21:
        print(f"Port {port}: WARNING - FTP unencrypted!")
    else:
        print(f"Port {port}: Noted")