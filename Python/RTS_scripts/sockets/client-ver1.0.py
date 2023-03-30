#!/usr/bin/python3

import socket
import os

HOST = '192.168.200.199'                # Symbolic name meaning all available interfaces
PORT = 7788            # Arbitrary non-privileged port

menu = """
Welcome to the client!
Please choose an option:
1. Disable firewall
2. Option 2
3. Option 3
"""

def disable_firewall():
    os.system('cmd /k "netsh advfirewall set allprofiles state off"')
    
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True:
        data = s.recv(1024).decode()
        if not data:
            break
        print(data)
        option = input("Enter an option number: ")
        s.sendall(option.encode())
        response = s.recv(1024).decode()
        if option == '1':
            disable_firewall()
        elif option =='2':
            os.system("ping google.com")
            