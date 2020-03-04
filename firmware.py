import os
import json
from rf.rf import rf

# Upload to iLO repository
update_repo = True
# Update firmware
update_target = False
# Firmware file location
firmware = 'firmware/ilo/2.14/ilo5_214.bin'
# firmware = 'firmware/ilo/1.4/ilo5_140.bin'

### Do not edit below ###

# Update firmware
update_service_uri = rf.root.obj['UpdateService']['@odata.id']
update_service_response = rf.get(update_service_uri)
path = update_service_response.obj.HttpPushUri

body = []
json_data = {'UpdateRepository': update_repo, 'UpdateTarget': update_target, 'ETag': 'atag', 'Section': 0}
session_key = rf.session_key

filename = os.path.basename(firmware)
with open(firmware, 'rb') as fle:
    output = fle.read()

session_tuple = ('sessionKey', session_key)
parameters_tuple = ('parameters', json.dumps(json_data))
file_tuple = ('file', (filename, output, 'application/octet-stream'))

# Build the payload from each multipart-form data tuple
body.append(session_tuple)
body.append(parameters_tuple)
body.append(file_tuple)

header = {'Cookie': 'sessionKey=' + session_key}

print("Processing ...")
resp = rf.post(path, body, headers=header)
print("Done.")

