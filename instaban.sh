#!/bin/bash

clear
sleep 1
echo Subscribe Please
sleep 3
xdg-open "https://youtube.com/@SHIBILGAMER"
sleep 1
echo loading...
sleep 10
apt update -y
apt upgrade
pkg update -y
pkg upgrade
pkg install python -y
pkg install python2 -y
pkg install python3 -y
pkg install curl -y
pkg install figlet
sleep 1
bash local.sh
