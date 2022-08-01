"""SystemParser (The Factory) a simple system information gathering tool
using system commands  per  system environment ; using asyncio
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
Date: 07/31/2022"""
import asyncio
import sys
from async_factory import thefactory
from async_factory.nix_commands import POSIX_ACCEPTED_ARGS
from async_factory.win_commands import  WINDOWS_ACCEPTED_ARGS


async def main(args):
    operating_system = thefactory.get_os()
    if len(args) == 0 and operating_system == 'Windows':
        print(f"The following arguments for the {operating_system} system:", *WINDOWS_ACCEPTED_ARGS, sep=" ")
    elif len(args) == 0 and operating_system == "Linux":
        print(f"The following arguments for the {operating_system} system:", *POSIX_ACCEPTED_ARGS, sep=" ")

    elif len(args) > 0 and operating_system == 'Windows':
        windows = thefactory.WinRig()
        try: 
            if  "motherboard" in args:
                motherboard =   await windows.set_command("MotherboardDevice")
                thefactory.print_prettifier(motherboard)
            if "bus" in args:
                bus = await windows.set_command("Bus")
                thefactory.print_prettifier(bus)
            if "processor" in args:
                processor = await windows.set_command("Processor")
                thefactory.print_prettifier(processor)
            # if "network" in args:
            if "memory" in args:
                memory = await windows.set_command("MemoryArray")
                thefactory.print_prettifier(memory)
            # if "drivers" in args:
            if "sound_device" in args:
                sound_device = await windows.set_command("SoundDevice")
                thefactory.print_prettifier(sound_device)
            if "floppy_controller" in args:
                floppy_controller = await windows.set_command("FloppyController")
                thefactory.print_prettifier(floppy_controller)
            if "ide_controller" in args:
                ide_controller = await windows.set_command("IDEController")
                thefactory.print_prettifier(ide_controller)
            if "pcmcia_controller" in args:
                pcmcia_controller = await windows.set_command("PCMCIAController")
                thefactory.print_prettifier(pcmcia_controller)
            if "parallel_port" in args:
                parallel_port = await windows.set_command("ParallelPort")
                thefactory.print_prettifier(parallel_port)
            if "usb_hub" in args:
                usb_hub = await windows.set_command("USBHub")
                thefactory.print_prettifier(usb_hub)
            if "usb_controller" in args:
                usb_controller = await windows.set_command("USBController")
                thefactory.print_prettifier(usb_controller)
            if "usb_controller_device" in args:
                usb_controller_device = await windows.set_command("USBControllerDevice")
                thefactory.print_prettifier(usb_controller_device)
            if "serial_port" in args:
                serial_port = await windows.set_command("SerialPort")
                thefactory.print_prettifier(serial_port)
            if "serial_port_settings" in args:
                serial_port_settings = await windows.set_command("SerialPortSettings")
                thefactory.print_prettifier(serial_port_settings)
            if "serial_port_configurations" in args:
                serial_port_configurations = await windows.set_command("SerialPortConfiguration")
                thefactory.print_prettifier(serial_port_configurations)
            if "list_environment_variables" in args:
                list_environment_variables = await windows.set_command("EnvironmentVariables")
                thefactory.print_prettifier(list_environment_variables)
            if "video_controller" in args:
                video_controller = await windows.set_command("VideoController")
                thefactory.print_prettifier(video_controller)
            if "video_settings" in args:
                video_settings = await windows.set_command("VideoSettings")
                thefactory.print_prettifier(video_settings)
            if "video_configuration" in args:
                video_configuration = await windows.set_command("VideoConfiguration")
                thefactory.print_prettifier(video_configuration)
            if args not in WINDOWS_ACCEPTED_ARGS:
                print(f"Invalid args {args}")
        finally:
            sys.exit(0)
    elif len(args) > 0 and operating_system == 'Linux':
        posix = thefactory.NixRig()
        try: 
            if "bios" in args:
                bios = await posix.set_command("smbios")
                thefactory.print_prettifier(bios)
            if "processor" in args:
                processor = await posix.set_command("cpuinfo")
                thefactory.print_prettifier(processor)
            if "memory" in args:
                memory = await posix.set_command("meminfo")
                thefactory.print_prettifier(memory)
            if "virtual_memory_statistics" in args:
                vm_statistics = await posix.set_command("vmstat")
                thefactory.print_prettifier(vm_statistics)
            if "vulnerability_check" in args:
                cpu_vulnerability_check =  await posix.set_command("check_cpu_vuln")
                thefactory.print_prettifier(cpu_vulnerability_check)
            if "network_ip4" in args:
                network_info4 = await posix.set_command("network_info4")
                thefactory.print_prettifier(network_info4)
            if "network_ip6" in args:
                network_info6 =  await posix.set_command("network_info6")
                thefactory.print_prettifier(network_info6)
            if "power" in args:
                power = await posix.set_command("power")
                thefactory.print_prettifier(power)
            if "driver_modules" in args:
                driver_modules = await posix.set_command("modules")
                thefactory.print_prettifier(driver_modules)
            if "uptime" in args:
                uptime = await posix.set_command("uptime")
                thefactory.print_prettifier(uptime)
            if "load_average" in args:
                load_average = await posix.set_command("loadavg")
                thefactory.print_prettifier(load_average)
            if args not in POSIX_ACCEPTED_ARGS:
                print(f"Invalid args {args}")
        finally:
            sys.exit(0)
    elif len(args) >= 0 and operating_system == 'Darwin':
        print(f"Implementation coming soon for the {operating_system} environment")
        sys.exit(0)
