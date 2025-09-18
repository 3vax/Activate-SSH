import serial.tools.list_ports as port_list

def list_serial_ports():
    ports = list(port_list.comports())
    for ports in ports:
        print(ports)


if __name__ == "__main__":
    list_serial_ports()