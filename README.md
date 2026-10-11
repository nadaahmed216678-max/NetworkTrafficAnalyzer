# Network Traffic Analyzer

## Project Overview

Network Traffic Analyzer is a Python-based tool that reads saved PCAP files and analyzes network packets using Scapy. It was developed for learning basic network security and packet analysis concepts.

## Features

* Reads packets from a PCAP file.
* Identifies common protocols such as TCP, UDP, and ICMP.
* Displays source and destination IP addresses where available.
* Displays source and destination port numbers for TCP and UDP packets.
* Counts packets by protocol.
* Displays a summary of analyzed traffic.
* Handles errors such as missing PCAP files and file-reading failures.

## Technologies and Libraries

* Python 3
* Scapy
* `collections.Counter` (Python standard library)

## Project Files

* `main.py`: Main network traffic analyzer.
* `sample.pcap`: Sample PCAP file used for testing.
* `packet_basics.py`: Packet analysis practice.
* `pcap_basics.py`: PCAP file reading and writing practice.
* `counter_example.py`: Protocol counting practice.

## Installation

Install Python 3, then install Scapy:

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

## Testing and Results

The program was tested using a sample PCAP file containing three packets: one UDP packet, one TCP packet, and one ICMP packet.

The program displayed packet information and reported one packet for each protocol, with three packets counted in total.

A missing-file test was also performed to verify that the program displays an appropriate error message.

## External Resources

* Scapy Documentation: https://scapy.readthedocs.io/
* Python Documentation: https://docs.python.org/3/
* Wireshark Documentation: https://www.wireshark.org/docs/

## Safety Note

This version reads saved PCAP files and does not perform live network capture. Only analyze traffic that you are authorized to access.

## Limitations

The current version provides basic packet analysis. It does not decrypt encrypted traffic or perform advanced intrusion detection.

