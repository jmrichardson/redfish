### Install

	create --name redfish python=3.6
	conda activate redfish
	pip install python-ilorest-library
	wget https://downloads.hpe.com/pub/softlib2/software1/pubsw-windows/p1463761240/v150722/ilorest_chif.dll
	git clone https://github.com/jmrichardson/redfish
	cd redfish
	pip install -r requirements.txt
	# Be sure to put the above DLL in your environment path

