"""This file is included with SystemParser in order to obtain system information
on windows machines. Copyright (C) 2022 AERivas

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

A basic windows system information gathering tool using asyncio
subprocess, to create a bespoke function which hides the window from the user,
and a bespoke powershell output separator tool.

Returns a defaultdict whose values are a string of words contained in lists,
the data contained inside is the output information from a valid powershell command
the commands are a list of strings that are commands separated by commas.

Example: ['PowerShell.exe', 'Get-CimInstance', '-ClassName', 'Win32_Processor']
the above example tells powershell to get an 'instance of a Win32 class object'
in this case information about the local or remote systems processor.

*changes will be made periodically*
NOTE: https://docs.microsoft.com/en-us/windows/win32/cimwin32prov/win32-provider    

Author: AERivas
Date 07/31/2022"""
import asyncio
import subprocess
import logging

from collections import defaultdict
from .win_commands import POWERSHELL_COMMANDS

logger = logging.getLogger()
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s"
)

async def hide_process():
    """Coroutine awaitable function
    Returns information for a process startup to create no window
    when using subprocess.Popen or asyncio.create_subprocess_exec
    its use is mainly for windows in this program"""
    startup_information = subprocess.STARTUPINFO()
    startup_information.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startup_information.wShowWindow = subprocess.CREATE_NO_WINDOW
    return startup_information


async def create_windows_process(command_key):
    """*Coroutine awaitable function*
    Starts a process based on above example of powershell command
    separated strings by commas contained in a list. Converts the 
    process output (bytes) to a list of strings to be used for the program

    Parameter command: a list of strings separated by commas.
    Precondition command: a valid Win32 provider class string (check examples)"""
    _process = await asyncio.create_subprocess_exec(
        *POWERSHELL_COMMANDS[command_key.pop()],
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
        startupinfo= await hide_process())
    stdout, stderr = await _process.communicate()
    await _process.wait()
    
    if stdout is not None:
        stream_byte_str_to_lst = stdout.decode().split("\r\n")
        stream_iter = filter(None, stream_byte_str_to_lst)
        bucket = await stream_parser(stream_iter)
        return bucket
    if stderr:
        pass


async def stream_parser(stream_iter):
    """*Coroutine awaitable function*
    Returns a default-dict from the started process.
    this function takes a filter iterable object which contains
    the output information as a list of strings from the created
    powershell process.
    
    Parameter stream_iter: 
    Precondition stream_iter:"""
    TEMPLATE = defaultdict(list)
    for strings in stream_iter:
        colon = strings.find(":")
        keys = strings[:colon].strip(" ")
        values = strings[colon+1:].strip(" ")
        TEMPLATE[keys].append(values)
    return TEMPLATE