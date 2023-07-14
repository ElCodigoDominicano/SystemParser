"""Copyright (C) 2023 AERivas

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

A all-in-one system information display tool, small,a nd no external dependancies.

Author: AERivas
Date: 07/31/2022
Updated: 01/10/2023 ~ 07/14/2023
"""
import sys
import os

from .logger import LogCenter
from .ansi.give_color import AnsiTools
from .nix.async_posix import create_posix_process, POSIX_COMMANDS
from .win.async_windows import create_windows_process, POWERSHELL_COMMANDS

give_color = AnsiTools()
logger = LogCenter("factory")
wall_ornament = give_color.to_this_string("dark_green", "|_-~> ")
    
async def start_posix(args):
    nix_response = "\n".join([wall_ornament + give_color.to_this_string("bright_green", nix_keys) for nix_keys in POSIX_COMMANDS])
    try:
        response_from_sys = await create_posix_process(args)
        colored_dict = give_color.to_this_dict(response_from_sys, "green", "bright_green")
        for x in colored_dict:
            print(f"{wall_ornament}{x}: {colored_dict[x]}")
    except KeyError as ke:
        logger.log_critical(f"Invalid Selection ~> {ke}")
    except IndexError:
        print("The following are the list available commands: \n{}".format(nix_response))
    finally:
        sys.exit(0) 

async def start_windows(args):
    os.system('color')
    win_response = "\n".join([wall_ornament + give_color.to_this_string("bright_green", win_keys) for win_keys in POWERSHELL_COMMANDS])
    try:
        response_from_sys = await create_windows_process(args)
        colored_dict = give_color.to_this_dict(response_from_sys, "yellow", "bright_yellow")
        for x in colored_dict:
            print(f"{wall_ornament}{x}: {colored_dict[x]}")
    except KeyError as ke:
        logger.log_critical(f"Invalid argument ~> {ke}")
    except IndexError:
        print("The following are the list of available commands: \n{}".format(win_response))
    finally:
        sys.exit(0)