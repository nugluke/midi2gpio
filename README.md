# Midi2GPIO

Python application that hosts a virtual MIDI port using rtmidi and sends received messages to Raspberry's GPIO. Tested using RPI 3

## Setting Up


* You will need a MIDI DIN connector, a 220Ω resistor and a MIDI cable to connect your RPI's GPIO to your synths. [This scheme works well](https://github.com/nugluke/midi2gpio/blob/master/assets/midi-out-schema.png). 
* Run `make install` in the project's folder.

## Running

* Set `GPIO_PIN` and `PORT_NAME` in `config.py` as you need
* Run `make run` in the project's folder. 
* Use `aconnect -l` to list your current MIDI ports and connect using `aconnect (your midi source:port) (midi port created by this application:port)`. Reference: https://linux.die.net/man/1/aconnect
