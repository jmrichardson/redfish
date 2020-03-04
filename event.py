import json
from rf.rf import rf

url = "/redfish/v1/EventService/Actions/EventService.SubmitTestEvent"
headers = {'Content-Type': 'application/json'}

with open('json/event.json') as json_file:
    body = json.load(json_file)

response = rf.post(url, body, headers=headers)
print(response.status)
print(response.read)

