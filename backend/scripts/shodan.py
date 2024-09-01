import subprocess
import shodan
import socket
API_KEY = 'cNKl3a6MYaHsDVgz4TWmyJVQLja3yiha'

api = shodan.Shodan(API_KEY)

def resolve_domain(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        print(f"Error: Unable to resolve domain {domain}")
        return None

def lookup_host(ip):
    try:
        if isinstance(ips, str):  # Handle a single IP as a string
            ips = [ips]
        elif not isinstance(ips, (list, tuple)):  # If it's not a list or tuple, raise an error
            raise ValueError("IP must be a string or a list/tuple of strings")

        host=self._request('/shodan/host/{}'.format(','.join(ips)), params)

        print(f"IP: {host['ip_str']}")
        print(f"Organization: {host.get('org', 'N/A')}")
        print(f"Operating System: {host.get('os', 'N/A')}")

        for item in host['data']:
            print(f"\nPort: {item['port']}")
            print(f"Banner: {item['data']}")
        
        if 'vulns' in host:
            print("\nVulnerabilities:")
            for vuln in host['vulns']:
                print(f"CVE: {vuln.replace('!', '')}")
        return host       
    except shodan.APIError as e:
        print(f"Error: {e}")
        return e

