import socket
from _datetime import datetime


target = input("Enter the target IP address: ")

def port_scan(target):
    try:
        ip = socket.gethostbyname(target)
        print(f"Scanning the target {ip}")
        print("Time started:", datetime.now())

        for port in range(20,8081):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((ip, port))
            if result == 0:
                print("Port {}: Open".format(port))
            sock.close
        
    except socket.gaierror:
        print("Hostname could not be resolved")

    except socket.error:
        print("Could not connect to the server")

port_scan(target)