"""
Configuration module for Cisco device SSH setup.
Contains prompts and default values for device configuration.
"""

# Device-specific prompts
PROMPTS = {
    "switch": {
        "serial_port": "Enter serial port (e.g., COM4) (COM4 is default): ",
        "hostname": "Enter hostname for the device: ",
        "device_password": "Enter password for the device: ",
        "mgmt_svi": "Enter VLAN-id for MGMT (99 is default): ",
        "mgmt_ipaddress": "Enter IP address: ",
        "mgmt_subnetmask": "Enter subnet mask (255.255.255.0 is default): ",
        "mgmt_interface_port": "Enter MGMT interface/trunk port (e.g., g1/0/1): ",
        "mgmt_access_interface_port": "Enter access interface port (e.g., g1/0/2): ",
        "default_gateway": "Enter default gateway: ",
        "domain_name": "Enter domain name: ",
        "username": "Enter username: ",
        "password": "Enter password: ",
        "ssh_version": "Enter SSH version (1 or 2)(2 is default): ",
        "key_size": "Enter key size (360-4096) (2048 is default): "
    },
    "router": {
        "serial_port": "Enter serial port (e.g., COM4) (COM4 is default): ",
        "hostname": "Enter hostname for the device: ",
        "device_password": "Enter password for the device: ",
        "mgmt_interface_port": "Enter MGMT interface port (e.g., g0/0): ",
        "mgmt_sub_interface_port": "Enter sub-interface port (e.g., g0/0.99): ",
        "mgmt_ipaddress": "Enter IP address for sub interface: ",
        "mgmt_subnetmask": "Enter subnet mask (255.255.255.0 is default): ",
        "mgmt_vlan": "Set the VLAN id for the subinterface (99 is default):",
        "domain_name": "Enter domain name: ",
        "username": "Enter username: ",
        "password": "Enter password: ",
        "ssh_version": "Enter SSH version (1 or 2)(2 is default): ",
        "key_size": "Enter key size (360-4096) (2048 is default): "
    }
}

# Default values (optional)
DEFAULTS = {
    "serial_port": "COM4",
    "mgmt_svi": "99",
    "mgmt_vlan": "99",
    "mgmt_subnetmask": "255.255.255.0",
    "key_size": "2048",
    "ssh_version": "2"
    
}

def get_user_input(device_type="switch"):
    """
    Collect user input for device configuration.
    device_type: "switch" or "router"
    Returns a dictionary with user-provided values.
    """
    variables = {}
    # Uses the .get() function to get the value for the key, and if the key
    # does not exists, it will use the values in DEFAULTS.
    # If no device_type is set, it will run switch configuration.
    prompts = PROMPTS.get(device_type, PROMPTS["switch"])
    
    for key, prompt in prompts.items(): # Gets the key and promt from promps.
        default = DEFAULTS.get(key, "") # Get default value if there is one
        if default:
            user_input = input(f"{prompt}").strip()
            variables[key] = user_input if user_input else default # if user does not write anything, use default
        else:
            variables[key] = input(prompt)
    return variables

if __name__ == "__main__":
    get_user_input()