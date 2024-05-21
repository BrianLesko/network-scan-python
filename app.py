# Brian Lesko
# 4/9/2024 
# Scan your local wifi network and display the devices that are connected to it.

import subprocess
import re
import netifaces

def get_ip_address():
    #Retrieve the local IP address of the computer on macOS.
    #:return: str - The IP address, or a message if not found.
    result = subprocess.run("ifconfig", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    interfaces = ['en0', 'en1', 'en2', 'en3', 'en4', 'en5']
    for interface in interfaces:
        match = re.search(rf'{interface}:.*?inet (\d+\.\d+\.\d+\.\d+)', result.stdout, re.DOTALL)
        if match:
            return match.group(1)
    return "No external IP address found."

import subprocess
import re

def get_subnet_mask(interface='en0'):
    addrs = netifaces.ifaddresses(interface)
    return addrs[netifaces.AF_INET][0]['netmask']

subnet_mask = get_subnet_mask()
print(f"Subnet Mask: {subnet_mask}")

ip_address = get_ip_address()
print(f"IP address: {ip_address}")

def calculate_broadcast_address(ip, subnet):
    #Calculate the broadcast address from an IP address and subnet mask.
    ip_binary = ''.join(format(int(octet), '08b') for octet in ip.split('.'))
    subnet_binary = ''.join(format(int(octet), '08b') for octet in subnet.split('.'))
    broadcast_binary = ''.join(ip_bit if subnet_bit == '1' else '1' 
                               for ip_bit, subnet_bit in zip(ip_binary, subnet_binary))
    broadcast_address = '.'.join(str(int(broadcast_binary[i:i + 8], 2)) for i in range(0, 32, 8))
    return broadcast_address

broadcast_address = calculate_broadcast_address(ip_address, subnet_mask)
print(f"Broadcast Address: {broadcast_address}")

def ping_broadcast(address, timeout):
    #Pings the specified address with a timeout.
    try:
        return subprocess.check_output(['ping', '-c', '3', address], text=True, timeout=timeout)
    except subprocess.TimeoutExpired:
        return f"Timeout after {timeout} seconds."
    except subprocess.CalledProcessError:
        return "Ping failed."

print(ping_broadcast(broadcast_address, 5))

def get_arp_table():
    try:
        arp_output = subprocess.check_output(['arp', '-a'], text=True)
        return [line for line in arp_output.splitlines() if 'permanent' not in line]
    except subprocess.CalledProcessError:
        return []


for line in get_arp_table():
    try:
        match = re.search(r'(\?\S*) \(([\d\.]+)\) at ([\w:]+) on (\w+)', line)
        if match:
            hostname, ipv4, mac, interface = match.groups()
            # Replace '?' with a placeholder if hostname is not available
            hostname = hostname if hostname != '?' else 'N/A'
            print(f"{ipv4} is assigned to {mac}, has name {hostname}, on the {interface} network")
            
        else:
            print("Line could not be parsed:", line)
    except Exception as e:
        print("Error parsing line:", line, e)
    