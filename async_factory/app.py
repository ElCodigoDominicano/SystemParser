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
Date: 07/31/2022 ~ Recently changed 07/13/2023
"""
import platform 

from .thefactory import start_posix, start_windows
from .logger import LogCenter

logger = LogCenter("app_main")

async def main(args):
    operating_system = platform.system()
    
    if operating_system == "Windows":
        await start_windows(args)
       
    elif operating_system == "Linux":
        await start_posix(args)
        
    # Mac coming soon
    else:
        logger.log_critical(f"Implementation coming soon for the {operating_system} environment")