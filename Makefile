install:
	sudo apt-get install libasound2-dev
	sudo apt-get install libjack-dev
	pip3 install -r requirements.txt
run:
	sudo pigpiod
	python3 midi2gpio.py
