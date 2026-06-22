# AI-Powered Automated Security Scanner

A Python-based network security scanner with AI anomaly detection, built as a portfolio project for cybersecurity roles.

## Features
- Real port scanning using Python socket
- Multi-threaded scanning for speed
- Banner grabbing to identify services and versions
- AI anomaly detection using Isolation Forest (scikit-learn)
- Color coded output (Red/Yellow/Green)
- Permanent scan history logging
- Professional CLI interface

## Installation

```bash
git clone https://github.com/sumit3599/AI-Security-Scanner.git
cd AI-Security-Scanner
pip install colorama scikit-learn
```

## Usage

```bash
python scanner.py --target <IP_ADDRESS> --ports <START-END>
```

### Examples

```bash
# Scan common ports on a target
python scanner.py --target 1.1.1.1 --ports 1-100

# Scan a specific range
python scanner.py --target 192.168.1.1 --ports 1-1000
```