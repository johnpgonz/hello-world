import os
#This will extract specific route-policies and create text file per policy
input = raw_input("Enter the input filename with a list of route-policies to extract from all devices: ")
hostname = raw_input("Enter the hostname of the device you want to extract policies from without .gz or fqdn:  ")
with open(input) as p:
    for policy in p:
        os.system('zcat /home/configs/*/current/' + str(hostname) + str("* | perl -e 'while (<>){print if (/^route-policy ")  + policy + str("/../^end-policy/);}'") + str(" >> ") + str(hostname) + str(":") + policy)
        print ("Output has been printed to :  " +  str(hostname) + str(":") + policy)
