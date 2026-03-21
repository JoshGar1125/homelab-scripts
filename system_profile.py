server_hostname = "homelab"
server_username = "ghost"
num_of_services = 5
server_status = True

def describe_device(name, role, os):
    return f"Device name: {name} - Role: {role} - OS: {os}"

def storage_remaining(total_gb, used_gb):
    available_storage = total_gb - used_gb
    percentage_available = (used_gb / total_gb) * 100
    return f"Storage remaining: {available_storage}GB ({percentage_available:.2f}% used)" 

def lab_status():
    print(f"=== Home Lab Status === \nServer: {server_hostname} | User: {server_username} | Online: {server_status} \nDevices: 3 configured \n{storage_remaining(1000, 7)} ")

print(f"Server: {server_hostname} | User: {server_username} | Planned services: {num_of_services} | Online: {server_status}")

main_device = describe_device("Dell Precision 5560", "Main workstation", "Windows 11")
print(main_device)
spare_pc = describe_device("Spare Linux Server", "Home lab server", "Ubuntu server 24.04")
print(spare_pc)
kali_linux = describe_device("Asus laptop", "Kali linux hacking machine", "Pending")
print(kali_linux)

print(storage_remaining(1000, 7))

lab_status()