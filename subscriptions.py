from rf.rf import rf

# Setup
url = "/redfish/v1/EventService/Subscriptions"
headers = {'Content-Type': 'application/json'}

# Submit
response = rf.get(url, headers=headers)

print(response.read)

