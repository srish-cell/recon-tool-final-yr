import subprocess

def nmapscan(target):
    command = f"nmap -A -T4 {target}"  # -A includes OS detection, version detection, script scanning, and traceroute
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return result.stdout.decode()
    except subprocess.CalledProcessError as e:
        return e.stderr.decode()
