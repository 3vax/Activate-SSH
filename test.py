# This script is supposed to be run on an empty cisco switch.
# It will then configure the device to allow for SSH access.
import serial
import time
from tqdm import tqdm
from pathlib import Path
from scripts.config import get_user_input

def cisco_switch_settings():
    # Variables to be filled in by the user
#    prompts = {
#        "serial_port": "Enter serial port (e.g., COM4): ",
#        "hostname": "Enter hostname for the device: ",
#        "device_password": "Enter enable secret password for the device: ",
#        "mgmt_vlan": "Enter VLAN-id for MGMT: ",
#        "mgmt_ipaddress": "Enter IP address: ",
#        "mgmt_subnetmask": "Enter subnet mask: ",
#        "mgmt_interface_port": "Enter interface port (e.g., g1/0/1): ",
#        "default_gateway": "Enter default gateway: ",
#        "domain_name": "Enter domain name: ",
#        "username": "Enter username: ",
#        "password": "Enter password: ",
#        "ssh_version": "Enter SSH version (1 or 2)(2 is default): ",
#        "key_size": "Enter key size (360-4096): "
#    }
    # Get the directory where this script is located (project root)
    project_root = Path(__file__).parent
    commands_dir = project_root / "commands"

    # Collect user input into the variables dictionary
    variables = get_user_input()

    # Open the serial port and read the commands from the file
 #   ser = serial.Serial(variables["serial_port"])  # open serial port
 #   print(ser.name)      # check which port was really used
    with open(commands_dir/"cisco_switch_mgmt_commands.txt") as file:
        commands = file.readlines()
        sleep_next = False
        for command in commands:
            formatted_command = command.format(**variables)
 #           ser.write(formatted_command).encode() # write a string
            print(formatted_command)
            if sleep_next:
                time.sleep(1.5)
                sleep_next = False

            if "crypto key generate rsa" in command.strip():
                for i in tqdm(range(10), desc="Waiting for key generation"):
                    time.sleep(1)
                sleep_next = True
            else:
                time.sleep(1.5)
 #           print(ser.read(ser.in_waiting or 1).decode()) # read all characters in buffer
 #   ser.close()             # close port


if __name__ == "__main__":
    cisco_switch_settings()