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

from async_factory.async_posix import create_posix_process
from async_factory.async_windows import create_windows_process


def get_os() -> str:
    return platform.system()


def print_prettifier(default_dictionary):
    if get_os() == 'Windows':
        result = [print("{:10} {:^10} {:10}".format(k, "=>", " ".join(v))) for (k,v) in default_dictionary.items()]
    elif get_os() == 'Linux':
        result = [print("{:10} {:^10} {:10}".format(k, "=>", " ".join(v))) for (k,v) in default_dictionary.items()]
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


class NixRig:
    command: str
    
    @classmethod
    async def set_command(cls, command):
        self = NixRig()
        self._command = await create_posix_process(command)
        return self._command
