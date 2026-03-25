def startup_sequence(number):
    while number >= 1:
        print(f"Starting in {number}...")
        number -= 1
    print("Homelab is online.")

def total_storage(devices):
    total_gb = 0
    count = len(devices)
    for i in devices:
        total_gb += i["storage_gb"]
    print(f"Total lab storage: {total_gb}GB across {count} devices")

devices = [
    {"name": "Dell Precision 5560", "role":"Primary workstation", "status": True},
    {"name": "Spare PC", "role":"Home lab server", "status": True},
    {"name": "Lenovo Yoga C930", "role":"Kali machine", "status": False}
]

for device in devices:
    name = device["name"]
    role = device["role"]
    if device["status"]:
        stat = "Online"
    else:
        stat = "Offline"
    print(f"{name} - {role} - {stat}")

services = [
    {"name": "Pi-hole", "port": 80},
    {"name": "Immich", "port": 2283},
    {"name": "Plex", "port": 32400},
    {"name": "Nextcloud", "port": 8080},
    {"name": "Vaultwarden", "port": 8081},
    {"name": "Uptime Kuma", "port": 3001},
]

for service in services:
    name = service["name"]
    port = service["port"]
    url = f"http://192.168.1.110:{port}"

    if port <= 1023:
        port_type = "system port"
    elif port <= 8999:
        port_type = "application port"
    else:
        port_type = "high port"

    print(f"{name:15s}  port {port} ({port_type}) -> {url}")

startup_sequence(5)

lab_devices = [
    {"name": "Spare PC", "storage_gb": 1000},
    {"name": "Dell Precision", "storage_gb": 500},
    {"name": "Asus Laptop", "storage_gb": 256},
]

total_storage(lab_devices)


