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
# to be added Get-ChildItem -Path 'env:\'
 

# Must implement Network
