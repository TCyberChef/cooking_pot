#create ICMP packet with scapy and send it to the IP in dst variable.

from scapy.all import *
sendp(Ether()/IP(dst='8.8.8.8')/ICMP()/"MESSAGE")