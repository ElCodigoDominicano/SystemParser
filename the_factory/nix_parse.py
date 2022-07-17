"""
    This file is included with SystemParser in order to obtain system information
    Copyright (C) 2022 AERivas

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.


    A simple linux system information gathering tool using the builtin 
    subprocess library, and POSIX terminal commands find, sed, cat, and awk.
    without using shell=True (which may cause security concerns...)

    for more information: https://docs.python.org/3/library/subprocess.html#security-considerations
    Author: AERivas
    Date: 07/02/2022
"""
import subprocess
from collections import defaultdict

def start_posix_process(command: list[str]) -> defaultdict[list]:
    """
    Returns the created defaultdict that contains hardware information 
    from the above stated terminal command first starts a process
    converts its 'stream' from byte to string then to a list of strings 
    which are separated by its newline character.

    Parameter command: a list of properly separated by commas, strings that are commands used in the terminal.
    Precondition command: a list containing strings seperated by commas that are posix command based.
    """
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    process.wait()
    process_stream_to_str = str(process.communicate()[0], "UTF-8")
    process_string_to_lst = process_stream_to_str.split("\n")
    process.kill()
    if 'cat' in command:
        return cat_output_seperator_tool(process_string_to_lst)
    if 'find' in command:
        return find_sed_output_seperator_tool(process_string_to_lst)
    if 'awk' in command:
        return awk_output_seperator_tool(process_string_to_lst)


def cat_output_seperator_tool(list_of_strings: list[str]) -> defaultdict[list]:
    """
    Returns a defaultdict from a list of output strings from a
    """
    TEMPLATE = defaultdict(list)
    for string in list_of_strings:
        colon = string.find(":")
        keys = string[:colon].strip("\t")
        values = string[colon+2:]
        TEMPLATE[keys].append(values.strip(" "))
    TEMPLATE.pop("")
    return TEMPLATE


def find_sed_output_seperator_tool(list_of_strings: list[str]) -> defaultdict:
    TEMPLATE = defaultdict()
    for string in list_of_strings:
        colon = string.find(":")
        slash = string.find("/",12)
        rslash = string.rfind("/")
        dir_names = string[slash+1:rslash].replace("/", " ").strip("\x00")
        file_names = string[string.rfind("/"):colon].strip("\x00").replace("/"," ")
        keys = dir_names + file_names
        values = string[colon+1:].replace("\t", " ")
        TEMPLATE.update({keys:values})
    TEMPLATE.pop("")
    return TEMPLATE


def awk_output_seperator_tool(list_of_strings: list[str]) -> defaultdict:
    TEMPLATE = defaultdict()
    print(list_of_strings)
    for string in list_of_strings:
        print(string)
        colon = string.find(":")
        keys = string[:colon]
        values = string[colon+1:]
        TEMPLATE.update({keys:values})
    TEMPLATE.pop("")
    return TEMPLATE
