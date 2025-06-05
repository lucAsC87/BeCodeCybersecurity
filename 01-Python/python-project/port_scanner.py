"""A simple port scanner"""

from datetime import datetime
import logging
import re
import socket
import time

# === CONFIGURATION ===
try:
    HOST_NAME = socket.gethostname()  # Machine name
    TARGET_HOST = socket.gethostbyname(HOST_NAME)  # Machine IP Address
except socket.gaierror:
    print("Not possible to find the host name")
    TARGET_HOST = "127.0.1.1"
PORT_RANGE = range(1, 65536)
SCAN_DELAY = 0.1  # seconds between scans (rate limiting)

# === LOGGING SETUP ===
logging.basicConfig(
    filename="port_scan.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def validate(ip: str) -> bool:
    """Check if the user's input is a valid IPV4 address."""
    check_ip = ip.split(".")
    for part in check_ip:
        try:
            int(part)
        except ValueError:
            return False
        if int(part) > 255:
            return False
    pattern = r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
    if re.search(pattern, ip):
        return True
    return False


def is_port_open(host: str, port: int, timeout=0.1) -> bool:
    """Try to connect to a port and check if it's open."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        try:
            sock.connect((host, port))
            return True
        except (socket.timeout, ConnectionRefusedError, OSError):
            return False


def scan_ports(host: str, port_range: range) -> list:
    """Scan for local ports and add the open ones to a list."""
    ports = []
    print(
        f"Scanning host {host} from port {port_range.start} to {port_range.stop - 1}..."
    )
    logging.info(f"Started scanning {host}")

    start_time = datetime.now()
    last_print_time = time.time()

    for port in port_range:
        if is_port_open(host, port):
            print(f"[+] Port {port} is open.")
            logging.info(f"Port {port} is open")
            ports.append(port)
        if time.time() - last_print_time >= 30:
            print("Still scanning...")
            last_print_time = time.time()
        time.sleep(SCAN_DELAY)  # Rate limiting

    end_time = datetime.now()
    duration = end_time - start_time
    print(f"Scan completed in {duration}.")
    logging.info(f"Scan finished in {duration}")
    return ports


if __name__ == "__main__":
    while True:
        user_choice = input(
            "On which host would you scan ports? Choose L(ocal) or R(emote)\n"
        )
        if user_choice == "L":
            break
        if user_choice == "R":
            user_ip = input("Insert a valid IP address: ")
            if validate(user_ip):
                TARGET_HOST = user_ip
                break
            print("Not a valid IP address.")
            exit()
        else:
            continue
    try:
        open_ports = scan_ports(TARGET_HOST, PORT_RANGE)
        if not open_ports:
            print("No open ports found.")
            logging.info("No open ports found.")
        else:
            print("Open ports:", open_ports)
    except KeyboardInterrupt:
        print("\n[!] Scan interrupted by user.")
        logging.warning("Scan interrupted by user")
    except socket.gaierror:
        print("[!] Hostname could not be resolved.")
        logging.error("Hostname resolution failed")
    except Exception as e:
        print(f"[!] Unexpected error: {e}")
        logging.exception("Unexpected error occurred")
