"""This file is included with SystemParser in order to obtain system information
Copyright (C) 2022 AERivas

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

This file contains a dictionary whose keys contain a value which is a list 
separated by commas containing a powershell module and cmdlets.

Information on powershell: https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.2
Information on powershell module and cmdlets: https://docs.microsoft.com/en-us/powershell/module/cimcmdlets/?view=powershell-7.2"""


WINDOWS_ACCEPTED_ARGS: tuple[str] = (
    "motherboard",
    "bus",
    "processor",
    "memory",
    "sound_device",
    "floppy_controller",
    "ide_controller",
    "pcmcia_controller",
    "usb_hub",
    "usb_controller",
    "usb_controller_device",
    "parallel_port",
    "serial_port",
    "serial_port_settings",
    "serial_port_configurations",
    "video_controller",
    "video_settings",
    "video_configurations",
    "list_environment_variables",
)

POWERSHELL_COMMANDS: dict[str, tuple[str]] = {
    WINDOWS_ACCEPTED_ARGS[0]: (
        'PowerShell.exe', 
        'Get-CimInstance', 
        '-ClassName', 
        'Win32_MotherboardDevice | Format-List'
    ),
    WINDOWS_ACCEPTED_ARGS[1]:  (
        'PowerShell.exe', 
        'Get-CimInstance', 
        '-ClassName',
        'Win32_Bus | Format-List'
    ),
    WINDOWS_ACCEPTED_ARGS[2]:  (
        'PowerShell.exe',
        'Get-CimInstance',
        '-ClassName',
         'Win32_Processor | Format-List'
    ),
    WINDOWS_ACCEPTED_ARGS[3]:  (
        'PowerShell.exe',
        'Get-CimInstance', 
        '-ClassName', 
        'Win32_MemoryArray | Format-List'
    ),
    WINDOWS_ACCEPTED_ARGS[4]: (
        'PowerShell.exe', 
        'Get-CimInstance', 
        '-ClassName', 
        'Win32_SoundDevice | Format-List'
    ),
    WINDOWS_ACCEPTED_ARGS[5]: (
        'PowerShell.exe', 
        'Get-CimInstance', 
        '-ClassName', 
        'Win32_FloppyController | Format-List'
    ),
    WINDOWS_ACCEPTED_ARGS[6]: (
        'PowerShell.exe', 
        'Get-CimInstance', 
        '-ClassName', 
        'Win32_IDEController | Format-List'
    ),
    WINDOWS_ACCEPTED_ARGS[7]: (
        'PowerShell.exe', 
        'Get-CimInstance', 
        '-ClassName', 
        'Win32_PCMCIAController | Format-List'
    ),
    WINDOWS_ACCEPTED_ARGS[8]: (
        'PowerShell.exe', 
        'Get-CimInstance', 
        '-ClassName', 
        'Win32_USBHub | Format-List'
    ),
    WINDOWS_ACCEPTED_ARGS[9]:  (
        'PowerShell.exe',
        'Get-CimInstance',
        '-ClassName',
        'Win32_USBController | Format-List'
    ),
    WINDOWS_ACCEPTED_ARGS[10]:  (
        'PowerShell.exe',
        'Get-CimInstance',
        '-ClassName', 
        'Win32_USBControllerDevice | Format-List'
    ),
    WINDOWS_ACCEPTED_ARGS[11]: (
        'PowerShell.exe',
        'Get-CimInstance', 
        '-ClassName', 
        'Win32_ParallelPort | Format-List'
    ),
    WINDOWS_ACCEPTED_ARGS[12]:   (
        'PowerShell.exe', 
        'Get-CimInstance', 
        '-ClassName', 'Win32_SerialPort | Format-List'
    ),
    WINDOWS_ACCEPTED_ARGS[13]: (
        'PowerShell.exe', 
        'Get-CimInstance', 
        '-ClassName', 
        'Win32_SerialPortSettings | Format-List'
    ),
    WINDOWS_ACCEPTED_ARGS[14]: (
        'PowerShell.exe', 
        'Get-CimInstance', 
        '-ClassName', 
        'Win32_SerialPortConfiguration | Format-List'
    ),
    WINDOWS_ACCEPTED_ARGS[15]: (
        'PowerShell.exe', 
        'Get-CimInstance', 
        '-ClassName', 
        'Win32_VideoController | Format-List'
    ),
    WINDOWS_ACCEPTED_ARGS[16]: (
        'PowerShell.exe', 
        'Get-CimInstance', 
        '-ClassName', 
        'Win32_VideoConfiguration | Format-List'
    ),
    WINDOWS_ACCEPTED_ARGS[17]:  (
        'PowerShell.exe', 
        'Get-CimInstance', 
        '-ClassName', 
        'Win32_VideoSettings | Format-List'
    ),
    WINDOWS_ACCEPTED_ARGS[-1]: (
        'PowerShell.exe', 
        'Get-ChildItem', 
        'Env:* | Format-List'
        #'Env:* | Select-Object -Property Name,Value'
    )
}
