import os

# This is just a regular zgrep cmd that you would normally use without the directory and/or filename
search = raw_input("Enter the zgrep string (use zgrep -H to display filename, zgrep -A NUM for lines after): ")
# This will be the name of the new file containing output
output = raw_input("Enter the output filename you want to create: ")
print "Got it, per your request, running this: " + str(search) + ' /home/configs/archive/*-01/current/*' + str(" >> ") + str(output)
print "Will let you know when I'm done..."
os.system(str(search) + ' /home/configs/archive/*-01/current/*' + str(" >> ") + str(output))
print "Output has been written to " + str(output)
print "I'm done, here's a line count for how many matches: "
os.system(str("wc -l ") + str(output))
