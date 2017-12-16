# test
import os

f = open("ping_this.txt")
line = f.readline()
for devices in line:
    print(str(f.readline().rstrip(" \n")))