# Basic Network Sniffer

## Overview
A beginner-friendly Python network sniffer built with **Scapy**. It captures 10 network packets and displays useful information about each packet, including source and destination IP addresses, protocol numbers, TCP/UDP port numbers, and raw payload data when available.

## Features
- Captures 10 packets for a demonstration.
- Displays source and destination IPv4 addresses when present.
- Displays the IP protocol number.
- Displays source and destination ports for TCP and UDP packets.
- Displays raw payload data when a `Raw` layer is present.

## Requirements
- Python 3
- Scapy
- Appropriate permissions to capture network traffic

## Installation

Install Scapy:

```bash
python -m pip install scapy
```

On Windows, you may also need to install **Npcap** to capture packets.

## Usage

1. Save the program as `network_sniffer.py`.
2. Open a terminal in the directory containing the file.
3. Run the program with the permissions required by your operating system:

```bash
python network_sniffer.py
```

On some Linux systems, packet capture may require `sudo`:

```bash
sudo python3 network_sniffer.py
```

The program starts capturing packets and stops after it has captured 10 packets. It may wait if there is not enough network traffic.

## Example Output

Output varies depending on the packets captured. Example:

```text
Starting packet capture...

--- Packet Captured ---
Source IP: 192.168.1.5
Destination IP: 142.250.183.14
Protocol: 6
Source Port: 52341
Destination Port: 443
```

The addresses and port numbers above are illustrative examples, not actual capture results. In this program, protocol number `6` represents TCP and `17` represents UDP.

## How It Works
1. Imports `sniff` from Scapy.
2. Defines `packet_callback(packet)`, which is called for each captured packet.
3. Checks for an IP layer and prints source IP, destination IP, and protocol number.
4. Checks for TCP or UDP and prints the corresponding source and destination ports.
5. Prints raw payload bytes when a `Raw` layer is available.
6. Calls `sniff(count=10, prn=packet_callback)` to capture and process 10 packets.

## Limitations
- The program currently checks IPv4 (`IP`) packets, not IPv6.
- Payload data may be binary or encrypted, so it may not be readable.
- The capture depends on the selected/default network interface and operating-system permissions.
- This is a basic demonstration, not a full-featured packet analyzer.

## Safety and Privacy
Only capture traffic on networks and devices you own or have explicit permission to monitor. Packet payloads can contain sensitive information. Avoid sharing captured logs or payloads publicly.

## Project Task
**Task 1: Basic Network Sniffer**
- Build a Python program to capture network traffic packets.
- Analyze captured packets to understand their structure and content.
- Learn how data flows through the network and the basics of protocols.
- Use Scapy for packet capturing.
- Display source/destination IPs, protocols, ports, and available payloads.

## License
This project is provided for educational use.
