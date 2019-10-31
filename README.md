### Install

	conda create --name redfish python=3.6
	conda activate redfish
	wget https://downloads.hpe.com/pub/softlib2/software1/pubsw-windows/p1463761240/v150722/ilorest_chif.dll
	# Be sure to put the above DLL in your environment path
	git clone https://github.com/jmrichardson/redfish
	cd redfish
	pip install -r requirements.txt

### Update config.py
    
    cd rf
    vi config.py
        iLO_https_url = "https://x.x.x.x" 

### Sample

    cd ..
    python assets.py

