#!/bin/bash

clear
for (( i=1; i<=100; i++ ));
do
echo -ne "Launching...$i\r"
sleep 0.01
done
sleep 1
clear
figlet S S
echo This Tool Created By SHIBILGAMER
echo
echo "Enter Username without @"
read name
for (( j=1; j<=100; j++ )); do
echo -ne "searching username...$j%\r"
sleep 0.05
done
sleep 1
echo -e username searching succefull ✓
echo username:@$name
sleep 3

for (( i=1; i<=100; i++ )); do
    echo -ne "Instagram Account Baning..$i%\r"
    sleep 0.1  # Adjust sleep duration as needed
done
sleep 1
echo -e "\nban report sented succesfull ✓"
sleep 3
echo 'Wait 2 hours for instagram account baning '
