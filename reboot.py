# Init redfish object
from rf.rf import rf

# POST body
body = dict()
body["Action"] = "ComputerSystem.Reset"
body["ResetType"] = "ForceRestart"

# Generate POST Path
path = "/redfish/v1/Systems/1/Actions/ComputerSystem.Reset/"

# POST
response = rf.post(path, body)
print("An http response of \'%s\' was returned.\n" % response.status)


