"""Usage: assets.py [-a account] [-p password] [-u iLO_https_url]

Show asset inventory

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

# Get host assets
drill('/redfish/v1/Systems/*Members*', [
    'Model',
    'Manufacturer',
    'SerialNumber',
    'BiosVersion',
    'Oem/Hpe/PowerOnMinutes',
    # 'Oem/Hpe/HostOS/OsName',
    # 'Oem/Hpe/HostOS/OsVersion',
    'MemorySummary/TotalSystemMemoryGiB',
    'ProcessorSummary/Count',
    'ProcessorSummary/Model',
    'Oem/Hpe/SystemUsage/CPUUtil'
    ])
print("\nEthernet Interfaces:")
drill('/redfish/v1/Systems/*Members*/*EthernetInterfaces*/*Members*', [
    'Name',
    ['IPv4Addresses', 'Address'],
    'MACAddress',
    'SpeedMbps'
])
print("\nStorage:")
drill('/redfish/v1/Chassis/*Members*/*Links/Drives*', [
    'MediaType',
    ['Location', 'Info'],
    'CapacityBytes',
    'Model',
    'PredictedMediaLifeLeftPercent',
    'SerialNumber'
    ])
print("\nNetwork Adapters:")
drill('/redfish/v1/Chassis/*Members*/*NetworkAdapters*/*Members*', ['Model'])
print("\nPower:")
drill('/redfish/v1/Chassis/*Members*/*Power*', [
    ['PowerSupplies', 'Model'],
])


