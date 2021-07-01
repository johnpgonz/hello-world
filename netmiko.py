from netmiko import ConnectHandler
from getpass import getpass

password = getpass()
username = str("p2133799")

device1 = { 
    "device_type": "cisco_ios",
    "host": "rrrzoenwdcocd",
    "username": username,
    "password": password,
}

device2 = {
    "device_type": "cisco_ios",
    "host": "rrrzpenwdcocd",
    "username": username,
    "password": password,
}

device3 = { 
    "device_type": "cisco_ios",
    "host": "rrrzqenwdcocd",
    "username": username,
    "password": password,
}

device4 = {
    "device_type": "cisco_ios",
    "host": "rrrzrenwdcocd",
    "username": username,
    "password": password,
}

device5 = { 
    "device_type": "cisco_ios",
    "host": "rrrzsenwdcocd",
    "username": username,
    "password": password,
}

device6 = {
    "device_type": "cisco_ios",
    "host": "rrrztenwdcocd",
    "username": username,
    "password": password,
}

device7 = { 
    "device_type": "cisco_ios",
    "host": "rrrzuenwdcocd",
    "username": username,
    "password": password,
}

device8 = {
    "device_type": "cisco_ios",
    "host": "rrrzvenwdcocd",
    "username": username,
    "password": password,
}

device9 = { 
    "device_type": "cisco_ios",
    "host": "rrrzwenwdcocd",
    "username": username,
    "password": password,
}

device10 = {
    "device_type": "cisco_ios",
    "host": "rrrzxenwdcocd",
    "username": username,
    "password": password,
}

device11 = { 
    "device_type": "cisco_ios",
    "host": "rrrzyenwdcocd",
    "username": username,
    "password": password,
}

device12 = {
    "device_type": "cisco_ios",
    "host": "rrrzzenwdcocd",
    "username": username,
    "password": password,
}
 
command1 = "term len 0"
command2 = "show bgp all all summary"

for device in (device1, device2, device3, device4, device5, device6, device7, device8, device9, device10, device11, device12):
    net_connect = ConnectHandler(**device)
    print(net_connect.find_prompt()) 
    output1 = net_connect.send_command(command1) 
    print(command2)
    output2 = net_connect.send_command(command2)
    print(output2)
