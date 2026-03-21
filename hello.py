import os
import socket

hostname = socket.gethostname()
user = os.getenv("USER")

print(f"Hello from {user} on {hostname}")
print("Home lab is alive.")