import subprocess

def run_enum4linux(target):
    command = f"enum4linux -a {target}"

    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output = result.stdout.decode()

        shares = []
        users = []

        for line in output.splitlines():
            if "Sharename" in line:
                shares.append(line)
            if "User:" in line:
                users.append(line.split(":")[1].strip())
        
        return {"Shares": shares, "Users": users}

    except subprocess.CalledProcessError as e:
        print(f"Error running enum4linux: {e.stderr.decode()}")


