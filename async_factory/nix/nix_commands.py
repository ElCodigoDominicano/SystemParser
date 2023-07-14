"""This file is included with SystemParser in order 
Copyright (C) 2022 AERivas

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

This file contains a tuple containing strings which are the programs acceptable arguments
a dictionary that contains keys as those strings and values are
tuples containing strings with the approved command.

Bash commands in use are: find, sed
More information about bash commands(offline): within a terminal... $> man <command>
More information about bash commands(online): https://ss64.com/bash/
More information about the filesystem: https://www.kernel.org/doc/html/latest/admin-guide/"""


POSIX_COMMANDS: dict[str, tuple[str, ...]] = {
    'processor': (
        "find", 
        "/proc/cpuinfo", 
        "-type", 
        "f", 
        "-print0", 
        "-execdir", 
        "sed", 
        "-z", 
        "s/ //g", 
        "{}", 
        "+"
    ),
    'memory': (
        "find", 
        "/proc/meminfo", 
        "-type", 
        "f", 
        "-print0", 
        "-execdir", 
        "sed", 
        "-z", 
        "s/ //g", 
        "{}", 
        "+"
    ),
    'uptime': (
        "find", 
        "/proc/uptime", 
        "-type", 
        "f", 
        "-print0", 
        "-execdir", 
        "sed", 
        "-z", 
        "s/^/:/", 
        "{}", 
        "+"
    ),
    'load_average': (
        "find", 
        "/proc/loadavg", 
        "-type", 
        "f", 
        "-execdir", 
        "sed", 
        "-z", 
        "s/^/:/", 
        "{}", 
        "+"
    ),
    'driver_modules': (
        "find", 
        "/proc/modules", 
        "-type", 
        "f",
        "-execdir", 
        "sed", 
        "-z", 
        "s/\\b /:/g", 
        "{}", 
        "+"
    ),
    'virtual_memory_statistics': (
        "find", 
        "/proc/vmstat", 
        "-print0", 
        "-execdir", 
        "sed", 
        "-z", 
        "s/ /:/g", 
        "{}", 
        "+"
    ),
    'power': (
        "find", 
        "/sys/devices/virtual/dmi/id/power/", 
        "-type", 
        "f", 
        "-print0", 
        "-readable", 
        "-execdir", 
        "sed", 
        "s/^/:/", 
        "{}", 
        ";"
    ),
    'network_ip4': (
        "find", 
        "-L", 
        "/proc/sys/net/ipv4/", 
        "-type", 
        "f", 
        "-print0", 
        "-execdir", 
        "sed", 
        "-z", 
        "s/^/:/", 
        "{}", 
        ";"
    ),
    'network_ip6': (
        "find",
        "-L", 
        "/proc/sys/net/ipv6/", 
        "-type", 
        "f", 
        "-print0", 
        "-execdir", 
        "sed", 
        "-z", 
        "s/^/:/", 
        "{}", 
        ";"
    ),
    'bios': (
        "find", 
        "/sys/devices/virtual/dmi/id",
        "-type", 
        "f", 
        "-readable", 
        "-print0", 
        "-execdir", 
        "sed", 
        "-z", 
        "s/^/:/", 
        "{}", 
        ";"
    ),
    'vulnerability_check': (
        "find",
        "/sys/devices/system/cpu/vulnerabilities",
        "-type", 
        "f", 
        "-readable",
        "-print0", 
        "-execdir", 
        "sed", 
        "-z", 
        "s/^/:/", 
        "{}", 
        ";"
    ),
}


# "iomem": ["find", "/proc/iomem", "-type", "f", "-print0", "-execdir", "sed", "-z", "s/^/:/", "{}", "+"),
# "ioports": ["find", "/proc/ioports", "-type", "f", "-print0", "-execdir", "sed", "-z", "s/^/:/", "{}", "+"),
# "glxinfo": ["glxinfo"],
# "glxinfoD": ["egrep", "-i", "device|memory"],
# "env": ["env"]
