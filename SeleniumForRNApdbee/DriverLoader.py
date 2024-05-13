"""This module loads the selenium driver from the resource directory depending on the operating system"""

import sys
import os
import logging


def get_selenium_driver_path():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('DriverLoader')
    here = os.path.dirname(__file__)
    
    if sys.platform == 'win32':
        gecko_driver = os.path.join(here, 'driver', 'geckodriver_win.exe')
    elif sys.platform == 'darwin':
        gecko_driver = os.path.join(here, 'driver', 'geckodriver_mac')
    elif sys.platform.startswith('linux'):
        gecko_driver = os.path.join(here, 'driver', 'geckodriver_linux')
    else:
        raise Exception("Unsupported operating system.")

    logger.info("Init GeckoDriver: {} for {}".format(gecko_driver, sys.platform))
    return gecko_driver
