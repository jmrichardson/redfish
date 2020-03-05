### Install

    # (Optional) Create virtual python environment
	conda create --name redfish python=3.6
	conda activate redfish
	
    # Install redfish repo	
	git clone https://github.com/jmrichardson/redfish
	cd redfish
	pip install -r requirements.txt

### Update config.py
    
    # Provide url, id and password
    cd rf
    vi config.py
        iLO_https_url = "https://x.x.x.x" 
        iLO_account = "id"
        iLO_password = "pass"
        
        
### Examples

#### List Assets

    cd ..
    python assets.py

    # Note
    The example code utilizes a helper function "drill" to recursively traverse the API tree.  This significantly reduces the amount of boiler plate code and complexity required to find the appropriate API endpoint.  However, HPE provides [examples](https://github.com/HewlettPackard/python-ilorest-library) that can be used instead of this helper function.  

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

    # Update "Destination" field to listener IP address
    cd ..
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
   
    

