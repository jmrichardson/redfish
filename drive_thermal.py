from rf.rf import drill

drill('/redfish/v1/Chassis/*Members*/*Links/Drives*/', [
    'Oem/Hpe/TemperatureStatus/Health',
    'Oem/Hpe/TemperatureStatus/State',
])


