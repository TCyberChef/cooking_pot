#!/usr/bin/python3

from scapy.all import *

def findDNS(p):
    if p.haslayer(DNS):
        print(p.summary())
        print(p.display())
sniff(prn=findDNS)