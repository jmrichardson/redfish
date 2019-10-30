"""Usage: monitor.py [-a account] [-p password] [-u iLO_https_url]

Reboot host

Options:
  -a account                ILO account
  -p password               ILO password
  -u iLO_https_url          ILO HTTPS URL (ie. https://X.X.X.X)
"""
from docopt import docopt
arguments = docopt(__doc__)

# Get default configuration
from rf import config

# Set config args if provided
if 'arguments' in locals():
    if arguments['-u']: config.iLO_https_url = arguments['-u']
    if arguments['-p']: config.iLO_password = arguments['-p']
    if arguments['-a']: config.iLO_account = arguments['-a']


# Init redfish object
from rf.rf import drill
import sys
from loguru import logger
from time import sleep

logger.remove()
logger.add(sys.stdout, format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | {message}")
logger.add(config.monitor_log, format="{time:YYYY-MM-DD HH:mm:ss} | {message}")

while True:
    for key, value in config.monitor.items():
        result = drill(key, value, output=False)
        for k, v in result.items():
            logger.info(f"{k}, {v}")
    sleep(config.monitor_frequency)


