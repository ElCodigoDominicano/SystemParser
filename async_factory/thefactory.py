"""This file is included with SystemParser,  assigns the results 
to the attribs

Copyright (C) 2023 AERivas

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

The Factory becomes. Ergo... ASync Factory; The awaitable command 
center; used for Central Intelligence of Information Gathering 
(in short for you to use too find out about certain information 
about your system)
... |(--@_@),
The delegator of environments,
Author: AERivas
Date: 07/31/2022
Updated: 01/10/2023"""
import platform
import logging

from dataclasses import dataclass
from .async_posix import create_posix_process
from .async_windows import create_windows_process
from .nix_commands import POSIX_ACCEPTED_ARGS
from .win_commands import WINDOWS_ACCEPTED_ARGS
from .exception_classes import OSNotImplemented

logger = logging.getLogger()
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s"
)


# Windows powershell command handling
@dataclass
class WindowsMachine:
    _command: str
    motherboard: str
    bus: str
    processor: str
    memory: str
    sound_device: str
    floppy_controller: str
    ide_controller: str
    pcmcia_controller: str
    parallel_port: str
    usb_hub: str
    usb_controller: str
    usb_controller_device: str
    serial_port: str
    serial_port_settings: str
    serial_port_configurations: str
    list_environment_variables: str
    video_controller: str
    video_settings: str
    video_configurations: str

    @classmethod
    async def get_system_information(cls, command):
        cls._command = await create_windows_process(command)
        return cls._command
    
    @classmethod
    async def __delegate_user_command(cls, args):
        if "motherboard" in args:
            cls.motherboard = await WinRig.set_command("motherboard")
        elif "bus" in args:
            cls.bus = await WinRig.set_command("bus")
        elif "processor" in args:
            cls.processor = await WinRig.set_command("processor")
        elif "memory" in args:
            cls.memory = await WinRig.set_command("memory")
        elif "sound_device" in args:
            cls.sound_device = await WinRig.set_command("sound_device")
        elif "floppy_controller" in args:
            cls.floppy_controller = await WinRig.set_command("floppy_controller")
        elif "ide_controller" in args:
            cls.ide_controller = await WinRig.set_command("ide_controller")
        elif "pcmcia_controller" in args:
            cls.pcmcia_controller = await WinRig.set_command("pcmcia_controller")
        elif "parallel_port" in args:
            cls.parallel_port = await WinRig.set_command("parallel_port")
        elif "usb_hub" in args:
            cls.usb_hub = await WinRig.set_command("usb_hub")
        elif "usb_controller" in args:
            cls.usb_controller = await WinRig.set_command("usb_controller")
        elif "usb_controller_device" in args:
            cls.usb_controller_device = await WinRig.set_command("usb_controller_device")
        elif "serial_port" in args:
            cls.serial_port = await WinRig.set_command("serial_port")
        elif "serial_port_settings" in args:
            cls.serial_port_settings = await WinRig.set_command("serial_port_settings")
        elif "serial_port_configurations" in args:
            cls.serial_port_configurations = await WinRig.set_command("serial_port_configurations")
        elif "list_environment_variables" in args:
            cls.list_environment_variables = await WinRig.set_command("list_environment_variables")
        elif "video_controller" in args:
            cls.video_controller = await WinRig.set_command("video_controller")
        elif "video_settings" in args:
            cls.video_settings = await WinRig.set_command("video_settings")
        elif "video_configurations" in args:
            cls.video_configuration = await WinRig.set_command("video_configurations")
        elif args[0] not in POSIX_ACCEPTED_ARGS:
            logger.warning("Invalid argument please try again.")


# Posix bash command handling
@dataclass(slots=True)
class PosixMachine:
    information: None
    bios: str
    processor: str
    memory: str
    virtual_memory_statistics: str
    vulnerability_check: str
    network_info4: str
    network_info6: str
    power: str
    driver_modules: str
    uptime: str
    load_average: str
    
    @classmethod
    async def get_system_information(cls, command):
        cls._command = await create_posix_process(command)
        return cls._command

    @classmethod
    async def __delegate_user_command(cls, args):
        if "bios" in args:
            cls.bios = await NixRig.set_command("bios")
        elif "processor" in args:
            cls.processor = await NixRig.set_command("processor")
        elif "memory" in args:
            cls.memory = await NixRig.set_command("memory")
        elif "virtual_memory_statistics" in args:
            cls.vm_statistics = await NixRig.set_command("vmstat")
        elif "vulnerability_check" in args:
            cls.cpu_vulnerability_check = await NixRig.set_command("vulnerability_check")
        elif "network_ip4" in args:
            cls.network_info4 = await NixRig.set_command("network_ip4")
        elif "network_ip6" in args:
            cls.network_info6 = await NixRig.set_command("network_ip6")
        elif "power" in args:
            cls.power = await NixRig.set_command("power")
        elif "driver_modules" in args:
            cls.driver_modules = await NixRig.set_command("driver_modules")
        elif "uptime" in args:
            cls.uptime = await NixRig.set_command("uptime")
        elif "load_average" in args:
            cls.load_average = await NixRig.set_command("load_average")
        elif not args[0] in WINDOWS_ACCEPTED_ARGS:
            logger.warning("Invalid argument please run again.")