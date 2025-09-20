# This script is supposed to be run on an empty cisco switch.
# It will then configure the device to allow for SSH access.
import serial
import time
import sys
from tqdm import tqdm
from pathlib import Path

script_dir = Path(__file__).parent
sys.path.insert(0, str(script_dir))

from config import get_user_input

def cisco_switch_settings(run = "default"):
    # Get the directory where this script is located, then go up to project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent  # Go up one level from scripts/ to project root
    commands_dir = project_root / "commands"

# Collect user input into the variables dictionary
    variables = get_user_input()

# Open the serial port and read the commands from the file
    ser = serial.Serial(variables["serial_port"])  # open serial port
    print(f'The serial port used is {ser.name}')      # check which port was really used
    with open(commands_dir/"cisco_switch_mgmt_commands.txt") as file:
        commands = file.readlines()
        for command in commands:
            formatted_command = command.format(**variables)
            ser.write(formatted_command).encode() # write a string
            if "crypto key generate rsa" in command.strip():
                for i in tqdm(range(20), desc="Waiting for key generation"):
                    time.sleep(0.5)
            else:
                time.sleep(1.5)
            print(ser.read(ser.in_waiting or 1).decode()) # read all characters in buffer
    ser.close()             # close port

def cisco_switch_settings_test():
    # Get the directory where this script is located, then go up to project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent  # Go up one level from scripts/ to project root
    commands_dir = project_root / "commands"

# Collect user input into the variables dictionary
    variables = get_user_input()

    with open(commands_dir/"cisco_switch_mgmt_commands.txt") as file:    
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
    cisco_switch_settings_test()