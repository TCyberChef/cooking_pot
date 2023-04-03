#!/usr/bin/env python3
import socket
import select
import logging

BLACKLIST = ['google.com', 'google.co.uk', 'facebook.com']

logging.basicConfig(filename='server.log', level=logging.INFO)
def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('', 8000))
    server_socket.listen()

    inputs = [server_socket]
    clients = {}

    while True:
        read, _, _ = select.select(inputs, [], [])

        for sock in read:
            if sock == server_socket:
                client_socket, client_address = sock.accept()
                inputs.append(client_socket)
                clients[client_socket] = client_address
                logging.info(f'New client connected: {client_address}')
            else:
                data = sock.recv(1024).decode().strip()

                if not data:
                    sock.close()
                    inputs.remove(sock)
                    if sock in clients:
                        logging.info(f'Client disconnected: {clients[sock]}')
                        del clients[sock]
                else:
                    if any(site in data for site in BLACKLIST):
                        logging.warning(f'Blacklisted site visited by {clients[sock]}: {data}')
                    else:
                        logging.info(f'Visited site: {data}')

main()