#sample code to test the led on and off

import sys
from PyQt5.QtCore import Qt, QIODevice
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo

class ArduinoLEDControl(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.serial_port = QSerialPort()

        self.lbl_status = QLabel('Status: Not Connected')
        self.btn_connect = QPushButton('Connect', self)
        self.btn_connect.clicked.connect(self.connect_serial)

        self.btn_led_on = QPushButton('Turn On LED', self)
        self.btn_led_on.clicked.connect(self.turn_on_led)

        self.btn_led_off = QPushButton('Turn Off LED', self)
        self.btn_led_off.clicked.connect(self.turn_off_led)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.lbl_status)
        self.layout.addWidget(self.btn_connect)
        self.layout.addWidget(self.btn_led_on)
        self.layout.addWidget(self.btn_led_off)

        self.setWindowTitle('Arduino LED Control')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def connect_serial(self):
        if self.serial_port.isOpen():
            self.serial_port.close()
            self.lbl_status.setText('Status: Not Connected')
        else:
            port_name = "COM4"  # Change this to your Arduino's port
            self.serial_port.setPortName(port_name)

            if self.serial_port.open(QIODevice.ReadWrite):
                self.lbl_status.setText(f'Status: Connected to {port_name}')
            else:
                self.lbl_status.setText(f'Error: Could not open {port_name}')

    def turn_on_led(self):
        self.send_data('1')  # Send '1' to turn on the LED

    def turn_off_led(self):
        self.send_data('0')  # Send '0' to turn off the LED

    def send_data(self, data):
        if self.serial_port.isOpen():
            self.serial_port.write(data.encode())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    led_control_app = ArduinoLEDControl()
    sys.exit(app.exec_())
