from rf.rf import update, rf

# Set variables
update_repo = True
update_target = False
firmware = 'firmware/ilo/2.14/ilo5_214.bin'
# firmware = 'firmware/ilo/1.4/ilo5_140.bin'

# Update firmware
update(rf, update_repo, update_target, firmware)


