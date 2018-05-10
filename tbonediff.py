import os
import time

print "This script allows you to compare a list of tbone configs with past date configs."
input = raw_input("Enter the input filename (devices hostnames in file must be FQDN with or without the .gz file extension: ")
date1 = raw_input("Enter the past date to compare with, for example, apr20: ")
date2 = raw_input("Enter the more current date to compare with, for example, apr30: ")
diffreport = raw_input("Enter the name of the diffreport: ")
single = raw_input("Enter an \"s\" if you want a single consolidated report only, if not just hit enter: ")

with open(input) as p:
    for devices in p:
        os.system('diff -u /home/john.gonzalez2/Py/configs/7843/' + date1 + '/' + devices.rstrip("\n") + ' /home/john.gonzalez2/Py/configs/7843/' + date2 + '/' + devices.rstrip("\n") + str(" >> tmp_") + devices.rstrip("\n"))
        print "Compared configs for " + devices.rstrip("\n")
results = os.system('ls -la | grep tmp_ | grep -v " 0 " | awk {\'print $9\'} >> ' + str(diffreport))
with open(diffreport) as r:
    for line in r:
        os.system('cat ' + line.rstrip("\n") + str(" >> ") + line.replace('tmp_', 'diff_'))
print "\nThere was a diff in the following devices: "
os.system('ls -la | grep diff_ | awk {\'print $9\'}')
os.system('more -1000000 diff_* >> ' + str(diffreport))
time.sleep(.5)
os.system('rm tmp_*')
if single  == 's':
    os.system('rm diff_*')
    print ("\nAll changes can be viewed in " + str(diffreport))
else:
    print ("\nAll changes can be viewed in " + str(diffreport) + " or individually by files named diff_<device name> ")
