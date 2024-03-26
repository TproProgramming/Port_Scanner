import socket

def port_scan(target_host, port_range):
    for port in range(port_range[0], port_range[1] + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target_host, port))
        if result == 0:
            print(f"Port {port} is open")
        sock.close()


def main():
    #Ask user for target host. Need to add input validation in future implementations
    target_host=input("Input target host IP address. Example: 10.0.12.123\n")

    #Ask user for port range
    port_max=input("How many ports do you want to be scanned? Enter a number from 1 to 65,535.\n")
    port_max = int(port_max)
    port_range = (1, port_max)
    port_scan(target_host, port_range)
    
    print("\nPort Scanning is Complete.")

if __name__ == "__main__":
    main()