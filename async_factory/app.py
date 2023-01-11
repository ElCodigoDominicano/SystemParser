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
import time
import logging
import pprint
import platform 

from .thefactory import WindowsMachine, PosixMachine
from .nix_commands import POSIX_ACCEPTED_ARGS
from .win_commands import WINDOWS_ACCEPTED_ARGS
from .exception_classes import OSNotImplemented


logger = logging.getLogger()
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s"
)

# helper
def get_operating_system() -> str:
    return platform.system()


start = time.time()
async def main(args):
    operating_system = get_operating_system()
    pp = pprint.PrettyPrinter(indent=4)
    if operating_system == 'Windows' and len(args) <= 0:
        logger.info(f"The following arguments for {operating_system}: \n{' | '.join(WINDOWS_ACCEPTED_ARGS)}.")
    
    if operating_system == 'Windows' and len(args) == 1:
        if args[0] in WINDOWS_ACCEPTED_ARGS:
            await WindowsMachine.get_system_information(args)
            pp.pprint(WindowsMachine._command)

        elif args[0] not in WINDOWS_ACCEPTED_ARGS:
            logger.warning(f"Invalid argument => {args}")
            sys.exit(0)
    
    if operating_system == 'Linux' and len(args) <= 0:
        logger.info(f"the following arguments for {operating_system}: \n{' | '.join(POSIX_ACCEPTED_ARGS)}.")
    
    if operating_system == 'Linux' and len(args) == 1:
        if args[0] in POSIX_ACCEPTED_ARGS:
            await PosixMachine.get_system_information(args)
            pp.pprint(PosixMachine._command)
            
        elif args[0] not in POSIX_ACCEPTED_ARGS:
            logger.info(f"Invalid argument -> {args}")
            sys.exit(0)
    
    if operating_system == 'Darwin':
        raise OSNotImplemented(f"Implementation coming soon for the {operating_system} environment")

    end = time.time()
    logger.info(f"Execution time: {end - start}")
