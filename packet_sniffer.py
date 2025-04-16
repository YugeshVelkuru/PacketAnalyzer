import pyshark


# Function to capture packets
def capture_packets(interface):
    print("Starting packet capture...")
    cap = pyshark.LiveCapture(interface=interface)

    # Start capturing
    cap.sniff(timeout=60)  # Capture for 60 seconds

    # Save the captured packets to a file
    cap.save_file("captured_traffic.pcap")
    print("Packets saved to captured_traffic.pcap")


# Run the capture function
if __name__ == "__main__":
    # Replace 'eth0' with the actual network interface
    interface = "Ethernet"
    capture_packets(interface)

