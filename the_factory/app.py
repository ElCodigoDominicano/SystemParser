"""
    SystemParser(The Factory) a simple system information gathering tool
    Copyright (C) 2022 AERivas

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    Author: AERivas
    Date: 07/17/2022
"""
import sys
from the_factory import thefactory

def main(args: list[str]):
    operating_system = thefactory.get_os()
    if len(args) == 0 and operating_system == 'Windows':
        print(f"The following arguements for the {operating_system} system:", *thefactory.WINDOWS_ACCEPTED_ARGS, sep=" ")
        sys.exit(0)
    elif len(args) == 0 and operating_system == "Linux":
        print(f"The following arguements for the {operating_system} system:", *thefactory.LINUX_ACCEPTED_ARGS, sep=" ")
    if len(args) > 0 and operating_system == 'Windows':
        w = thefactory.WinRig()
        for arguement in args:
            try:
                if arguement == 'bus':
                    w.get_bus_information()
                if arguement == 'processor':
                    w.get_processor_information()
                if arguement == 'network':
                    w.get_network_information()
                if arguement == 'memory':
                    w.get_memory_information()
                if arguement == 'drivers':
                    w.get_driver_information()
                if arguement == 'sound':
                    w.get_sound_device_information()
                if arguement == 'usb':
                    w.get_usb_port_information()
                if arguement == 'floppy':
                    w.get_floppy_drive_information()
                if arguement == 'ide':
                    w.get_ide_controller_information()
                if arguement == 'pcmcia':
                    w.get_pcmcia_controller_information()
                if arguement == 'usb':
                    w.get_usb_port_information()
                if arguement == 'parallel':
                    w.get_parallel_port_information()
                if arguement == 'serial':
                    w.get_serial_port_information()
                if arguement == 'graphics':
                    w.get_graphic_card_information()
                if arguement not in thefactory.WINDOWS_ACCEPTED_ARGS:
                    print(f"The provided arguement [{arguement}] is invalid, please run again.")
                    raise
            finally:
                sys.exit(0)
        
    if operating_system == 'Linux' and len(args) > 0:
        x = thefactory.NixRig()
    for arguement in args:   
        try:     
            if arguement == 'bios':
                x.get_smbios_information()
            if arguement == 'processor':
                x.get_processor_information()
            if arguement == 'network':
                x.get_network_information()
            if arguement == 'memory':
                x.get_memory_information()
            if arguement == 'drivers':
                x.get_driver_information()
            if arguement == 'check_vuln':
                x.get_cpu_vuln_information()
            if arguement == 'power':
                x.get_power_information()
            if arguement not in thefactory.LINUX_ACCEPTED_ARGS:
                print(f"The Provided arguement [{arguement}] is invalid, please run again.")
        finally:
            sys.exit(0)

    if operating_system == 'Darwin':
        print(f"Implementation coming soon for the {operating_system} environment")
        raise
