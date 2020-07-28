import mido
from gpio_interface import GPIOInterface



class MIDI2GPIO:
    """
    Class to receive MIDI from virtual port and send to GPIO 
    """

    port_name = 'PY-MIDI-IN-PORT'
    gpio_interface = GPIOInterface()

    def __init__(self):
        self.open_port(self.port_name)

    def receive_msg(self, port):
        """
        Keep program alive receiving MIDI messeges
        """
        while True:
            msg = port.receive()
            print(msg)
            self.gpio_interface.enqueue_message(msg)
        
    def open_port(self, port_name):
        """
        Opens Virtual MIDI PORT
        """
        port = mido.open_input(port_name, virtual=True)
        print('Port' + port_name + ' Running...')
        self.receive_msg(port)

MIDI2GPIO()
