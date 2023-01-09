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

The Factory becomes. Ergo... ASync Factory; The awaitable command 
center used for Central Intelligence of Rig-Information (Your Machine)
the starter of processes..
... (..@_@),
The delegator of environments, the output prettifier.

Author: AERivas
Date: 07/31/2022"""
import platform

from .async_posix import create_posix_process
from .async_windows import create_windows_process


def get_os() -> str:
    return platform.system()


def print_prettifier(default_dictionary):
    if get_os() == 'Windows':
        result = [print("{:20} {:^10} {:20}".format(k, "=>", " ".join(v))) for (k,v) in default_dictionary.items()]
    elif get_os() == 'Linux':
        result = [print("{:20} {:^10} {:20}".format(k, "=>", " ".join(v))) for (k,v) in default_dictionary.items()]
    elif get_os == 'Darwin':
        print(f"The following environment hasn't been implemented yet {get_os()}.")
        raise


class WinRig:
    command: str

    @classmethod
    async def set_command(cls, command):
        self = WinRig()
        self._command = await create_windows_process(command)
        return self._command
    
    
    async def windows_logic(self, args):
        if "motherboard" in args:
            motherboard = await WinRig.set_command("MotherboardDevice")
            print_prettifier(motherboard)
        if "bus" in args:
            bus = await WinRig.set_command("Bus")
            print_prettifier(bus)
        if "processor" in args:
            processor = await WinRig.set_command("Processor")
            print_prettifier(processor)
        if "memory" in args:
            memory = await WinRig.set_command("MemoryArray")
            print_prettifier(memory)
        if "sound_device" in args:
            sound_device = await WinRig.set_command("SoundDevice")
            print_prettifier(sound_device)
        if "floppy_controller" in args:
            floppy_controller = await WinRig.set_command("FloppyController")
            print_prettifier(floppy_controller)
        if "ide_controller" in args:
            ide_controller = await WinRig.set_command("IDEController")
            print_prettifier(ide_controller)
        if "pcmcia_controller" in args:
            pcmcia_controller = await WinRig.set_command("PCMCIAController")
            print_prettifier(pcmcia_controller)
        if "parallel_port" in args:
            parallel_port = await WinRig.set_command("ParallelPort")
            print_prettifier(parallel_port)
        if "usb_hub" in args:
            usb_hub = await WinRig.set_command("USBHub")
            print_prettifier(usb_hub)
        if "usb_controller" in args:
            usb_controller = await WinRig.set_command("USBController")
            print_prettifier(usb_controller)
        if "usb_controller_device" in args:
            usb_controller_device = await WinRig.set_command("USBControllerDevice")
            print_prettifier(usb_controller_device)
        if "serial_port" in args:
            serial_port = await WinRig.set_command("SerialPort")
            print_prettifier(serial_port)
        if "serial_port_settings" in args:
            serial_port_settings = await WinRig.set_command("SerialPortSettings")
            print_prettifier(serial_port_settings)
        if "serial_port_configurations" in args:
            serial_port_configurations = await WinRig.set_command("SerialPortConfiguration")
            print_prettifier(serial_port_configurations)
        if "list_environment_variables" in args:
            list_environment_variables = await WinRig.set_command("EnvironmentVariables")
            print_prettifier(list_environment_variables)
        if "video_controller" in args:
            video_controller = await WinRig.set_command("VideoController")
            print_prettifier(video_controller)
        if "video_settings" in args:
            video_settings = await WinRig.set_command("VideoSettings")
            print_prettifier(video_settings)
        if "video_configuration" in args:
            video_configuration = await WinRig.set_command("VideoConfiguration")
            print_prettifier(video_configuration)

            
class NixRig:
    command: str
    
    @classmethod
    async def set_command(cls, command):
        self = NixRig()
        self._command = await create_posix_process(command)
        return self._command
    
    
    async def posix_logic(self, args):
        if "bios" in args:
            bios = await NixRig.set_command("smbios")
            print_prettifier(bios)
        if "processor" in args:
            processor = await NixRig.set_command("cpuinfo")
            print_prettifier(processor)
        if "memory" in args:
            memory = await NixRig.set_command("meminfo")
            print_prettifier(memory)
        if "virtual_memory_statistics" in args:
            vm_statistics = await NixRig.set_command("vmstat")
            print_prettifier(vm_statistics)
        if "vulnerability_check" in args:
            cpu_vulnerability_check = await NixRig.set_command("check_cpu_vuln")
            print_prettifier(cpu_vulnerability_check)
        if "network_ip4" in args:
            network_info4 = await NixRig.set_command("network_info4")
            print_prettifier(network_info4)
        if "network_ip6" in args:
            network_info6 =  await NixRig.set_command("network_info6")
            print_prettifier(network_info6)
        if "power" in args:
            power = await NixRig.set_command("power")
            print_prettifier(power)
        if "driver_modules" in args:
            driver_modules = await NixRig.set_command("modules")
            print_prettifier(driver_modules)
        if "uptime" in args:
            uptime = await NixRig.set_command("uptime")
            print_prettifier(uptime)
        if "load_average" in args:
            load_average = await NixRig.set_command("loadavg")
            print_prettifier(load_average)
