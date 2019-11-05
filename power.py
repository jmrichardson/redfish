"""Usage: power.py [-a account] [-p password] [-u iLO_https_url]

Show power consumption

Options:
  -a account        ILO account
  -p password       ILO password
  -u iLO_https_url  ILO HTTPS URL (ie. https://X.X.X.X)
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

# Import drill function to iterate API
from rf.rf import drill

drill('/redfish/v1/Chassis/*Members*/Power/', [
    ['PowerControl', 'PowerCapacityWatts'],
    ['PowerControl', 'PowerConsumedWatts'],
    ['PowerControl', 'PowerMetrics/AverageConsumedWatts']
])


