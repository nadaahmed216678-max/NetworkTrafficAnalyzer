
from collections import Counter
from scapy.all import rdpcap, IP, IPv6, Ether, TCP, UDP, ICMP, ARP


def identify_protocol(packet):
    if packet.haslayer(TCP):
        return "TCP"
    elif packet.haslayer(UDP):
        return "UDP"
    elif packet.haslayer(ICMP):
        return "ICMP"
    elif packet.haslayer(ARP):
        return "ARP"
    elif packet.haslayer(IP):
        return "Other IPv4"
    elif packet.haslayer(IPv6):
        return "Other IPv6"
    else:
        return "Other"


def analyze_pcap(filename):
    try:
        packets = rdpcap(filename)

    except FileNotFoundError:
        print("Error: PCAP file not found.")
        return

    except PermissionError:
        print("Error: Permission denied.")
        return

    except Exception as error:
        print("Error reading PCAP file:", error)
        return

    protocol_counts = Counter()

    print("\n=== Network Traffic Analyzer ===")
    print("Total packets:", len(packets))

    for index, packet in enumerate(packets, start=1):
        protocol = identify_protocol(packet)
        protocol_counts[protocol] += 1

        print(f"\nPacket #{index}")
        print("Protocol:", protocol)
        print("Length:", len(packet), "bytes")

        if packet.haslayer(IP):
            print("Source IP:", packet[IP].src)
            print("Destination IP:", packet[IP].dst)

        elif packet.haslayer(IPv6):
            print("Source IP:", packet[IPv6].src)
            print("Destination IP:", packet[IPv6].dst)

        elif packet.haslayer(ARP):
            print("Source IP:", packet[ARP].psrc)
            print("Destination IP:", packet[ARP].pdst)

        elif packet.haslayer(Ether):
            print("Source MAC:", packet[Ether].src)
            print("Destination MAC:", packet[Ether].dst)

        else:
            print("Source and destination addresses unavailable.")

        if packet.haslayer(TCP):
            print("Source Port:", packet[TCP].sport)
            print("Destination Port:", packet[TCP].dport)

        elif packet.haslayer(UDP):
            print("Source Port:", packet[UDP].sport)
            print("Destination Port:", packet[UDP].dport)

    print("\n=== Protocol Summary ===")

    for protocol, count in protocol_counts.most_common():
        print(f"{protocol}: {count}")

    print("\nTotal packets counted:", sum(protocol_counts.values()))


if __name__ == "__main__":
    analyze_pcap("sample.pcap")