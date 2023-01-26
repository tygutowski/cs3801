from scapy.all import *
import random

conf.iface="wlan1"

# Initialize destination IP and message to be sent.
dst = "192.168.1.100"
msg = "adastra per explotium"

pcap = []

for character in msg:
    # Create a packet using TCP to ensure they are received.
    # Encrypt character into numeric value with ord() and send as dport.
    # Create random string to be sent in in the Raw load to confuse interceptors.
    pkt = IP(dst=dst)/TCP(sport=20,dport=ord(character))/Raw(load=random.choice(string.ascii_lowercase))
    # Append packet to pcap list.
    pcap.append(pkt)

# Send all packets.
wrpcap("pcap.pcap",pcap)
send(pcap)
