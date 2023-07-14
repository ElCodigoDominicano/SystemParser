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
Information on powershell module and cmdlets: https://docs.microsoft.com/en-us/powershell/module/cimcmdlets/?view=powershell-7.2
"""

POWERSHELL_COMMANDS: dict[str, tuple[str, ...]] = {
    "motherboard":(
        'PowerShell.exe', 
        'Get-CimInstance', 
        '-ClassName', 
        'Win32_MotherboardDevice | Format-List'
    ),
    "bus": (
        'PowerShell.exe', 
        'Get-CimInstance', 
        '-ClassName',
        'Win32_Bus | Format-List'
    ),
    "processor": (
        'PowerShell.exe',
        'Get-CimInstance',
        '-ClassName',
         'Win32_Processor | Format-List'
    ),
    "memory": (
        'PowerShell.exe',
        'Get-CimInstance', 
        '-ClassName', 
        'Win32_MemoryArray | Format-List'
    ),
    "sound_device":(
        'PowerShell.exe', 
        'Get-CimInstance', 
        '-ClassName', 
        'Win32_SoundDevice | Format-List'
    ),
    "floppy_controller":(
        'PowerShell.exe', 
        'Get-CimInstance', 
        '-ClassName', 
        'Win32_FloppyController | Format-List'
    ),
    "ide_controller":(
        'PowerShell.exe', 
        'Get-CimInstance', 
        '-ClassName', 
        'Win32_IDEController | Format-List'
    ),
    "pcmcia_controller":(
        'PowerShell.exe', 
        'Get-CimInstance', 
        '-ClassName', 
        'Win32_PCMCIAController | Format-List'
    ),
    "usb_hub":(
        'PowerShell.exe', 
        'Get-CimInstance', 
        '-ClassName', 
        'Win32_USBHub | Format-List'
    ),
    "usb_controller": (
        'PowerShell.exe',
        'Get-CimInstance',
        '-ClassName',
        'Win32_USBController | Format-List'
    ),
    "usb_controller_device":  (
        'PowerShell.exe',
        'Get-CimInstance',
        '-ClassName', 
        'Win32_USBControllerDevice | Format-List'
    ),
    "parallel_port": (
        'PowerShell.exe',
        'Get-CimInstance', 
        '-ClassName', 
        'Win32_ParallelPort | Format-List'
    ),
    "serial_port":   (
        'PowerShell.exe', 
        'Get-CimInstance', 
        '-ClassName', 'Win32_SerialPort | Format-List'
    ),
    "serial_port_settings": (
        'PowerShell.exe', 
        'Get-CimInstance', 
        '-ClassName', 
        'Win32_SerialPortSettings | Format-List'
    ),
    "serial_port_configurations": (
        'PowerShell.exe', 
        'Get-CimInstance', 
        '-ClassName', 
        'Win32_SerialPortConfiguration | Format-List'
    ),
    "video_controller": (
        'PowerShell.exe', 
        'Get-CimInstance', 
        '-ClassName', 
        'Win32_VideoController | Format-List'
    ),
    "video_settings": (
        'PowerShell.exe', 
        'Get-CimInstance', 
        '-ClassName', 
        'Win32_VideoConfiguration | Format-List'
    ),
    "video_configurations":  (
        'PowerShell.exe', 
        'Get-CimInstance', 
        '-ClassName', 
        'Win32_VideoSettings | Format-List'
    ),
    "list_environment_variables": (
        'PowerShell.exe', 
        'Get-ChildItem', 
        'Env:* | Format-List'
        #'Env:* | Select-Object -Property Name,Value'
    )
}
