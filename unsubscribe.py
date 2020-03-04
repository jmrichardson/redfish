import json
from rf.rf import rf

# Setup POST
sid=113
url = "/redfish/v1/EventService/Subscriptions" + "/" + str(sid)
headers = {'Content-Type': 'application/json'}

# Submit
response = rf.delete(url, headers=headers)

if response.status == 200:
    print("Status code 200: subscription successfully deleted")
else:
    print("Status code " + str(response.status) +": " + response.read)
