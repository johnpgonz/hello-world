import os
#This will extract a specific route-policy and create text file for each device
input = raw_input("Enter the input filename (devices hostnames in file must be FQDN with or without the .gz file extension: ")
search = raw_input("Enter the exact name of the route-policy you want to extract: ")

with open(input) as p:
    for devices in p:
        os.system(' zcat /home/configs/*/current/' + devices.rstrip(".gz\n") + str(".gz") + str(" | perl -e 'while (<>){print if (/^route-policy ")  + str(search) + str("/../^end-policy/);}'") + str(" >> ") + devices.rstrip(".gz\n") + str("_") + search)
        print ("Output for " + str(devices.rstrip(".gz\n")) + " has been written to " + str(devices.rstrip(".gz\n")) + str("_") + search)
