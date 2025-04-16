import pyshark
import matplotlib.pyplot as plt
from collections import Counter


# Function to analyze captured packets
def analyze_packets(capture_file):
    cap = pyshark.FileCapture(capture_file)

    # Packet summary statistics
    packet_count = 0
    protocols = []

    for packet in cap:
        packet_count += 1
        protocols.append(packet.transport_layer)  # Extract transport layer protocol (TCP/UDP)

    print(f"Total packets captured: {packet_count}")

    # Count protocol occurrences
    protocol_count = Counter(protocols)

    print("Protocol distribution:")
    for protocol, count in protocol_count.items():
        print(f"{protocol}: {count}")

    # Plot protocol distribution
    labels = list(protocol_count.keys())
    sizes = list(protocol_count.values())

    plt.figure(figsize=(10, 6))
    plt.bar(labels, sizes, color='skyblue')
    plt.xlabel("Protocol")
    plt.ylabel("Frequency")
    plt.title("Protocol Distribution in Captured Traffic")
    plt.savefig("protocol_distribution.png")
    print("Protocol distribution chart saved as 'protocol_distribution.png'")


# Run the analysis function
if __name__ == "__main__":
    capture_file = "captured_traffic.pcap"  # The captured packet file
    analyze_packets(capture_file)
