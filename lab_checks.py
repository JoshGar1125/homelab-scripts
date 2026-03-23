def check_server(is_online):
    if is_online:
        return "Server is online and ready."
    else:
        return "Server is offline. Check your connection."

def storage_check(total_gb, used_gb):
    percentage_available = (used_gb / total_gb) * 100
    if percentage_available <= 50:
        return "Storage is healthy"
    elif 80 >= percentage_available >= 50:
        return "Storage is filling up - consider cleanup"
    else:
        return "WARNING: Storage critically low"
    
def service_status(service_name, port_num):
    if port_num <= 1023:
        return f"{service_name} is running on a standard system port"
    elif 1024 <= port_num <= 8999:
        return f"{service_name} is running on a standard application port"
    else: 
        return f"{service_name} is running on a high port - double check your config"

def lab_readiness():
    print("=== Full report ===")
    print(f"{check_server(True)} \n{storage_check(1000, 56)} \n{service_status('Plex', 32400)} \n{service_status('Immich', 2283)} \n{service_status('Pi-Hole', 80)} \n{service_status('Uptime Kuma', 3001)}")
    print("====================")

print(check_server(True))
print(check_server(False))

print(storage_check(100, 51))

print(service_status("Plex", 32400))

lab_readiness()
