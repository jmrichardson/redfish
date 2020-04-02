from rf.rf import rf

# Device to move to fron
device = 'Usb'

# Get current boot order
res = rf.get('/redfish/v1/systems/1/bios/boot/')
uri = res.obj['@Redfish.Settings']['SettingsObject']['@odata.id']
boot_order = res.obj['DefaultBootOrder']
print(f"Current boot order: {boot_order}")

# Change boot order
boot_order.insert(0, boot_order.pop(boot_order.index(device)))
print(f"Setting new boot order: {boot_order}")

# Update boot order
body = {'DefaultBootOrder': boot_order}
res = rf.patch(uri, body)

if res.status != 200:
    sys.stderr.write("An http response of \'%s\' was returned.\n" % res.status)
else:
    print("Success! Restart required.\n")

