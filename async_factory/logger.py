"""LogCenter - Used for debugging functions and classes in python
also contains a decorator function that displays a function execution time.
with added AnsiColors.

Author: AERivas
Date: 07/12/2023
"""
import time
import logging

from .ansi.ansi_colors import AnsiColors

class LogCenter(logging.Logger):
    def __init__(self, name, level=logging.NOTSET):
        super().__init__(name, level)
        console_handler = logging.StreamHandler()
        text = " %(levelname)s ~ [Time]: %(asctime)s ~ [Name]: %(name)s \
                ~ [Function Name]: %(funcName)s ~ [Filename]: %(filename)s \
                ~ [Pathname]: %(pathname)s ~ [Created]: %(relativeCreated)s \
                ~ [ProcessID]: %(process)s ~ [Module]: %(module)s ~ [Message]: %(message)s "
        formatter = ColorFormatter(text.replace("~", "\n"))
        console_handler.setFormatter(formatter)
        self.addHandler(console_handler)
    
    def log_info(self, message):
        self.info(message)
    
    def log_debug(self, message):
        self.debug(message)
    
    def log_warning(self, message):
        self.warning(message)
    
    def log_error(self, message):
        self.error(message)
    
    def log_critical(self, message):
        self.critical(message)
    
    def time_event(self, func):
        def wrapper(*args, **kwargs):
            func.__name__ = AnsiColors.BRIGHT_YELLOW + func.__name__ + AnsiColors.END_COLOR
            self.info("Starting ~{}~> function".format(func.__name__))
            start_time = time.time()
            result = func(*args, **kwargs)
            self.info("Function ~{}~> finished.".format(func.__name__))
            self.info("Execution took: ~{%.6f}~> seconds.", time.time() - start_time)
            return result
        return wrapper


class ColorFormatter(logging.Formatter):
    LEVEL_COLORS = {
        "DEBUG": AnsiColors.BRIGHT_GREEN ,
        "INFO": AnsiColors.BRIGHT_BLUE,
        "WARNING": AnsiColors.BRIGHT_YELLOW,
        "ERROR": AnsiColors.ORANGE,
        "CRITICAL": AnsiColors.BLINK + AnsiColors.BRIGHT_RED,
    }
    RECORD_COLORS = {
        "name": AnsiColors.SKY_BLUE,
        'exc_info': AnsiColors.LAWN_GREEN,
        'exc_text': AnsiColors.LIME_GREEN,
        'filename': AnsiColors.MINT_GREEN,
        'funcName': AnsiColors.PEAR_GREEN,
        'module': AnsiColors.SAGE_GREEN,
        'msg': AnsiColors.CHARTREUSE_GREEN,
        'pathname': AnsiColors.JUNGLE_GREEN,
        'process': AnsiColors.LIGHT_SEA_GREEN,
        'stack_info': AnsiColors.OLIVE_GREEN,
        'relativeCreated': AnsiColors.LIGHT_GREEN,
    }


    def format(self, record):
        levelname = record.levelname
        color = self.LEVEL_COLORS.get(levelname, "")
        record.levelname = f"{color}{levelname}{AnsiColors.END_COLOR}"
        for attribute, colors in self.RECORD_COLORS.items():
            gets = getattr(record, attribute)
            setattr(record, attribute, f"{colors}{gets}{AnsiColors.END_COLOR}")
        return super().format(record)