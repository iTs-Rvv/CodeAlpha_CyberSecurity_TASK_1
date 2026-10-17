
from scapy.all import sniff, IP, IPv6, TCP, UDP, ICMP, Raw

def packet_callback(packet):
    print("\n--- Packet Captured ---")

    # IPv4 information
    if IP in packet:
        ip_layer = packet[IP]
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")

    # IPv6 information
    elif IPv6 in packet:
        ip_layer = packet[IPv6]
        print(f"Source IPv6: {ip_layer.src}")
        print(f"Destination IPv6: {ip_layer.dst}")

    # Protocol and port information
    if TCP in packet:
        tcp_layer = packet[TCP]
        print("Protocol: TCP")
        print(f"Source Port: {tcp_layer.sport}")
        print(f"Destination Port: {tcp_layer.dport}")

    elif UDP in packet:
        udp_layer = packet[UDP]
        print("Protocol: UDP")
        print(f"Source Port: {udp_layer.sport}")
        print(f"Destination Port: {udp_layer.dport}")

    elif ICMP in packet:
        print("Protocol: ICMP")

    # Display available raw payload
    if Raw in packet:
        payload = packet[Raw].load
        print(f"Payload (first 100 bytes): {payload[:100]!r}")

print("Starting packet capture...")
sniff(count=10, prn=packet_callback)
print("Packet capture completed.")
