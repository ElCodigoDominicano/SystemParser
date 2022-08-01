# SystemParser_0.1.0

A simple system information gathering tool written in python, displays a medley of<br>
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

#### List of available arguements for Nix systems: bios, processor, network4, network6, memory, drivers, check_vuln, power
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
#### List of available arguements for Windows systems: bus, processor, network, memory, drivers, sound, floppy, ide,
#### pcmcia, usb_hub, usb_controller, usb_controller_device, parallel, serial_port, serial_port_settings.
```markdown
$> py SystemParser <*arguement*>
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
