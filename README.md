# SystemParser_0.2.0

A simple tool used to display various system information
written in python using the asyncio library and other built-in libraries,<br>

Information reported by the systems environment(ex. Windows, Nix, MACOS)<br> 
such as..
- hardware information (>processor vulnerability check for Linux machines)
- network information
- audio information
- usb device information
- bios information
- motherboard information
- and more 

# Nix
First(The only requirement): download python and install it (preferably v3.8+)<br>
Second: 
```markdown
cd ~/Desktop
git clone https://github.com/SolFox/SystemParser
```

#### List of available arguments for Nix systems: 
processor, memory, uptime, load_average, driver_modules, 
virtual_memory_statistics, modules_drivers, power, uptime, 
load_average, network_ip4, network_ip6, bios, vulnerability_check

```markdown
$> python SystemParser network_ip4
```
Above will have the program go into the directory /proc/sys/net/ipv4 and display all values found in each file,<br>
(in this case the ipv4 setting/configuration) and does the same for every subdirectory within it.

```markdown
...
...
...
|_-~> ipv4 conf docker0 accept_local: 0
|_-~> ipv4 conf docker0 accept_redirects: 1
|_-~> ipv4 conf docker0 accept_source_route: 0
|_-~> ipv4 conf docker0 arp_accept: 0
|_-~> ipv4 conf docker0 arp_announce: 0
|_-~> ipv4 conf docker0 arp_evict_nocarrier: 1
|_-~> ipv4 conf docker0 arp_filter: 0
|_-~> ipv4 conf docker0 arp_ignore: 0
|_-~> ipv4 conf docker0 arp_notify: 0
|_-~> ipv4 conf docker0 bc_forwarding: 0
|_-~> ipv4 conf docker0 bootp_relay: 0
|_-~> ipv4 conf docker0 disable_policy: 0
|_-~> ipv4 conf docker0 disable_xfrm: 0
|_-~> ipv4 conf docker0 drop_gratuitous_arp: 0
|_-~> ipv4 conf docker0 drop_unicast_in_l2_multicast: 0
|_-~> ipv4 conf docker0 force_igmp_version: 0
|_-~> ipv4 conf docker0 forwarding: 1
|_-~> ipv4 conf docker0 igmpv2_unsolicited_report_interval: 10000
|_-~> ipv4 conf docker0 igmpv3_unsolicited_report_interval: 1000
|_-~> ipv4 conf docker0 ignore_routes_with_linkdown: 0
|_-~> ipv4 conf docker0 log_martians: 0
|_-~> ipv4 conf docker0 mc_forwarding: 0
|_-~> ipv4 conf docker0 medium_id: 0
|_-~> ipv4 conf docker0 promote_secondaries: 1
|_-~> ipv4 conf docker0 proxy_arp: 0
|_-~> ipv4 conf docker0 proxy_arp_pvlan: 0
|_-~> ipv4 conf docker0 route_localnet: 0
|_-~> ipv4 conf docker0 rp_filter: 2
...
...
...
```

# Windows
#### List of available arguments for Windows systems:
bus, motherboard, processor, memory, sound_device, floppy_controller, ide_controller,
pcmcia_controller, parallel_port, usb_hub, usb_controller, usb_controller_device,
serial_port, serial_port_settings, serial_port_configurations, list_environment_variables,
video_controller, video_settings, video_configurations

```markdown
$> py SystemParser processor
...
```
Will give you information about your processor
```
...
|_-~> Caption: AMD64 Family 23 Model 96 Stepping 1
|_-~> DeviceID: CPU0
|_-~> Manufacturer: AuthenticAMD
|_-~> MaxClockSpeed: 2371
|_-~> Name: AMD Ryzen 5 4500U with Radeon Graphics
|_-~> SocketDesignation:
...
```

# OSX
```markdown
$> *information about usage here*
```

### Work in progress
OSX not implemented, yet.

### Support or Contact
Email: py_devops3@proton.me
