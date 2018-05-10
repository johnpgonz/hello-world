import paramiko
import os
import sys
import getpass
import time
import telnetlib

username = raw_input("Enter your username: ")
password = getpass.getpass()
input = raw_input("Enter the device filename: ")
directory = raw_input("Enter the directory to write output to: ")
commands = raw_input("Enter the command filename: ")
print "Got it, please standby..."

def SSH_FUNC():
    print "Starting device for loop..."
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(hostname=(devices.rstrip("\n")),username=username,password=password)
    print "Connected to " + devices.rstrip("\n")
    cmd = ssh_client.invoke_shell()
    c.seek(0) 
    print "Sending cmds..."
    for cmds in c:
        cmd.send(str(cmds) + "\n")
        print cmds.rstrip("\n") + ": has been executed"
        x = str(cmds.rstrip("\n"))
        if x.find("term len 0") != -1:
            time.sleep(0)
        elif x.find("admin show hw-module fpd location all") != -1:
            time.sleep(120)
        elif x.find("show controllers fabric link health") != -1:
            time.sleep(120)
        elif x.find("admin show version") != -1:
            time.sleep(60)
        elif x.find("show int | i \"line|Desc|rate|error\"") != -1:
            time.sleep(90)
        elif x.find("show tech-support") != -1:
            time.sleep(600)
        else:
            time.sleep(10)
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
        print "Changing stdout to print output to file, brb..."
        original = sys.stdout
        sys.stdout = open(str(directory) + devices.rstrip("\n") + ".txt" , "a")
        print output
        sys.stdout = original
        print "Ok, I'm back, just printed output of " + cmds.rstrip("\n") + " for " + devices.rstrip("\n")
        print "Moving to top of cmd for loop\n\n"
    print "No more cmds to execute, closing out the ssh session..."
    ssh_client.close
    print "Closed, moving back to top of device for loop...\n\n"

def TELNET_FUNC():
    print "SSH didn't work, I'll try telnet..."
    tn = telnetlib.Telnet(devices.rstrip("\n"))
    if password:
        tn.read_until("username:" or "Username:", 1) 
        tn.write(username + "\n")
        tn.read_until("Password:" or "password:", 1)
        tn.write(password + "\n")
        print "Connected to " + devices.rstrip("\n")
        c.seek(0)
        print "Sending cmds..."
        for cmds in c:
            tn.write(str(cmds) + "\n")
            print cmds.rstrip("\n") + " : will be executed"
        tn.write("exit\n")
        original = sys.stdout
        sys.stdout = open(str(directory) + devices.rstrip("\n") + ".txt" , "a")
        print tn.read_all()
        sys.stdout = original
        print "Ok, just printed output for " + devices.rstrip("\n")
        print "... moving back to top of the for loop...\n\n"
        print "Done."

with open(input) as f:
    with open(commands) as c:
        for devices in f:
            try:
                SSH_FUNC()
            except:
                try:
                     TELNET_FUNC()
                except:
                    print "!!!Could not telnet to " + devices.rstrip("\n") + " I'll move on...\n"
                    pass
