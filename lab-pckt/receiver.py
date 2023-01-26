from scapy.all import *

# If a packet is received via sniff(), this function is called.
def pkt_callback(pkt):
    print(pkt)
    # Unencrypts the 
    character = str(chr(pkt[TCP].dport))
    print("[+] Received Character: " + character)


print("[+] Started Listener")

# Sniffs all tcp packets received through wlan0.
sniff(prn=pkt_callback, filter='tcp', store=0, iface="eth1")#, iface='wlan0')