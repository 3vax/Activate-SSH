# This script is supposed to be run on an empty cisco switch or router.
# It will then configure the device to allow SSH access.
import serial
import time

# Get user input for configuration:
#hostname = input("Enter hostname: ")
#vlan = input("Enter VLAN-id: ")
#vlan1 = input("Enter VLAN interface id: ")
#ip_address = input("Enter IP address: ")
#ip_address1 = input("Enter secondary IP address: ")
#subnet_mask = input("Enter subnet mask: ")
#subnet_mask1 = input("Enter secondary subnet mask: ")
#default_gateway = input("Enter default gateway: ")
#domain_name = input("Enter domain name: ")
#username =  input("Enter username: ")
#password = input("Enter password: ")
#ssh_version = input("Enter SSH version (1 or 2)(2 is default): ")
#key_size = input("Enter key size (360-4096): ")

#commands = [
#    'enable',
#    'conf t',
#    f'hostname {hostname}',
#    f'int vlan {vlan}',
#    f'ip address {ip_address} {subnet_mask}',
#    'no shut',
#    'exit',
#    f'int vlan {vlan1}',
#    f'ip address {ip_address1} {subnet_mask1}',
#    'no shut',
#    'exit',
#    'int f0/1',
#    'switchport mode access',
#    f'switchport access vlan {vlan}',
#    'exit',
#    'ip default-gateway 10.10.99.1',
#    'ip domain-name test.com',
#    f'username {username} password {username}',
#    'crypto key generate rsa',
#    f'{key_size}',
#    'ip ssh version 2',
#    'line vty 0 15',
#    'login local',
#    'transport input ssh',
#    'end'
#]

ser = serial.Serial('COM4')  # open serial port
print(ser.name)      # check which port was really used
with open("sw-commandoes.txt") as file:
    commands = file.readlines()
    sleep_next = False
    for command in commands:
        ser.write(command.encode()) # write a string
        if sleep_next:
            time.sleep(10)
            sleep_next = False

        if "crypto key generate rsa" in command.strip():
            time.sleep(3)
            sleep_next = True
        else:
            time.sleep(1.5)
        print(ser.read(ser.in_waiting or 1).decode()) # read all characters in buffer
ser.close()             # close port

