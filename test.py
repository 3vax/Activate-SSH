prompts = {
    "hostname": "Enter hostname for the device: ",
    "device_password": "Enter enable secret password for the device: ",
    "mgmt_vlan": "Enter VLAN-id for MGMT: ",
    "mgmt_ipaddress": "Enter IP address: ",
    "mgmt_subnetmask": "Enter subnet mask: ",
    "mgmt_interface_port": "Enter interface port (e.g., g1/0/1): ",
    "default_gateway": "Enter default gateway: ",
    "domain_name": "Enter domain name: ",
    "username": "Enter username: ",
    "password": "Enter password: ",
    "ssh_version": "Enter SSH version (1 or 2)(2 is default): ",
    "key_size": "Enter key size (360-4096): "
}

# Collect user input into the variables dictionary
variables = {key: input(prompt) for key, prompt in prompts.items()}

commands = [
    'enable',
    'conf t',
    'enable secret {device_password}',
    'hostname {hostname}',
    'int vlan {mgmt_vlan}',
    'ip address {mgmt_ipaddress} {mgmt_subnetmask}',
    'no shut',
    'exit',
    'int {mgmt_interface_port}',
    'switchport mode access',
    'switchport access vlan {mgmt_vlan}',
    'exit',
    'ip default-gateway {default_gateway}',
    'ip domain-name {domain_name}',
    'username {username} password {password}',
    'crypto key generate rsa modulus {key_size}',
    'ip ssh version {ssh_version}',
    'line vty 0 15',
    'login local',
    'transport input ssh',
    'end'
]


for command in commands:
    formatted_command = command.format(**variables)
    print(formatted_command.encode()) # write a string