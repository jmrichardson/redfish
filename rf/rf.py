from rf.config import *
from rf._redfishobject import RedfishObject
from redfish.rest.v1 import ServerDownOrUnreachableError
import dpath.util

# Set configuration variables
iLO_https_url = iLO_https_url
iLO_account = iLO_account
iLO_password = iLO_password

# Create a REDFISH object
try:
    rf = RedfishObject(iLO_https_url, iLO_account, iLO_password)
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


