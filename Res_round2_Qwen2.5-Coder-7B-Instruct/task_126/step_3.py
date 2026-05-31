import subprocess

# Try pinging the domain to check connectivity
def ping_domain(domain):
    try:
        output = subprocess.check_output(['ping', '-c', '1', domain], stderr=subprocess.STDOUT)
        return True
    except subprocess.CalledProcessError as e:
        print(e.output.decode())
        return False

domain = "www.boredapi.com"
if ping_domain(domain):
    print(f"Ping to {domain} successful.")
else:
    print(f"Ping to {domain} failed. Please check your network connection.")