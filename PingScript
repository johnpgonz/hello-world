import os

f = open("iplist.txt")
line = f.readlines()
for devices in line:
    os.system("ping -c 1 " + devices.rstrip("\n"))
