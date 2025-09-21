from scripts.cisco_settings import cisco_settings
import tools.list_ports
import scripts
import time

run = True

while run:
    '''
    This is the main script, it will print out different options for the user.
    Based on the users choice it will show available ports on the computer,
    or run the cisco_settings script with values for either a switch or router.
    '''
    print(f'''
What would you like to do?
[1] Check what COM ports are available.
[2] Switch
[3] Router
Or press enter to quit...
Enter the number of what you would like to do:''')
    switch_or_router = input()

    if switch_or_router == "1":
        tools.list_ports.list_serial_ports()
        time.sleep(3)


    elif switch_or_router == "2":
        cisco_settings("switch")

    elif switch_or_router == "3":
        cisco_settings("router")

    else:
        run = False
