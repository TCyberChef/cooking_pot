from scapy.all import *

#define a function to check if a packet matches the target IP address

def check_pkt(pkt):
    if IP in pkt and pkt[IP].dst == "8.8.8.8":
        print("ALERT: Packet to 8.8.8.8 detected!") #print a message if the packet matches the target IP address
        
        
        
# start sniffing packets
sniff(prn=check_pkt)

