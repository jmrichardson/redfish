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
def drill(path, keys, indent=0):
    urls = ['/']
    terms = path.split('*')[:-1]
    if len(terms):
        for url, od in zip(terms[0::2], terms[1::2]):
            new_urls = []
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
    for url in urls:
        res = rf.redfish_get(url)
        for key in keys:
            if isinstance(key, list):
                dres = dpath.util.get(res.dict, key[0])
            else:
                dres = dpath.util.get(res.dict, key)
            if isinstance(dres, list):
                for idx in dres:
                    print(" " * indent + f"{'/'.join(map(str, key))}: {dpath.util.get(idx, key[1])}")
            else:
                print(" "*indent + f"{key}: {dres}")


