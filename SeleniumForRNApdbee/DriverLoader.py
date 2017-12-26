import sys
import os
import logging


def get_selenium_driver_path():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger('DriverLoader')
    here = os.path.dirname(__file__)
    if sys.platform == 'win32':
        phantom_js = os.path.join(here, 'driver', 'phantomjs_win.exe')
    elif sys.platform == 'darwin':
        phantom_js = os.path.join(here, 'driver', 'phantomjs_mac.exe')
    elif sys.platform == 'linux2':
        phantom_js = os.path.join(here, 'driver', 'phantomjs_linux.exe')
    else:
        raise Exception("Do not supported operating system.")

    logger.info("Init phantomjs driver: {} for {}".format(phantom_js, sys.platform))
    return phantom_js
