#!/usr/bin/python3


import socket

HOST = '192.168.200.199'                # Symbolic name meaning all available interfaces
PORT = 9999             # Arbitrary non-privileged port

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello, world')
    data = s.recv(1024)
    