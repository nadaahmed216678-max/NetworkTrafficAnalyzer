# Network Traffic Analyzer

## Project Overview

Network Traffic Analyzer is a basic Python tool that reads PCAP files and analyzes network packets using Scapy.

## Features

* Reads packets from a PCAP file.
* Identifies common protocols, including TCP, UDP, and ICMP.
* Displays source and destination IP addresses.
* Displays source and destination port numbers when available.
* Counts packets by protocol.
* Displays a summary of analyzed traffic.
* Handles errors such as missing files and file-reading failures.

## Technologies Used

* Python
* Scapy
* collections.Counter

## Project Files

* `main.py`: Main program for analyzing network traffic.
* `sample.pcap`: Sample PCAP file used for testing.
* `packet_basics.py`: Packet analysis practice.
* `pcap_basics.py`: PCAP file reading and writing practice.
* `counter_example.py`: Protocol counting practice.

## Requirements

* Python 3
* Scapy

Install Scapy using:

```bash
pip install scapy
```

## How to Run

1. Place `main.py` and `sample.pcap` in the same directory.
2. Open a terminal in the project directory.
3. Run:

```bash
python main.py
```

## Testing

The program was tested with a sample PCAP file containing three packets: UDP, TCP, and ICMP.

The program correctly displayed packet details and counted one packet for each protocol.

A missing-file test was also performed to verify error handling.

## Safety Note

This version analyzes a saved PCAP file. It does not perform live network capture. Only analyze traffic that you are authorized to access.

## Learning Resources

* Python documentation: https://docs.python.org/3/
* Scapy documentation: https://scapy.readthedocs.io/
