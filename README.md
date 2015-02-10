# RasPyCam

You'll need: 

		1. Rapsberry Pi (https://www.modmypi.com/shop/raspberry-pi-model-b-plus)	
		2. PIR Sensor (https://www.modmypi.com/pir-motion-sensor)
		3. Camera board(https://www.modmypi.com/raspberry-pi-noir-camera-board)
		4. SD Card with raspbian installed (http://www.raspberrypi.org/downloads/)


A python script for a motion activated camera


		1. Attach your PIR sensor to Pins 26, 6 and 2. (IO, Ground and 5V) 
		http://www.raspberrypi-spy.co.uk/wp-content/uploads/2013/01/pir_module_circuit_1.png
		(https://www.modmypi.com/blog/raspberry-pi-gpio-sensing-motion-detection)
		I did not use a breadboard, instead attaching directly. 
		2. Attach your Rapsberry Pi NoIR cammera to the camera ribbon 
		socket behind the ethernet port (Model B+).
		3. Install raspbian. (http://www.raspberrypi.org/downloads/)
		4. Clone this python script
		5. run "Sudo python motion.py"
To do: 

		Add email function

Kudos: 
		https://www.modmypi.com/blog/raspberry-pi-gpio-sensing-motion-detection
