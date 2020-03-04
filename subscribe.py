import json
from rf.rf import rf

# Setup POST
url = "/redfish/v1/EventService/Subscriptions"
headers = {'Content-Type': 'application/json'}
with open('json/subscription.json') as json_file:
    body = json.load(json_file)

# Submit
response = rf.post(url, body, headers=headers)

if response.status == 201:
    print("Status code 201: subscription successfully set for EventService")
else:
    print("Status code " + str(response.status) +": " + response.read)
