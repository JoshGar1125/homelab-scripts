import subprocess
from datetime import datetime

def get_system_info():
    t_line = []
    parts = []
    disk_parts = []
    name = subprocess.run(['hostname'], capture_output=True, text=True).stdout.strip()
    timeup = subprocess.run(['uptime'], capture_output=True, text=True).stdout.strip()
    timeup_lines = timeup.split("up")[1].split(",")[0]
    timeup_lines_2 = timeup.split("up")[1].split(",")[1]
    nproc_out = subprocess.run(['nproc'], capture_output=True, text=True).stdout.strip()
    ram = subprocess.run(['free', '-h'], capture_output=True, text=True).stdout.strip()
    lines = ram.split("\n")
    for line in lines:
        if line.startswith("Mem:"):
            parts = line.split()
    
    disk = subprocess.run(['df', '-h', '/'], capture_output=True, text=True).stdout.strip()
    disk_lines = disk.split("\n")
    for disk_line in disk_lines:
        if disk_line.startswith("/"):
            disk_parts = disk_line.split()

    print("=== System Info ===")
    print(f"Hostname:   {name}")
    print(f"Uptime:     up{timeup_lines},{timeup_lines_2}")
    print(f"CPU cores:  {nproc_out}")
    print(f"Ram total:  {parts[1]}")
    print(f"Ram used:   {parts[2]}")
    print(f"Disk total: {disk_parts[1]}")
    print(f"Disk used:  {disk_parts[2]}")
    print("========================")

def get_containers():
    docker_stats = subprocess.run(['docker', 'ps', '--format', '{{.Names}}\t{{.Status}}'], capture_output=True, text=True).stdout.strip()
    
    docker_split = docker_stats.split("\n")

    print("=== Running Containers ===")
    for line in docker_split:
        parts = line.split("\t")
        print(f"{parts[0]:<25} {parts[1]}")
    print("===========================")

def check_storage():
    os_storage = subprocess.run(['df', '-h', '/'], capture_output=True, text=True).stdout.strip()
    os_storage_split = os_storage.split("\n")
    for line in os_storage_split:
        if line.startswith("/dev"):
            parts = line.split()
    total_storage = parts[1]
    used_storage = parts[2]
    avail_storage = parts[3]

    media_storage = subprocess.run(['df', '-h', '/mnt/external'], capture_output=True, text=True).stdout.strip()
    media_storage_split = media_storage.split("\n")
    for line in media_storage_split:
        if line.startswith("/dev"):
            media_parts = line.split()
    total_m_storage = media_parts[1]
    used_m_storage = media_parts[2]
    avail_m_storage = media_parts[3]

    movie_storage = subprocess.run(['du', '-sh', '/mnt/external/movies'], capture_output=True, text=True).stdout.strip()
    movie_split = movie_storage.split("\n")
    for line in movie_split:
        movie_parts = line.split()
    used_movie_storage = movie_parts[0]

    tv_storage = subprocess.run(['du', '-sh', '/mnt/external/tv'], capture_output=True, text=True).stdout.strip()
    tv_split = tv_storage.split("\n")
    for line in tv_split:
        tv_parts = line.split()
    used_tv_storage = tv_parts[0]

    down_storage = subprocess.run(['du', '-sh', '/mnt/external/downloads'], capture_output=True, text=True).stdout.strip()
    down_split = down_storage.split("\n")
    for line in down_split:
        down_parts = line.split()
    used_down_storage = down_parts[0]
    
    print("=== Storage ===")
    print("--- OS Drive ---")
    print(f"Total: {total_storage}  Used: {used_storage}  Free: {avail_storage}\n")
    print("--- Media Drive (/mnt/external) ---")
    print(f"Total: {total_m_storage}  Used: {used_m_storage}  Free: {avail_m_storage}\n")
    print("--- Media Folders ---")
    print(f"movies/:    {used_movie_storage}")
    print(f"tv/:        {used_tv_storage}")
    print(f"downloads/: {used_down_storage}")
    print("==================")

def check_port(port):
    used_port = subprocess.run(['ss', '-tulnp'], capture_output=True, text=True).stdout.strip()
    lines = used_port.split("\n")
    in_use = False
    for line in lines:
        if "LISTEN" in line and f":{port} " in line:
            in_use = True
    if in_use:
        print(f"Port {port}: IN USE")
    else:
        print(f"Port {port}: FREE")

def homelab_health():
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("======== Homelab Health Check =========")
    print(timestamp)

    get_system_info()
    get_containers()
    check_storage()
    print("--- Key Ports ---")
    check_port(32400)  # Plex
    check_port(8181)   # SABnzbd
    check_port(7878)   # Radarr
    check_port(8989)   # Sonarr
    check_port(9696)   # Prowlarr
    check_port(5055)   # Overseerr
    check_port(2283)   # Immich
    check_port(9999)   # test — should show FREE
    print("========================================")

homelab_health()
