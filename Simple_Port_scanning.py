import socket

def scan_ports(target, start_port, end_port):
    open_ports = []

    print(f"Scanning ports on {target}...\n")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        try:
            sock.connect((target, port))
            open_ports.append(port)
            print(f"Port {port} is open.")
        except (socket.timeout, socket.error):
            # Connection attempt timed out or failed
            pass
        finally:
            sock.close()

    print("\nScan completed.")
    return open_ports

if __name__ == "__main__":
    target_host = input("Enter target host: ")
    start_port = int(input("Enter start port: "))
    end_port = int(input("Enter end port: "))

    open_ports = scan_ports(target_host, start_port, end_port)

    if open_ports:
        print("\nOpen ports:", open_ports)
    else:
        print("\nNo open ports found.")
