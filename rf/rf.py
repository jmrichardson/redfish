import os
import json
from rf.config import *
import redfish
# from rf._redfishobject import RedfishObject
# from redfish import RedfishClient
# from redfish.rest.v1 import ServerDownOrUnreachableError
import dpath.util

# Set configuration variables
iLO_https_url = iLO_https_url
iLO_account = iLO_account
iLO_password = iLO_password

# Create a REDFISH object
try:
    rf = redfish.RedfishClient(base_url=iLO_https_url, username=iLO_account, password=iLO_password)
    rf.login()

except ServerDownOrUnreachableError as excp:
    raise Exception("ERROR: server not reachable or doesn't support RedFish.\n")
except Exception as excp:
    raise excp


# Helper function to traverse API
def drill(path, keys, indent=0, output=True):
    urls = ['/']
    terms = path.split('*')
    if terms[-1] == '':
        terms = terms[:-1]
    if not (len(terms) % 2) == 0:
        terms.append("/")
    if len(terms):
        for url, od in zip(terms[0::2], terms[1::2]):
            new_urls = []
            if od == '/':
                for i, val in enumerate(urls):
                    new_urls.append(val + url)
            else:
                for i in urls:
                    uri = i + url
                    res = rf.redfish_get(uri)
                    dres = dpath.util.get(res.dict, od)
                    if isinstance(dres, dict):
                        dres = [dres]
                    for item in dres:
                        new_urls.append(item['@odata.id'])
            urls = new_urls
    else:
        urls = [path]
    result = {}
    # print(urls)
    for url in urls:
        res = rf.redfish_get(url)
        for key in keys:
            if isinstance(key, list):
                dres = dpath.util.get(res.dict, key[0])
            else:
                dres = dpath.util.get(res.dict, key)
            if isinstance(dres, list):
                for idx in dres:
                    value = dpath.util.get(idx, key[1])
                    if isinstance(key, list): k = '/'.join(map(str, key))
                    result[k] = value
                    if output: print(" " * indent + f"{k}: {value}")
            else:
                result[key] = {dres}
                if output: print(" "*indent + f"{key}: {dres}")

    return result


def update(rf, update_repo, update_target, firmware):

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
    return resp


