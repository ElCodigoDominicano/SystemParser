"""This file is included with SystemParser in order to obtain system
information and is the main file so the program can be used with
python through a terminal or similar command line application
Copyright (C) 2022 AERivas

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details."

usage posix within a terminal: python SystemParser  command
will display all commands accepted by the program

usage windows within cmd or powershell: py SystemParser command
will display all commands accepted by the program

usage darwin: not implemented yet (near-future)

list of commands for posix machines: processor, bios, virtual_memory_statistics,
vulnerability_check, network_info4, network_info6, modukes_drivers, power,
uptime, load_average

list of commands for windows machines: bus, motherboard,
processor, memory, sound_device, floppy_controller, ide_controller,
pcmcia_controller, parallel_port, usb_hub, usb_controller,
usb_controller_device, serial_port, serial_port_settings,
serial_port_configurations, list_environment_variables,
video_controller, video_settings, video_configurations

Author: AERivas
Date: 07-31-2022"""
import sys
import asyncio

from async_factory import app
asyncio.run(app.main(sys.argv[1:]))
