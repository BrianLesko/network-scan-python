
# Network Scan using Python

Discover other devices on your network using this simple script written in python. More specifically, this code pings the broadcast address of your network, waits for devices to respond, and then prints the responses. 

## How it works
  The Internet Protocol (IP) suite is a set of rules governing how computers communicate over networks. A local network consists of interconnected computers and devices, like those connected via home WiFi or office Ethernet cables. The network's router manages the allocation of IP addresses within a specified range and assigns an IP address to each device. IP addresses can change when a device connects to a different network or even periodically on the same network due to Dynamic Host Configuration Protocol (DHCP).

On local networks, devices use the Address Resolution Protocol (ARP) to associate each IP address with a corresponding physical hardware address (MAC address). This association is stored in a device’s ARP table, which logs the IP addresses of computers it has recently communicated with and their corresponding MAC addresses. Before sending data, a device checks its ARP table to find the MAC address associated with the desired IP address. If the address isn't already in the ARP table, the device broadcasts an ARP request to all devices on the network. This request asks, "Who has this IP address?" The device with the matching IP address responds with its MAC address, which is then stored in the ARP table for future communications. Therefore, the arp table cannot be trusted to be an accurate record of all the devices on a network.

There exists a way to force update the ARP table, by telling your device to broadcast to the entire local network, turning the ARP table into an up to date record of all the devices on your network. The broadcast address is a special address that targets all devices on the network. It is used to send messages simultaneously to every device within a network segment.

&nbsp;

## Software Dependencies

This code uses the following libraries:
- `netifaces`: for retrieving the subnet

&nbsp;

## Hardware Dependencies
- `An Apple or Mac Computer`

The code written here uses network interfaces specific to my personal computer, which happens to be from Apple. The code is untested on other devices.

## Usage
```
pip install netifaces
python app.py
```

&nbsp;

## Topics 
```
Python | Internet IP 
Mechanical and Robotics engineer
```
&nbsp;

<hr>

&nbsp;

<div align="center">



╭━━╮╭━━━┳━━┳━━━┳━╮╱╭╮        ╭╮╱╱╭━━━┳━━━┳╮╭━┳━━━╮
┃╭╮┃┃╭━╮┣┫┣┫╭━╮┃┃╰╮┃┃        ┃┃╱╱┃╭━━┫╭━╮┃┃┃╭┫╭━╮┃
┃╰╯╰┫╰━╯┃┃┃┃┃╱┃┃╭╮╰╯┃        ┃┃╱╱┃╰━━┫╰━━┫╰╯╯┃┃╱┃┃
┃╭━╮┃╭╮╭╯┃┃┃╰━╯┃┃╰╮┃┃        ┃┃╱╭┫╭━━┻━━╮┃╭╮┃┃┃╱┃┃
┃╰━╯┃┃┃╰┳┫┣┫╭━╮┃┃╱┃┃┃        ┃╰━╯┃╰━━┫╰━╯┃┃┃╰┫╰━╯┃
╰━━━┻╯╰━┻━━┻╯╱╰┻╯╱╰━╯        ╰━━━┻━━━┻━━━┻╯╰━┻━━━╯
  


&nbsp;


<a href="https://twitter.com/BrianJosephLeko"><img src="https://raw.githubusercontent.com/BrianLesko/BrianLesko/f7be693250033b9d28c2224c9c1042bb6859bfe9/.socials/svg-white/x-logo-white.svg" width="30" alt="X Logo"></a> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <a href="https://github.com/BrianLesko"><img src="https://raw.githubusercontent.com/BrianLesko/BrianLesko/f7be693250033b9d28c2224c9c1042bb6859bfe9/.socials/svg-white/github-mark-white.svg" width="30" alt="GitHub"></a> &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; <a href="https://www.linkedin.com/in/brianlesko/"><img src="https://raw.githubusercontent.com/BrianLesko/BrianLesko/f7be693250033b9d28c2224c9c1042bb6859bfe9/.socials/svg-white/linkedin-icon-white.svg" width="30" alt="LinkedIn"></a>

follow all of these for pizza :)

</div>


&nbsp;


