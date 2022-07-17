"""
A basic windows system information gathering tool using subprocess Popen, 
powershell commands and bespoke helper functions.

Returns an accumulatable(by value, not key) defaultdict 
containing the output information from a valid powershell command 
(a list of strings that are commands seperated by commas)

Example. ['PowerShell.exe', 'Get-CimInstance', '-ClassName', 'Win32_Processor']
the above example tells powershell to get a 'instance of a Win32 class object' 
in this case information about the local or remote systems processor.

*changes will be made periodically*
NOTE: https://docs.microsoft.com/en-us/windows/win32/cimwin32prov/win32-provider    

Author: AERivas
Date 07/09/2022
"""
import subprocess
from collections import defaultdict

def hide_process():
    """Returns information for a proccess startup to create no window when used with Popen and windows only"""
    startup_information = subprocess.STARTUPINFO()
    startup_information.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    startup_information.wShowWindow = subprocess.CREATE_NO_WINDOW
    return startup_information


def start_powershell_process(command: list[str]):
    """ 
    Starts a process based on above example of power shell commands
    separated strings by commas contained in a list. Converts the 
    process output (bytes) to a list of strings to be used for the program

    Parameter command: a list of strings seperated by commas.
    Precondition command: a valid Win32 provider class string (check examples)
    """
    process = subprocess.Popen(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        startupinfo=hide_process()
    )
    process.wait()
    stream_to_str = str(process.communicate()[0], 'UTF-8')
    stream_str_to_lst = stream_to_str.split("\r\n")
    process.kill()
    return parse_process(stream_str_to_lst)

def parse_process(lst_of_str: list[str]):
    """
    Returns a defaultdict from the started process.

    list of strings containing the information displayed (the output)
    from a the created powershell process.
    
    Parameter list_of_strings:
    Precondition list_of_strings:
    """
    TEMPLATE = defaultdict(list)
    for strings in lst_of_str:
        colon = strings.find(":")
        keys = strings[:colon].strip(" ")
        values = strings[colon+1:].strip(" ")
        TEMPLATE[keys].append(values)
    TEMPLATE.pop("")
    return TEMPLATE
   