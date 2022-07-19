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
    
    The Factory; gatherer of information, the hodlr of values, 
    the delagator of environments, the outlet of default dictionaries.
    
    Author: AERivas
    Date: 07/11/2022
"""
import platform
from .nix_parse import start_posix_process
from .win_parse import start_powershell_process
from .win_commands import powershell_command
from .nix_commands import posix_command

WINDOWS_ACCEPTED_ARGS: list[str] = [
    'bus',
    'processor',
    'network',
    'memory',
    'drivers',
    'sound',
    'usb',
    'floppy',
    'ide',
    'pcmcia',
    'usb',
    'parallel',
    'serial',
    'graphics',
    ]
LINUX_ACCEPTED_ARGS: list[str] = [
    'bios',
    'processor',
    'network',
    'memory',
    'drivers',
    'check_vuln',
    'power',
    '',
    '',
    '',
    '',
    '',
    ]


def get_os() -> str:
    return platform.system()


def print_prettifier(func):
    if get_os() == 'Windows':
        result = [print("{:20} => {:^30}".format(k, " ".join(v))) for (k,v) in func.items()]
        result.pop(None)
    elif get_os() == 'Linux':
        result = [print("{:20} => {:^30}".format(k, v[0:])) for (k,v) in func.items()]
        result.pop(None)


class WinRig:

    def __init__(self):
        self._motherboard = powershell_command["MotherboardDevice"]
        self._processor = powershell_command["Processor"]
        self._memory = powershell_command["MemoryArray"]
        self._bus = powershell_command["Bus"]
        #self._network = powershell_command["Network"]
        self._sound_device = powershell_command["SoundDevice"]
        self._floppy = powershell_command["FloppyController"]
        self._ide = powershell_command["IDEController"]
        self._pcmcia = powershell_command["PCMCIAController"]
        self._parallel = powershell_command["ParallelPort"]
        self._usb_hub = powershell_command["USBHub"]
        self._usb_controller = powershell_command["USBController"]
        self._usb_controller_device = powershell_command["USBControllerDevice"]
        self._serial_port = powershell_command["SerialPort"]
        self._serial_port_settings = powershell_command["SerialPortSettings"]
        self._serial_port_configuration = powershell_command["SerialPortConfiguration"]
    
    def get_motherboard_information(self):
        print_prettifier(start_powershell_process(self._motherboard))


    def get_processor_information(self):
        print_prettifier(start_powershell_process(self._processor))
        
            
    def get_memory_information(self):
        print_prettifier(start_powershell_process(self._memory))


    # def get_network_information(self):
    #     print(start_powershell_process(self._network))


    def get_bus_information(self):
        print_prettifier(start_powershell_process(self._bus))


    def get_sound_device_information(self):
        print_prettifier(start_powershell_process(self._sound_device))


    def get_floppy_drive_information(self):
        print_prettifier(start_powershell_process(self._floppy))


    def get_ide_controller_information(self):
        print_prettifier(start_powershell_process(self._ide))


    def get_pcmcia_controller_information(self):
        print_prettifier(start_powershell_process(self._pcmcia))


    def get_parallel_port_information(self):
        print_prettifier(start_powershell_process(self._parallel))


    def get_usb_hub_information(self):
        print_prettifier(start_powershell_process(self._usb_hub))
    
    
    def get_usb_controller_information(self):
        print_prettifier(start_powershell_process(self._usb_controller))
    
    
    def get_usb_controller_device_infromation(self):
        print_prettifier(start_powershell_process(self._usb_controller_device))
   

    def get_serial_port_information(self):
        print_prettifier(start_powershell_process(self._serial_port))

    
    def get_serial_port_settings_information(self):
        print_prettifier(start_powershell_process(self._serial_port_settings))
        
    
    def get_serial_port_configuration_information(self):
        print_prettifier(start_powershell_process(self._serial_port_configuration))


    def get_graphic_card_information(self):
        """
        To be implemented, amd and nvidia dependent..
        """
        pass

class NixRig():

    def __init__(self):
        self._smbios = posix_command["smBios"]
        self._processor = posix_command["cpuInfo"]
        self._memory = posix_command["memInfo"]
        self._drivers = posix_command["modules"]
        self._cpu_vulnerabilities = posix_command['checkCpuVuln']
        self._network4 = posix_command["networkInfo4"]
        self._network6 = posix_command["networkInfo6"]
        self._power = posix_command["power"]
        # self._usb = 
        # self._audio_device = 
        # self._bus = 
        # self._gpu = 
    
    def get_power_information(self):
        print_prettifier(start_posix_process(self._power))

    
    def get_smbios_information(self):
        """
        Path below contain SMBIOS information;
        BIOS, Board, Chassis and Product information..
        it is a question of ask user to run as root 
        or have them install dmidecode
        
        /sys/devices/virtual/dmi/id/
        """      
        print_prettifier(start_posix_process(self._smbios))


    def get_processor_information(self):
        """
        Returns a dictionary-like object containing various CPU information,
        such as the brand, its rated speed, its model number and cache size.
        in human readable format. the information is parsed from /proc/cpuinfo

        *defaultdict in short allows for mutability of the dictionary data type
        dictionary keys are immutable which wont allow for duplicated keys
        with that being said all duplicated keys group their values into lists
        ex: {'Processor': [0,1,2,3,4,5]}

        more about default-dictionaries below
        https://docs.python.org/3/library/collections.html#collections.defaultdict
        """
        print_prettifier(start_posix_process(self._processor))
   

    def get_memory_information(self):
        """
        Returns a dictionary containing memory information from the system. 
        parses this information from /proc/meminfo file which contains 
        ram and swap usage information. since the stream is non-repetitive 
        there is no need for this to be a default dictionary
        """
        print_prettifier(start_posix_process(self._memory))


    def get_gpu_information(self):
        """
        Returns a dictionary containing the systems 
        graphics processing information such as qty of memory, 
        brand name, model #, etc

        glxinfo | egrep -i 'device|memory'
        
        """
        pass


    def get_audio_device_information(self):
        """
        aplay -l <-- lists hardware playback devices
        aplay --list-devices
        aplay --list-pcms
        """
        pass


    def get_bus_information(self):
        """
        lcpci -v
        """
        pass


    def get_usb_port_information(self):
        """"
        lsusb
        """
        pass
    
    
    def get_network4_information(self):
        """
        Returns a dictionary containing various network
        information such as settings and configuration 
        stored in /proc/sys/net/ipv4
        """
        print_prettifier(start_posix_process(self._network4))

    
    def get_network6_information(self):
        """
        Returns a dictionary containing various network
        information such as settings and configuration 
        stored in /proc/sys/net/ipv6
        """
        print_prettifier(start_posix_process(self._network6))
    
    
    def get_driver_information(self):
        """Returns a dictionary containing the installed device drivers (mod)"""
        print_prettifier(start_posix_process(self._drivers))
    
    
    def get_cpu_vuln_information(self):
        """
        Returns a dictionary containing the codenames of the vulnerabilities 
        that effect CPUs as keys, and the values are output that reflect the state 
        for that  CPU.
        
        possible outputs...
        "Not affected"	  CPU is not affected by the vulnerability
		"Vulnerable"	  CPU is affected and no mitigation in effect
		"Mitigation: $M"  CPU is affected and mitigation $M is in effect

        these files are located: /sys/devices/system/cpu/vulnerabilities/
        more information: https://www.kernel.org/doc/Documentation/ABI/testing/sysfs-devices-system-cpu
        """
        print_prettifier(start_posix_process(self._cpu_vulnerabilities))
