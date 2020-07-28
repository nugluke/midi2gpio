import queue
import threading

import pigpio
import serial


def set_midi_baudrate(midi_baudrate):
    """
    Set gpio baudrate to 31250
    """
    serial.Serial(
        port="/dev/ttyAMA0",
        baudrate=midi_baudrate,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=1,
    )


class GPIOInterface:
    """
    Class to handle gpio communication
    """

    gpio_pin = 16
    MIDI_BAUDRATE = 31250

    def __init__(self):
        self.message_buffer = queue.Queue()
        # set_midi_baudrate(self.MIDI_BAUDRATE)

        self.pi_instance = pigpio.pi()
        self.pi_instance.set_mode(self.gpio_pin, pigpio.OUTPUT)
        self.pi_instance.callback(self.gpio_pin, pigpio.FALLING_EDGE, self.send_message)

        


    def enqueue_message(self, message):
        """
        Adds message to queue
        """
        self.message_buffer.put(message.bytes())

    def send_message(self, gpio=0, level=0, tick=0):
        """
        Sends message from queue to pin
        """
        message = self.message_buffer.get()
        self.send_to_pin(message)
        print(message)

    def send_to_pin(self, message):
        """
        Sends message to gpio pin
        """
        self.pi_instance.wave_clear()
        self.pi_instance.wave_add_new()
        self.pi_instance.wave_add_serial(self.gpio_pin, self.MIDI_BAUDRATE, message)
        wid = self.pi_instance.wave_create()
        self.pi_instance.wave_send_once(wid)
