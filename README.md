# SystemParser_0.1.0

A simple system information gathering tool written in python using the asyncio library, displays a medley of<br>
system information reported by the systems environment(ex. Windows, Nix, MACOS)<br> 
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
processor, bios, virtual_memory_statistics, vulnerability_check, network_info4, network_info6,
modules_drivers, power, uptime, load_average

```markdown
$> python SystemParser network4
```
Above will have the program go into the directory /proc/sys/net/ipv4 and display all values found for each file,<br>
(in this case the ipv4 setting/configuration) and does the same for every subdirectory within it.

```markdown
cipso_cache_bucket_size =>               10              
cipso_cache_enable   =>               1               
cipso_rbm_optfmt     =>               0               
cipso_rbm_strictvalid =>               1               
accept_local         =>               0               
accept_redirects     =>               1               
accept_source_route  =>               0               
arp_accept           =>               0               
arp_announce         =>               0               
arp_filter           =>               0               
arp_ignore           =>               0               
arp_notify           =>               0               
bc_forwarding        =>               0               
bootp_relay          =>               0               
disable_policy       =>               0               
disable_xfrm         =>               0
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
$> py SystemParser <*argument*>
```

# OSX
```markdown
$> *information about usage here*
```

### Work in progress
hint: It works and it's an ongoing progress
OSX not implemented, yet.

### Support or Contact
Email: py_devops3@proton.me
