def storage_remaining(total_gb, used_gb):
    try:
        available_storage = total_gb - used_gb
        percentage_available = (used_gb / total_gb) * 100
        return f"Storage remaining: {available_storage}GB ({percentage_available:.2f}% used)" 
    except ZeroDivisionError:
        return "Error: total storage cannot be zero"
    except TypeError:
        return "Error: storage values must be numbers"

def get_device_info(devices, device_name):
    for device in devices:
        name = device["name"]
        role = device["role"]
        storage = device["storage_gb"]
        
        if device_name == name:
            return f"{name} - {role} - {storage}GB"

    else:        
        return f"Device '{device_name}' not found in lab inventory"

def validate_port(port_number):
    
    if isinstance(port_number, str):
        return "wrong type - 'Error: port must be a number'"
    elif isinstance(port_number, float):
        return "decimal - 'Error: port must be a whole number'"
    elif isinstance(port_number, int):
        if 1 <= port_number <= 65535:
            return f"valid - 'Port {port_number} is valid'"
        else:
            return f"out of range -  'Port {port_number} is out of valid range (1-65535)'"
    else:
        return "Error: invalid input"

def read_config(filename):
    try:
        with open(filename, "r") as f:
            contents = f.read()
            print(contents)
    except FileNotFoundError:
        print(f"{filename} not found")
    except PermissionError:
        print(f"{filename} permission denied")

print(storage_remaining(2, 1))
print(storage_remaining(0, 7))
print(storage_remaining("big", 1))

lab_devices = [
    {"name": "Spare PC", "role": "Home lab server", "storage_gb": 1000},
    {"name": "Dell Precision", "role": "Primary workstation", "storage_gb": 500},
    {"name": "Asus Laptop", "role": "Kali machine", "storage_gb": 256},
]

print(get_device_info(lab_devices, "Dell h"))

print(validate_port(80))
print(validate_port(99999))
print(validate_port("http"))
print(validate_port(3.14))

read_config("homelab.conf")
read_config("/etc/shadow")     
read_config("/etc/hostname")