from rf.rf import update, rf

# Upload to iLO repository
update_repo = True

# Update firmware
update_target = False

# Firmware file location
firmware = 'firmware/ilo/2.14/ilo5_214.bin'

# firmware = 'firmware/ilo/1.4/ilo5_140.bin'

# Update firmware
update(rf, update_repo, update_target, firmware)


