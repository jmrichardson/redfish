# Set default variables
iLO_https_url = "https://16.91.158.182"
iLO_account = "admin"
iLO_password = "admin"

# Monitor
monitor_log = 'logs/monitor.log'
monitor_frequency = 5
monitor = {
  '/redfish/v1/Systems/*Members*': [
    'Oem/Hpe/SystemUsage/CPUUtil',
    'Oem/Hpe/SystemUsage/MemoryBusUtil'
    ],
  '/redfish/v1/Chassis/*Members*': [
    'Status/Health'
  ]
}
