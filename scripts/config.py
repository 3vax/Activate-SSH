"""
Configuration module for Cisco device SSH setup.
Contains prompts and default values for device configuration.
"""

# Prompts for user input
PROMPTS = {
    "serial_port": "Enter serial port (e.g., COM4) (default is COM4): ",
    "hostname": "Enter hostname for the device: ",
    "device_password": "Enter password for the device: ",
    "mgmt_vlan": "Enter VLAN-id for MGMT: ",
    "mgmt_ipaddress": "Enter IP address: ",
    "mgmt_subnetmask": "Enter subnet mask (255.255.255.0 is default): ",
    "mgmt_interface_port": "Enter interface port (e.g., g1/0/1): ",
    "default_gateway": "Enter default gateway: ",
    "domain_name": "Enter domain name: ",
    "username": "Enter username: ",
    "password": "Enter password: ",
    "ssh_version": "Enter SSH version (1 or 2)(2 is default): ",
    "key_size": "Enter key size (360-4096) (1024 is default): "
}

# Default values (optional)
DEFAULTS = {
    "serial_port": "COM4",
    "mgmt_vlan": "99",
    "mgmt_subnetmask": "255.255.255.0",
    "key_size": "1024",
    "ssh_version": "2"
    
}

def get_user_input():
    """
    Collect user input for all configuration parameters.
    Returns a dictionary with user-provided values.
    """
    variables = {}
    for key, prompt in PROMPTS.items():
        default = DEFAULTS.get(key, "")
        if default:
            user_input = input(f"{prompt}({default}): ").strip()
            variables[key] = user_input if user_input else default
        else:
            variables[key] = input(prompt)
    return variables