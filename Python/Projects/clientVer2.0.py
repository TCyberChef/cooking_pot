import socket
import time
import logging
import subprocess
import platform
import re

logging.basicConfig(filename='client.log', level=logging.INFO)

SERVER_ADDRESS = ('192.168.200.199', 8000) # change IP address to match server IP address 
HEARTBEAT_INTERVAL = 5
ARP_REGEX = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+\w+\s+\w+\s+([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})'

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(SERVER_ADDRESS)

    while True:
        # Send heartbeat
        client_socket.send('heartbeat'.encode())

        # Check ARP table for duplicate MAC address
        if platform.system() == 'Windows':
            arp_command = 'arp -a'
        elif platform.system() == 'Linux':
            arp_command = 'arp -a | grep -Eo "%s"' % ARP_REGEX
        else:
            logging.error('Unsupported operating system')
            break

        arp_output = subprocess.check_output(arp_command, shell=True).decode().strip()
        mac_addresses = re.findall(ARP_REGEX, arp_output)

        if len(mac_addresses) != len(set(mac_addresses)):
            logging.warning('Duplicate MAC address found in ARP table')
            client_socket.send('Duplicate MAC address found in ARP table'.encode())

        # Send message to server if google.com was searched
        if 'google.com' in arp_output:
            logging.warning('Google.com was searched')
            client_socket.send('Google.com was searched'.encode())

        time.sleep(HEARTBEAT_INTERVAL)
main()