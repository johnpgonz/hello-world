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

with open(input) as f:
    with open(commands) as c:
        for devices in f:
            try:
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
                    print cmds.rstrip("\n") + " : has been executed"
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
                    print "Back to regular for loop, changing stdout to print to file, brb..."
                    original = sys.stdout
                    sys.stdout = open(str(directory) + devices.rstrip("\n") + ".txt" , "a")
                    print output
                    sys.stdout = original
                    print "Ok, I'm back, just printed output for " + devices.rstrip("\n")
                print "Closing out the ssh session..."
                ssh_client.close
                print "Closed, moving back to top of the for loop...\n\n"
            except:
                print "SSH didn't work, I'll try telnet..."
                tn = telnetlib.Telnet(devices.rstrip("\n"))
                if password:
                    tn.read_until("username:" or "Username:", 1) 
                    tn.write(username + "\n")
                    tn.read_until("Password:" or "password:", 1)
                    tn.write(password + "\n")
                    print "Connected to " + devices.rstrip("\n")
                    print "Sending cmds..."
                    tn.write(str(command1) + "\n")
                    tn.write(str(command2) + "\n")
                    tn.write(str(command3) + "\n")
                    tn.write("exit\n")
                    original = sys.stdout
                    sys.stdout = open(str(directory) + devices.rstrip("\n") + ".txt" , "a")
                    print tn.read_all()
                    sys.stdout = original
                    print "Ok, just printed output for " + devices.rstrip("\n")
                    print "... moving back to top of the for loop...\n\n"
        print "Done."