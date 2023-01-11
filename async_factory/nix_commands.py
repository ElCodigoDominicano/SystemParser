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

POSIX_ACCEPTED_ARGS: tuple[str] = (
    'processor',
    'memory',
    'uptime',
    'load_average',
    'driver_modules',
    'virtual_memory_statistics',
    'power',
    'network_ip4',
    'network_ip6',
    'bios',
    'vulnerability_check',
)

POSIX_COMMANDS: dict[str, tuple[str]] = {
    POSIX_ACCEPTED_ARGS[0]: (
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
    POSIX_ACCEPTED_ARGS[1]: (
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
    POSIX_ACCEPTED_ARGS[2]: (
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
    POSIX_ACCEPTED_ARGS[3]: (
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
    POSIX_ACCEPTED_ARGS[4]: (
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
    POSIX_ACCEPTED_ARGS[5]: (
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
    POSIX_ACCEPTED_ARGS[6]: (
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
    POSIX_ACCEPTED_ARGS[7]: (
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
    POSIX_ACCEPTED_ARGS[8]: (
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
    POSIX_ACCEPTED_ARGS[9]: (
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
    POSIX_ACCEPTED_ARGS[-1]: (
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
