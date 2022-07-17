import platform
import sys
from the_factory import thefactory

WINDOWS_ACCEPTED_ARGS = [
    'bus',
    'processor',
    'network',
    'memory',
    'drivers',
    'sound',
    'usb',
    'floppy',
    'ide',
    'pcmcia',
    'usb',
    'parallel',
    'serial',
    'graphics',
    ]
LINUX_ACCEPTED_ARGS = [
    'bios',
    'processor',
    'network',
    'memory',
    'drivers',
    'check_vuln',
    'power',
    '',
    '',
    '',
    '',
    '',
    ]
operating_system = thefactory.get_os()

def main(args: list[str]):
    if operating_system == 'Windows':
        print(f"The following commands are for the {operating_system} system:", *WINDOWS_ACCEPTED_ARGS, sep=" ")
        w = thefactory.WinRig()
        for arguement in args:
            try:
                if arguement == 'bus':
                    w.get_bus_information()
                if arguement == 'processor':
                    w.get_processor_information()
                if arguement == 'network':
                    w.get_network_information()
                if arguement == 'memory':
                    w.get_memory_information()
                if arguement == 'drivers':
                    w.get_driver_information()
                if arguement == 'sound':
                    w.get_sound_device_information()
                if arguement == 'usb':
                    w.get_usb_port_information()
                if arguement == 'floppy':
                    w.get_floppy_drive_information()
                if arguement == 'ide':
                    w.get_ide_controller_information()
                if arguement == 'pcmcia':
                    w.get_pcmcia_controller_information()
                if arguement == 'usb':
                    w.get_usb_port_information()
                if arguement == 'parallel':
                    w.get_parallel_port_information()
                if arguement == 'serial':
                    w.get_serial_port_information()
                if arguement == 'graphics':
                    w.get_graphic_card_information()
                if arguement not in WINDOWS_ACCEPTED_ARGS:
                    print(f"The provided arguement [{arguement}] is invalid, please run again.")
                    raise
            finally:
                sys.exit(0)
     
    if operating_system == 'Linux':
        print(f"The following commands are for the {operating_system} system:", *LINUX_ACCEPTED_ARGS, sep=" ")
        x = thefactory.NixRig()
        for arguement in args:   
            try:     
                if arguement == 'bios':
                    x.get_smbios_information()
                if arguement == 'processor':
                    x.get_processor_information()
                if arguement == 'network':
                    x.get_network_information()
                if arguement == 'memory':
                    x.get_memory_information()
                if arguement == 'drivers':
                    x.get_driver_information()
                if arguement == 'check_vuln':
                    x.get_cpu_vuln_information()
                if arguement == 'power':
                    x.get_power_information()
                if arguement not in LINUX_ACCEPTED_ARGS:
                    print(f"The Provided arguement [{arguement}] is invalid, please run again.")
            finally:
                sys.exit(0)

    if operating_system == 'Darwin':
        print(f"Implementation coming soon for the {operating_system} environment")
        raise