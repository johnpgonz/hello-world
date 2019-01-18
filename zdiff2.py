import os
import time

print "This script allows you to compare a list of current configs with past date configs."
input = raw_input("Enter the input filename (devices hostnames in file must be FQDN with or without the .gz file extension: ")
date = raw_input("Enter the past date to compare with current, for example, 2018/04/24: ")
diffreport = raw_input("Enter the name of the diffreport: ")
single = raw_input("Enter an \"s\" if you want a single consolidated report only, if not just hit enter: ")
with open(input) as p:
    for devices in p:
        os.system('zdiff -u /home/configs/*/' + date + '/' + devices.rstrip(".gz\n") + str(".gz") + ' /home/configs/*/current/' + devices.rstrip(".gz\n") + str(".gz") + str(" >> temp/tmp_") + devices.rstrip(".gz\n"))
        print "Compared configs for " + devices.rstrip(".gz\n")
results = os.system('ls -la temp/ | grep tmp_ | grep -v " 0 " | awk {\'print $9\'} >> ' + str(diffreport))
time.sleep(.5)
with open(diffreport) as r:
    for line in r:
        os.system('cat temp/' + line.rstrip("\n") + str(" >> temp/") + line.replace('tmp_', 'diff_'))
print "\nThere was a diff in the following devices: "
os.system('ls -la temp/ | grep diff_ | awk {\'print $9\'}')
os.system('more -1000000 temp/diff_* >> ' + str(diffreport))
time.sleep(.5)
os.system('rm temp/tmp_*')
if single  == 's':
    os.system('rm temp/diff_*')
    print ("\nAll changes can be viewed in " + str(diffreport))
else:
    print ("\nAll changes can be viewed in " + str(diffreport) + " or individually by files named diff_<device name> in temp folder ")
