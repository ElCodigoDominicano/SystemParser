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
import sys

from async_factory import thefactory
from .nix_commands import POSIX_ACCEPTED_ARGS
from .win_commands import WINDOWS_ACCEPTED_ARGS


async def main(args):
    operating_system = thefactory.get_os()
    if operating_system == 'Windows' and len(args) <= 0:
        print(f"The following arguments for the Windows system: ", *WINDOWS_ACCEPTED_ARGS, sep=" ")
    if operating_system == 'Windows' and len(args) == 1:
        if args[0] in WINDOWS_ACCEPTED_ARGS:
            windows = thefactory.WinRig()
            information = await windows.windows_logic(args)
            return information
        elif args[0] not in WINDOWS_ACCEPTED_ARGS:
            print(f"Invalid argument -> {args}")
            sys.exit(0)
    
    if operating_system == 'Linux' and len(args) <= 0:
        print(f"The following arguments for the {operating_system} system:", *POSIX_ACCEPTED_ARGS, sep=" ")
    if operating_system == 'Linux' and len(args) == 1:
        if args[0] in POSIX_ACCEPTED_ARGS:
            posix = thefactory.NixRig()
            information = await posix.posix_logic(args)
            return information
        elif args[0] not in POSIX_ACCEPTED_ARGS:
            print(f"Invalid argument -> {args}")
            sys.exit(0)
    
    if operating_system == 'Darwin':
        print(f"Implementation coming soon for the {operating_system} environment")
        sys.exit(0)
