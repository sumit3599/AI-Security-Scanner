# Sumit Kumar - AI-Powered Security Scanner
# GitHub: github.com/sumit3599/AI-Security-Scanner

import socket
import threading
import argparse
from colorama import Fore, Style
from sklearn.ensemble import IsolationForest
import numpy as np


parser = argparse.ArgumentParser(description="AI Security Scanner")
parser.add_argument("--target", help="IP address to scan")
parser.add_argument("--ports", help="Port range e.g. 1-100")
args = parser.parse_args()

scan_target = args.target
parts = args.ports.split("-")
start = int(parts[0])
end = int(parts[1])
print("Scanning target:", scan_target)
print("Scanner initialized successfully!")
print("\n--- Scanning Common Ports ---")


dangerous_ports = range(start, end + 1)


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
open_ports = []

def grab_banner(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(2)
        sock.connect((ip, port))
        banner = sock.recv(1024)
        return banner.decode()
    except:
        return "No banner"

def scan_port(port):
    if is_port_open(scan_target, port):
        result = check_port(port, scan_target)
        banner = grab_banner(scan_target, port)
        if is_dangerous(port):
            print(Fore.RED + f"{result} | Banner: {banner}" + Style.RESET_ALL)
            scan_report.append(port)
        elif port == 443:
            print(Fore.GREEN + f"{result} | Banner: {banner}" + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + f"{result} | Banner: {banner}" + Style.RESET_ALL)
        with open("scan_history.txt", "a") as file:
            file.write(f"{result} | Banner: {banner}\n")
        open_ports.append(port)

threads = []

def detect_anomaly(open_ports_count, dangerous_ports_count):
    # Training data - what normal looks like
    normal_data = [
    [1, 0], [2, 0], [1, 0], [2, 1], [1, 0],
    [2, 0], [1, 0], [3, 0], [2, 0], [1, 1]
]
    
    model = IsolationForest(contamination=0.1)
    model.fit(normal_data)
    
    result = model.predict([[open_ports_count, dangerous_ports_count]])
    
    if result[0] == -1:
        return "ANOMALY DETECTED - Suspicious scan result!"
    else:
        return "Normal scan result"


for port in range(start, end + 1):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()


print(f"Total ports scanned: {len(list(range(start, end + 1)))}")
print(f"Dangerous ports found: {len(scan_report)}")
print(f"Dangerous ports: {scan_report}")

file = open("scan_history.txt", "a")
file.write(f"Scanned {scan_target} - Dangerous ports: {scan_report}\n")
file.close()

anomaly_result = detect_anomaly(len(open_ports), len(scan_report))
print(Fore.CYAN + f"\n--- AI ANALYSIS ---\n{anomaly_result}" + Style.RESET_ALL)