import subprocess
import shodan
import socket
API_KEY = 'EHZGgmpZzkyCMp5BOg5Ij3AqyZ0VegU5'

cmd=f"shodan init {API_KEY}"
def resolve_domain(domain):
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        print(f"Error: Unable to resolve domain {domain}")
        return None

def lookup_host(ips):
    
    try:
        command = f"shodan host {ips}"
        subprocess.run(cmd, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode()

        
    except subprocess.CalledProcessError as e:
        return e.stderr.decode()

