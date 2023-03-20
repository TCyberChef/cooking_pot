#!/usr/bin/python3


import socket

HOST = ''                # Symbolic name meaning all available interfaces
PORT = 51207              # Arbitrary non-privileged port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
    
print(f"Received: {data!r}")
