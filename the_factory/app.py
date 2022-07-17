"""
    The Factory a simple system information gathering tool
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

import sys
from the_factory import thefactory


def main(args: list[str]):
    operating_system = thefactory.get_os()
    print(f"The following arguments for the {operating_system} system:", *thefactory.WINDOWS_ACCEPTED_ARGS, sep=" ")
    print()
    if operating_system == 'Windows':
        w = thefactory.WinRig()
        for argument in args:
            try:
                if argument == 'bus':
                    w.get_bus_information()
                if argument == 'processor':
                    w.get_processor_information()
                if argument == 'network':
                    w.get_network_information()
                if argument == 'memory':
                    w.get_memory_information()
                if argument == 'drivers':
                    w.get_driver_information()
                if argument == 'sound':
                    w.get_sound_device_information()
                if argument == 'usb':
                    w.get_usb_port_information()
                if argument == 'floppy':
                    w.get_floppy_drive_information()
                if argument == 'ide':
                    w.get_ide_controller_information()
                if argument == 'pcmcia':
                    w.get_pcmcia_controller_information()
                if argument == 'usb':
                    w.get_usb_port_information()
                if argument == 'parallel':
                    w.get_parallel_port_information()
                if argument == 'serial':
                    w.get_serial_port_information()
                if argument == 'graphics':
                    w.get_graphic_card_information()
                if argument not in thefactory.WINDOWS_ACCEPTED_ARGS:
                    print(f"The provided argument [{argument}] is invalid, please run again.")
                    raise
            finally:
                sys.exit(0)
        
    if operating_system == 'Linux':
        print(f"The following commands for the {operating_system} system:", *thefactory.LINUX_ACCEPTED_ARGS, sep=" ")
        x = thefactory.NixRig()
    for argument in args:   
        try:     
            if argument == 'bios':
                x.get_smbios_information()
            if argument == 'processor':
                x.get_processor_information()
            if argument == 'network':
                x.get_network_information()
            if argument == 'memory':
                x.get_memory_information()
            if argument == 'drivers':
                x.get_driver_information()
            if argument == 'check_vuln':
                x.get_cpu_vuln_information()
            if argument == 'power':
                x.get_power_information()
            if argument not in thefactory.LINUX_ACCEPTED_ARGS:
                print(f"The Provided argument [{argument}] is invalid, please run again.")
        finally:
            sys.exit(0)

    if operating_system == 'Darwin':
        print(f"Implementation coming soon for the {operating_system} environment")
        raise
