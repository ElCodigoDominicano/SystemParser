"""This file is included with SystemParser in order to display 
system information on posix machines. Copyright (C) 2022 AERivas

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.


A simple linux system information gathering tool using the builtin 
asyncio library, 

Author: AERivas
Date: 07/31/2022 ~ 07/13/2023
"""
import asyncio

from .nix_commands import POSIX_COMMANDS
from ..logger import LogCenter

log_center = LogCenter("async_posix")

async def create_posix_process(command_key):
    """COROUTINE, creates and ansychronous subprocess which then takes 
    the stream, decodes from bytes to str and filters out the None values
    which are OS level errors; Permission. then awaits for stream_parser to
    return that stream data as a dictionary.

    Parameter command_key: the argument required for this program to function properly.
    Precondition command_key: must be valid posix commands contained in lists separated by commas.
    
    Author: AERivas
    Date: 07/31/2022 ~ 07/13/2023
    """
    
    _process = await asyncio.create_subprocess_exec(
        *POSIX_COMMANDS[command_key[0]],
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await _process.communicate()
    await _process.wait()
    
    if stdout is not None:   
        stream_to_str_to_lst = stdout.decode().split("\n")
        stream_iter = filter(None, stream_to_str_to_lst)
        bucket = await stream_parser(stream_iter)
        return bucket
    if stderr:
        log_center.log_warning("Permission needed to view certain files.")
        # Permission error dependent on which command being ran.
        # certain files and or directories require superuser.
        # sudo required for viewing root permission files
        
async def stream_parser(stream_iter):
    """Returns a dictionary containing the information gathered from stream_iter

    Parameter stream_iter: a stream iterable object produced from create_posix_process
    Precondition stream_iter: must be a decoded byte->str, split by its newlines and NoneTypes filtered out.
    
    Author: AERivas
    Date: 07/31/2022
    """
    TEMPLATE = {}
    for file_output in stream_iter:
        if file_output.startswith("/"):
            first_slash = file_output.find("/")
            colon = file_output.find(":")
            data_inside_file = file_output[colon:].strip(":").replace("\t","")
            dir_file_names = file_output[first_slash+13:colon].replace("/", " ").strip("\x00 ")
            TEMPLATE |= {dir_file_names: data_inside_file}
        elif not file_output.startswith("/"): 
            colon = file_output.find(":")
            _key = file_output[:colon].strip("\t")
            _val = file_output[colon+1:]
            TEMPLATE |= {_key: _val}
    return TEMPLATE