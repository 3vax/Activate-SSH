from scripts.cisco_switch_settings import cisco_switch_settings
import tools.list_ports
import scripts
import time

run = True

while run:
    print(f'''
What would you like to do?
1. Check what COM ports are available.
2. Switch
3. Router
Enter the number of what you would like to do:''')
    switch_or_router = input()

    if switch_or_router == "1":
        tools.list_ports.list_serial_ports()
        time.sleep(3)


    elif switch_or_router == "2":
        cisco_switch_settings()

    elif switch_or_router == "3":
        pass

    else:
        run = False
