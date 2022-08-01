"""This file is included with SystemParser in order to obtain system information
Copyright (C) 2022 AERivas

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

This file contains a dictionary contains keys and values the keys are
just short names for *nix bash commands to be used with the asynchronous

Bash commands in use are: find, sed
More information about bash commands(offline): within a terminal... $> man <command>
More information about bash commands(online): https://ss64.com/bash/
More information about the filesystem: https://www.kernel.org/doc/html/latest/admin-guide/"""


# make a function that handles all of this.think all list values in the first position [1] after find 
# a function that allows for quick add and change of file and or directory
# files that require root user to view iomem, ioports


POSIX_COMMANDS = {
    "cpuinfo": ["find", "/proc/cpuinfo", "-type", "f", "-print0", "-execdir", "sed", "-z", "s/ //g", "{}", "+"],
    "meminfo": ["find", "/proc/meminfo", "-type", "f", "-print0", "-execdir", "sed", "-z", "s/ //g", "{}", "+"],
    "uptime": ["find", "/proc/uptime", "-type", "f", "-print0",  "-execdir", "sed", "-z", "s/^/:/", "{}", "+"],
    # "iomem": ["find", "/proc/iomem", "-type", "f", "-print0", "-execdir", "sed", "-z", "s/^/:/", "{}", "+"],
    # "ioports": ["find", "/proc/ioports", "-type", "f", "-print0", "-execdir", "sed", "-z", "s/^/:/", "{}", "+"],
    "loadavg": ["find", "/proc/loadavg", "-type", "f", "-execdir", "sed", "-z", "s/^/:/", "{}", "+"],
    "modules": ["find", "/proc/modules", "-type", "f", "-execdir", "sed", "-z", "s/\\b /:/g", "{}", "+"],
    "vmstat": ["find", "/proc/vmstat", "-print0", "-execdir", "sed", "-z", "s/ /:/g", "{}", "+"],
    "power": ["find", "/sys/devices/virtual/dmi/id/power/", "-type", "f", "-print0", "-readable", "-execdir", "sed", "s/^/:/", "{}", ";"],
    "network_info4":  ["find", "-L", "/proc/sys/net/ipv4/", "-type", "f", "-print0", "-execdir", "sed", "-z", "s/^/:/", "{}", ";"],
    "network_info6": ["find", "-L", "/proc/sys/net/ipv6/", "-type", "f", "-print0", "-execdir", "sed", "-z", "s/^/:/", "{}", ";"],
    "smbios": ["find", "/sys/devices/virtual/dmi/id","-type", "f", "-readable", "-print0", "-execdir", "sed", "-z", "s/^/:/", "{}", ";"],
    "check_cpu_vuln": ["find", "/sys/devices/system/cpu/vulnerabilities","-type", "f", "-readable", "-print0", "-execdir", "sed", "-z", "s/^/:/", "{}", ";"],
    # "glxinfo": ["glxinfo"],
    # "glxinfoD": ["egrep", "-i", "device|memory"],
    # "env": ["env"]
    }

POSIX_ACCEPTED_ARGS: list[str] = [
    'processor',
    'memory',
    'uptime',
    'loadavg',
    'bios',
    'virtual_memory_statistics',
    'vulnerability_check',
    'network_ip4',
    'network_ip6',
    'driver_modules',
    'power']
