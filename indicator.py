from rf.rf import rf
import sys

led = sys.argv[1]

url = "/redfish/v1/chassis/1/"
headers = {'Content-Type': 'application/json'}
body = {"IndicatorLED": led}

response = rf.patch(url, body, headers=headers)

print(response.status)
print(response.read)

