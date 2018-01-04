import os

input = raw_input("Enter the input filename (devices hostnames in file must be FQDN with or without the .gz file extension: ")
search = raw_input("Enter the zgrep string (use zgrep -H to display filename, zgrep -A NUM for lines after): ")
output = raw_input("Enter the output filename you want to create: ")

with open(input) as p:
    for devices in p:
        os.system(str(search) + ' /home/configs/archive/*-01/current/' + devices.rstrip(".gz\n") + str(".gz") + str(" >> ") + str(output))
        print "Output for " + devices.rstrip(".gz\n") + " has been written to " + str(output)
