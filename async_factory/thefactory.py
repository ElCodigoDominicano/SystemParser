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
Author: AERivas
Date: 07/31/2022
Updated: 01/10/2023"""
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
@dataclass(slots=True)
class WindowsMachine:
    
    @classmethod
    async def get_system_information(cls, command):
        cls._command = await create_windows_process(command)
        return cls._command
    

# Posix bash command handling
@dataclass(slots=True)
class PosixMachine:
 
    @classmethod
    async def get_system_information(cls, command):
        cls._command = await create_posix_process(command)
        return cls._command
