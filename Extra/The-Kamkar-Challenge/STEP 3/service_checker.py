import socket
import concurrent.futures
from typing import List
import ssl

def check_port(domain: str, port: int, timeout: int = 3) -> bool:
    """Try to connect to a specific port on a domain."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((domain, port))
        sock.close()
        return result == 0
    except (socket.gaierror, socket.timeout, ConnectionRefusedError):
        return False

def check_https(domain: str, port: int = 443, timeout: int = 3) -> bool:
    """Check if HTTPS is available on the domain."""
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, port), timeout=timeout) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                return ssock.version() is not None
    except (socket.gaierror, socket.timeout, ssl.SSLError, ConnectionRefusedError):
        return False

def load_domains(filename: str) -> List[str]:
    """Load domains from a file."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"Error reading domains file: {e}")
        return []

def http_check(domains: List[str], port: int = 80) -> List[str]:
    """Find active HTTP servers."""
    active = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        future_to_domain = {
            executor.submit(check_port, domain, port): domain 
            for domain in domains
        }
        
        for future in concurrent.futures.as_completed(future_to_domain):
            domain = future_to_domain[future]
            try:
                if future.result():
                    print(f"Found active HTTP: {domain}")
                    active.append(domain)
            except Exception as e:
                print(f"Error checking HTTP for {domain}: {e}")
    
    return active

def https_check(domains: List[str], port: int = 443) -> List[str]:
    """Find active HTTPS servers."""
    active = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        future_to_domain = {
            executor.submit(check_https, domain, port): domain 
            for domain in domains
        }
        
        for future in concurrent.futures.as_completed(future_to_domain):
            domain = future_to_domain[future]
            try:
                if future.result():
                    print(f"Found active HTTPS: {domain}")
                    active.append(domain)
            except Exception as e:
                print(f"Error checking HTTPS for {domain}: {e}")
    
    return active

def ssh_check(domains: List[str], port: int = 22) -> List[str]:
    """Find active SSH servers."""
    active = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        future_to_domain = {
            executor.submit(check_port, domain, port): domain 
            for domain in domains
        }
        
        for future in concurrent.futures.as_completed(future_to_domain):
            domain = future_to_domain[future]
            try:
                if future.result():
                    print(f"Found active SSH: {domain}")
                    active.append(domain)
            except Exception as e:
                print(f"Error checking SSH for {domain}: {e}")
    
    return active

def save_results(filename: str, domains: List[str]) -> None:
    """Save results to a file."""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            for domain in sorted(domains):
                f.write(f"{domain}\n")
        print(f"Results saved to {filename}")
    except Exception as e:
        print(f"Error saving results to {filename}: {e}")

def main():
    print("Loading domains...")
    domains = load_domains('domains.txt')
    if not domains:
        print("No domains found!")
        return

    print(f"\nChecking {len(domains)} domains for HTTP...")
    http_active = http_check(domains)
    save_results('http.txt', http_active)
    
    print(f"\nChecking {len(domains)} domains for HTTPS...")
    https_active = https_check(domains)
    save_results('https.txt', https_active)
    
    print(f"\nChecking {len(domains)} domains for SSH...")
    ssh_active = ssh_check(domains)
    save_results('ssh.txt', ssh_active)
    
    print("\nScan complete!")
    print(f"Found {len(http_active)} HTTP servers")
    print(f"Found {len(https_active)} HTTPS servers")
    print(f"Found {len(ssh_active)} SSH servers")

if __name__ == "__main__":
    main()