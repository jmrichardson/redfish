from rf.rf import rf

url = "/redfish/v1/systems/1/"
headers = {'Content-Type': 'application/json'}
body = {"HostName": "faredge.verizon.com"}

response = rf.patch(url, body, headers=headers)

print(response.status)
print(response.read)

