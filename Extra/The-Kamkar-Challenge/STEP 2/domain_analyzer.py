import json
import dns.resolver
import re
import concurrent.futures
from urllib.parse import urlparse
from typing import List, Set

def is_valid_domain(domain: str) -> bool:
    """Check if a domain name is syntactically valid."""
    if not domain:
        return False
    
    # Basic domain validation regex
    pattern = r'^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
    
    # Remove any protocol and path
    cleaned = domain.lower().strip()
    if '://' in cleaned:
        cleaned = cleaned.split('://', 1)[1]
    cleaned = cleaned.split('/')[0]
    cleaned = cleaned.split(':')[0]  # Remove port if present
    
    return bool(re.match(pattern, cleaned))

def extract_domain_from_url(url: str) -> str:
    """Extract domain from URL."""
    try:
        parsed = urlparse(url if '://' in url else f'http://{url}')
        return parsed.netloc.split(':')[0].lower()
    except Exception:
        return ''

def resolve_domain(domain: str) -> bool:
    """Check if a domain resolves to an IP address."""
    try:
        dns.resolver.resolve(domain, 'A')
        return True
    except Exception:
        return False

def extract_domains(programs_filename: str) -> List[str]:
    """Extract unique valid domains from the programs file."""
    domains: Set[str] = set()
    
    try:
        with open(programs_filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        for program in data.values():
            # Process direct domains
            if 'domains' in program:
                for domain in program['domains']:
                    if isinstance(domain, str):
                        # Remove wildcard notation if present
                        clean_domain = domain.replace('*.', '').strip()
                        if is_valid_domain(clean_domain):
                            domains.add(clean_domain)
            
            # Process URLs
            if 'urls' in program:
                for url in program['urls']:
                    if isinstance(url, str):
                        domain = extract_domain_from_url(url)
                        if domain and is_valid_domain(domain):
                            domains.add(domain)
            
            # Process wildcards
            if 'wildcards' in program:
                for wildcard in program['wildcards']:
                    if isinstance(wildcard, str):
                        # Remove wildcard notation and any trailing paths
                        clean_domain = wildcard.replace('*.', '').split('/')[0].strip()
                        if is_valid_domain(clean_domain):
                            domains.add(clean_domain)
    
    except Exception as e:
        print(f"Error reading or parsing programs file: {e}")
        return []
    
    return sorted(list(domains))

def check_domains(domains_list: List[str]) -> List[str]:
    """Check which domains are active using parallel processing."""
    active_domains = []
    
    # Use ThreadPoolExecutor for parallel DNS resolution
    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        future_to_domain = {executor.submit(resolve_domain, domain): domain for domain in domains_list}
        
        for future in concurrent.futures.as_completed(future_to_domain):
            domain = future_to_domain[future]
            try:
                is_active = future.result()
                if is_active:
                    active_domains.append(domain)
                    print(f"Active domain found: {domain}")
            except Exception as e:
                print(f"Error checking domain {domain}: {e}")
    
    return sorted(active_domains)

def clean_domains() -> None:
    """Extract domains, check them, and save active ones to file."""
    print("Extracting domains...")
    domains = extract_domains('programs.json')
    print(f"Found {len(domains)} unique valid domains")
    
    print("\nChecking domain activity...")
    active_domains = check_domains(domains)
    print(f"\nFound {len(active_domains)} active domains")
    
    print("\nSaving results to domains.txt...")
    with open('domains.txt', 'w', encoding='utf-8') as f:
        for domain in active_domains:
            f.write(f"{domain}\n")
    
    print("Done!")

def main():
    clean_domains()

if __name__ == "__main__":
    main()