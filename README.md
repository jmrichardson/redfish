### Installation

    # (Optional) Create clean python 3.6 environment
    conda create --name redfish python=3.6
    conda activate redfish 
    
    # Install
	git clone https://github.com/jmrichardson/redfish
	cd redfish
	pip install -r requirements.txt
	
	# Windows (C++ build tools)
	https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=BuildTools&rel=16

### Update config.py
    
    # Provide url, id and password
    vi rf/config.py
        iLO_https_url = "https://x.x.x.x" 
        iLO_account = "id"
        iLO_password = "pass"
       
        
### Examples

> Note: The example code utilizes a helper function "drill" to recursively traverse the API tree.  This significantly reduces the amount of boiler plate code and complexity required to find the appropriate API endpoint.  However, HPE provides [examples](https://github.com/HewlettPackard/python-ilorest-library) that can be used instead of this helper function.  
    

#### List Assets

    python assets.py

#### Update firmware

    # Edit firmware settings
    vi firmware.py
        update_repo = True
        update_target = False
        firmware = 'firmware/ilo/2.14/ilo5_214.bin'
        
    # Run firmware
    python firmware.py
    
#### Subscriptions

    # Start listener
    cd listener
    python RedfishEventListener_v1.py

    # In new window, update "Destination" field to listener IP address (your ip)
    vi json/subscription.json
    
    # Subscribe 
    python subscribe.py
    
    # List subscriptions
    python subscriptions
    
    # Send fake event
    python event.py
    
    # Unsubscribe with subscription id (sid)
    vi json/unsubscribe.py
    python unsubscribe.py 
    
#### List Drive Temperature Status

    python drive_thermal.py
   
   
#### Change boot order

    # Update device to bring to from of boot order.  Options include 'Usb', 'Cd', 'EmbeddedStorage', 'PcieSlotStorage', 'EmbeddedFlexLOM', 'PcieSlotNic', 'UefiShell'
    vi boot_order.py
    # device = 'Usb'
    
    python boot_order.py
    
