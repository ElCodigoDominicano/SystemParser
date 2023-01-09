"""This file is included with SystemParser in order to obtain system information
on posix machines. Copyright (C) 2022 AERivas

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.


A simple linux system information gathering tool using the builtin 
asyncio library,  create_subprocess_exec is similar to using the built-in
subprocess modules', Popen constructor without using shell=True
(which may cause security concerns...)

for more information: https://docs.python.org/3/library/subprocess.html#security-considerations
Author: AERivas
Date: 07/31/2022"""
import asyncio

from collections import defaultdict
from .nix_commands import POSIX_COMMANDS


async def create_posix_process(command_key):
    """*Coroutine awaitable function
    Starts an asynchronous subprocess based on the given 
    command_key, in this case the dictionary key and values
    found inside the nix_commands ; POSIX_COMMANDS
    which is a constant ; a dictionary holding all the posix commands
    required to have this program function properly.

    converts the output stream from byte to a list as strings
    filter function is used to help filter out the possibilities of  a
    NoneType error thus  the information is a filter iterable object.

    being asynchronous, the process awaits for another coroutine
    (commander_delegate)to finish before THIS coroutine completes
    its duty of becoming an awaitable coroutine that returns a default-dict.

    Parameter command_key: the argument required for this program to function properly.
    Precondition command_key: must be valid posix commands contained in lists separated by commas."""
    _process = await asyncio.create_subprocess_exec(
        *POSIX_COMMANDS[command_key],
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
        # Permission error dependent on which command being ran
        # sudo required for viewing root permission files
        pass


async def stream_parser(stream_iter):
    """*Coroutine awaitable function*
    Returns a default dictionary, using the list as its default factory.
    loops through a stream iterable that is using the find command. 
    adds the system file name as the keys and the file value as the 
    values for a default dictionary, the default factory is a list.

    Parameter stream_iter: a stream iterable object produced from create_posix_process
    Precondition stream_iter: must be a decoded byte->str, split by its newlines and None filtered.
    
    Author: AERivas
    Date: 07/31/2022"""
    TEMPLATE = defaultdict(list)
    for file_output in stream_iter:
        if file_output.startswith("/"):
            first_slash = file_output.find("/")
            colon = file_output.find(":")
            data_inside_file = file_output[colon:].strip(":").replace("\t"," ")
            dir_file_names = file_output[first_slash+13:colon].replace("/", " ").strip("\x00")
            TEMPLATE[dir_file_names].append(data_inside_file)
        elif not file_output.startswith("/"): 
            colon = file_output.find(":")
            _key = file_output[:colon]
            _val = file_output[colon+1:]
            TEMPLATE[_key].append(_val)
    return TEMPLATE
