# Midi2GPIO

This module runs a virtual MIDI port using rtmidi and send received messages to RPI GPIO. Tested using RPI 3

## Installing

* Run `make install` in the project's folder.

## Running

* Set `GPIO_PIN` and `PORT_NAME` in `config.py` as you need
* Run `make run` in the project's folder. 
* Use `aconnect -l` to list your current MIDI ports and connect using `aconnect (your midi source:port) (midi port created by this module:port)`. Reference: https://linux.die.net/man/1/aconnect
