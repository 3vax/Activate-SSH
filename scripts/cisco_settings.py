# This script is supposed to be run on an empty cisco switch or router.
# It will then configure the device to allow for SSH access.
import serial
import time
import sys
from tqdm import tqdm
from pathlib import Path

script_dir = Path(__file__).parent
sys.path.insert(0, str(script_dir))

from config import get_user_input

def cisco_settings(device_type):
    # Get the directory where this script is located, then go up to project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent  # Go up one level from scripts/ to project root
    commands_dir = project_root / "commands"

# Collect user input into the variables dictionary
    if device_type == "switch":
        variables = get_user_input("switch")
        commands_for_device = "cisco_switch_mgmt_commands.txt"
    
    if device_type == "router":
        variables = get_user_input("router")
        commands_for_device = "cisco_router_mgmt_commands.txt"

# Open the serial port and read the commands from the file
    ser = serial.Serial(variables["serial_port"])  # open serial port
    print(f'The serial port used is {ser.name}')      # check which port was really used
    with open(commands_dir/commands_for_device) as file:
        commands = file.readlines()
        for command in commands:
            formatted_command = command.format(**variables)
            ser.write(formatted_command.encode()) # encode the string before writing
            if "crypto key generate rsa" in command.strip():
                for i in tqdm(range(20), desc="Waiting for key generation"):
                    time.sleep(0.5)
            else:
                time.sleep(1.5)
            print(ser.read(ser.in_waiting or 1).decode()) # read all characters in buffer
    ser.close()             # close port

def cisco_switch_settings_test(device_type):
    # Get the directory where this script is located, then go up to project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent  # Go up one level from scripts/ to project root
    commands_dir = project_root / "commands"

# Collect user input into the variables dictionary
    if device_type == "switch":
        variables = get_user_input("switch")
        commands_for_device = "cisco_switch_mgmt_commands.txt"
    
    if device_type == "router":
        variables = get_user_input("router")
        commands_for_device = "cisco_router_mgmt_commands.txt"
     # check which port was really used
    with open(commands_dir/commands_for_device) as file:
        commands = file.readlines()
        for command in commands:
            formatted_command = command.format(**variables)
            print(formatted_command.encode())
            
            if "crypto key generate rsa" in command.strip():
                for i in tqdm(range(20), desc="Waiting for key generation"):
                    time.sleep(0.5)
            else:
                time.sleep(1.5)

if __name__ == "__main__":
    cisco_switch_settings_test("router")