"""Usage: reboot.py [-s system] [-a account] [-p password] [-u iLO_https_url]

Reboot host

Options:
  -s system         System number [default: 1]
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
    if arguments['-s']: system = arguments['-s']
else:
    system = "1"

# Init redfish object
from rf.rf import rf

# POST body
body = dict()
body["Action"] = "ComputerSystem.Reset"
body["ResetType"] = "ForceRestart"

# Generate POST Path
path = "/redfish/v1/Systems/" + system + "/Actions/ComputerSystem.Reset/"

# POST
response = rf.redfish_post(path, body)
rf.error_handler(response)

