import socket
import os
import threading

HOST = '192.168.200.199'
PORT = 7788

menu = """
Welcome to the client!
Please choose an option:
1. Disable firewall
2. Modify hosts file
"""

def disable_firewall():
    os.system('cmd /k "netsh advfirewall set allprofiles state off"')

def display_hosts_file():
    with open(os.path.join("C:\\Windows\\System32\\drivers\\etc\\hosts"), "r") as hosts_file:
        print("\nCurrent contents of the hosts file:")
        print(hosts_file.read())

def recv_thread(socket):
    while True:
        data = socket.recv(1024).decode()
        if not data:
            break
        print(data)

# Create a socket and connect to the server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    # Start a separate thread to receive data from the server
    recv_thread = threading.Thread(target=recv_thread, args=(s,))
    recv_thread.start()
    while True:
        # Display the menu and get the user's choice
        print(menu)
        choice = input("Enter an option number: ")
        # Send the user's choice to the server
        s.sendall(choice.encode())
        # If the user chooses option 1, disable the firewall
        if choice == '1':
            disable_firewall()
        # If the user chooses option 2, modify the hosts file
        elif choice == '2':
            redirect_ip = input("Enter the redirect IP address: ")
            redirect_domain = input("Enter the domain to redirect: ")
            display_hosts_file()
            with open(os.path.join("C:\\Windows\\System32\\drivers\\etc\\hosts"), "a") as hosts_file:
                hosts_file.write(f"\n{redirect_ip}    {redirect_domain}")
            display_hosts_file()
