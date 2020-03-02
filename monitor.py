from rf import config
from rf.rf import drill
import sys
from loguru import logger
from time import sleep

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

logger.remove()
logger.add(sys.stdout, format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | {message}")
logger.add(monitor_log, format="{time:YYYY-MM-DD HH:mm:ss} | {message}")

while True:
    for key, value in monitor.items():
        result = drill(key, value, output=False)
        for k, v in result.items():
            logger.info(f"{k}, {v}")
    sleep(monitor_frequency)


