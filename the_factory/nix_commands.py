"""
    This file is included with SystemParser in order to obtain system information
    Copyright (C) 2022 AERivas

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

"""

posix_command = {
    'cpuInfo': ["cat", "/proc/cpuinfo"],
    'memInfo': ["cat", "/proc/meminfo"],
    'ioMem': ["cat", "/proc/iomem"],
    'ioPorts': ["cat", "/proc/ioports"],
    'loadavg': ["cat", "/proc/loadavg"],
    'modules': ["cat", "/proc/modules"],
    'partitions': ["cat", "/proc/partitions"],
    'version': ["cat", "/proc/version"],
    'vmstat': ["cat", "/proc/vmstat"],
    'uptime': ["cat", "/proc/uptime"],
    'power': [
        'find', '/sys/devices/virtual/dmi/id/power/', '-type', 'f', '-print0', '-readable', '-exec', 
        'sed', 's/^/:/', '{}', ';'],
    'networkInfo6': [
        'find', "-L", '/proc/sys/net/ipv6', '-type', 'f', '-follow', '-print0', '-exec',
        'sed', '-z', 's/^/:/', '{}', ';'],
    'networkInfo4':  [
        'find', '-L', '/proc/sys/net/ipv4', '-type', 'f', '-print0', '-exec', 
        'sed', '-z', 's/^/:/', '{}', ';'],
    'smBios': [
        'find', '/sys/devices/virtual/dmi/id/bios_*', '/sys/devices/virtual/dmi/id/board_*', 
        '/sys/devices/virtual/dmi/id/chassis_*', '/sys/devices/virtual/dmi/id/product_*', 
        '/sys/devices/virtual/dmi/id/sys_*', '/sys/devices/virtual/dmi/id/uevent', 
        '/sys/devices/virtual/dmi/id/ec_firmware_release', 'modalias', '-type', 'f', '-readable', '-print0', '-exec', 
        'awk', '-F', "':'", '{ print FS $0 }', '{}', ';'],
    'checkCpuVuln': [
        'find', '/sys/devices/system/cpu/vulnerabilities','-type', 'f', '-readable', '-print0', '-exec',
        'awk', '-F', ':', '{ print FS $0 }', '{}', ';'],
    'dma': ["cat", "/proc/dma"],
    'diskstats': ["cat", "/proc/diskstats"],
    'devices': ["cat", "/proc/devices"],
    'cmdline': ["cat", "/proc/cmdline"],
    'console': ["cat", "/proc/consoles"],
    'swaps': ["cat", "/proc/swaps"],
    'glxinfo': ['glxinfo'],
    'glxinfoD': ["egrep", "-i", "device|memory"],
    'env': ["env"],
    'filesystems': ["cat", "/proc/filesystems"],
}


#awk -F ":"  '{ print FILENAME FS $0 }' /sys/devices/system/cpu/vulnerabilities
