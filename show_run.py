import paramiko
import os
import sys
import getpass
import time

username = raw_input("Enter your username: ")
password = getpass.getpass()
print "Got it, please standby..."


with open("iosxr_list.txt") as f:
    for devices in f:
        print "Starting for loop..."
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(hostname=(devices.rstrip("\n")),username=username,password=password)
        print "Connected to " + devices.rstrip("\n")
        cmd = ssh_client.invoke_shell()
        print "Sending term len and show run cmds..."
        cmd.send("term len 0\n")
        cmd.send("show run\n")
        print "CMDs have been executed, sleeping for 5 secs..."
        time.sleep(5)
        print "5 seconds are over, buffering config..."
        output = ""
        while True:
            if cmd.recv_ready():
                print "...At top of nested while loop"
                output += cmd.recv(65535)
                print "...At bottom of nested while loop"
                time.sleep(1)
                print "...The output length is: " + str(len(output))
            else:
                print "Broke out of nested while loop"
                break
        print "Back to regular for loop,changing stdout to print to file, brb..."
        original = sys.stdout
        sys.stdout = open(devices.rstrip("\n") + ".txt" , "w")
        print output
        sys.stdout = original
        print "Ok, I'm back, just printed output for " + devices.rstrip("\n")
        print "Closing out the ssh session..."
        ssh_client.close
        print "Closed, moving back to top of the for loop...\n\n"
print "Done."
