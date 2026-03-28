import datetime
import json

def write_log(message):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("homelab.log", 'a') as f:
        f.write(f"[{timestamp}] {message}\n")

def read_log():
    with open("homelab.log", 'r') as file:
        for index, line in enumerate(file, start=1):
            print(f"{index}: {line.strip()}")

def save_snapshot():
    data={
        "hostname" : "homelab",
        "ip" : "192.168.x.x",
        "services" : ["pihole", "docker"],
        "timestamp" : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    with open("snapshot.json", 'w') as json_file:
        json.dump(data, json_file, indent=4)

def load_snapshot():
    with open("snapshot.json", "r") as json_file:
        data = json.load(json_file)
        print("=== Homelab snapshot ===")
        print("Host:", data["hostname"])
        print("IP:", data["ip"])
        print("Services:", ", ".join(data["services"]))
        print("Captured:", data["timestamp"])
        print("========================")

def parse_blocklist(file_name):
    valid_domains = []

    with open(file_name, 'r') as file:
        for line in file:
            if not line.strip():
                continue
            if line.startswith('#'):
                continue
            valid_domains.append(line.strip())

    count = len(valid_domains)
    first_ten = valid_domains[:10]

    print(f"Valid domains found: {count}")
    print("First 10:")
    for domain in first_ten:
        print(f"  {domain}")

write_log("SSH connection established")
write_log("Docker service started")
write_log("Pi-Hole blocked 8%")

read_log()

save_snapshot()

load_snapshot()

parse_blocklist("testlist.txt")
