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

"""

powershell_command = {
    'Bus':  ['PowerShell.exe', 'Get-CimInstance', '-ClassName', 'Win32_Bus | Format-List'],
    'Processor':  ['PowerShell.exe', 'Get-CimInstance', '-ClassName', 'Win32_Processor | Format-List'],
    'USBController':  ['PowerShell.exe', 'Get-CimInstance','-ClassName', 'Win32_USBController | Format-List'],
    'USBHub': ['PowerShell.exe', 'Get-CimInstance', '-ClassName', 'Win32_USBHub | Format-List'],
    'USBControllerDevice':  ['PowerShell.exe','Get-CimInstance', '-ClassName', 'Win32_USBControllerDevice | Format-List'],
    'ParallelPort': ['PowerShell.exe', 'Get-CimInstance', '-ClassName', 'Win32_ParallelPort | Format-List'],
    'MotherboardDevice': ['PowerShell.exe', 'Get-CimInstance', '-ClassName', 'Win32_MotherboardDevice | Format-List'],
    'MemoryArray':  ['PowerShell.exe', 'Get-CimInstance', '-ClassName', 'Win32_MemoryArray | Format-List'],
    'IDEController':    ['PowerShell.exe', 'Get-CimInstance', '-ClassName', 'Win32_IDEController | Format-List'],
    'PCMCIAController': ['PowerShell.exe', 'Get-CimInstance', '-ClassName', 'Win32_PCMCIAController | Format-List'],
    'FloppyController': ['PowerShell.exe', 'Get-CimInstance', '-ClassName', 'Win32_FloppyController | Format-List'],
    'SoundDevice': ['PowerShell.exe', 'Get-CimInstance', '-ClassName', 'Win32_SoundDevice | Format-List'],
    'VideoController': ['PowerShell.exe', 'Get-CimInstance', '-ClassName', 'Win32_VideoController | Format-List'],
    'VideoConfiguration': ['PowerShell.exe', 'Get-CimInstance', '-ClassName', 'Win32_VideoConfiguration | Format-List'],
    'VideoSettings':    ['PowerShell.exe', 'Get-CimInstance', '-ClassName', 'Win32_VideoSettings | Format-List'],
    'SerialPort':   ['PowerShell.exe', 'Get-CimInstance', '-ClassName', 'Win32_SerialPort | Format-List'],
    'SerialPortSettings':   ['PowerShell.exe', 'Get-CimInstance', '-ClassName', 'Win32_SerialPortSettings | Format-List'],
    'SerialPortConfiguration':  ['PowerShell.exe', 'Get-CimInstance', '-ClassName', 'Win32_SerialPortConfiguration | Format-List'],
    'EnvironmentVariables': ['PowerShell.exe', 'Get-CimChildItem', '-Path', 'env:\ | Format-List']
}
