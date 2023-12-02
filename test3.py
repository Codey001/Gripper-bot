import sys
from PyQt5.QtCore import Qt, QIODevice
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QSlider

from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo

class AnalogDataSender(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.serial_port = QSerialPort()

        self.lbl_status = QLabel('Status: Not Connected')
        self.btn_connect = QPushButton('Connect', self)
        self.btn_connect.clicked.connect(self.connect_serial)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(1023)  # Assuming the analog data range is 0-1023
        self.slider.valueChanged.connect(self.send_analog_data)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.lbl_status)
        self.layout.addWidget(self.btn_connect)
        self.layout.addWidget(self.slider)

        self.setWindowTitle('Analog Data Sender')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def connect_serial(self):
        if self.serial_port.isOpen():
            self.serial_port.close()
            self.lbl_status.setText('Status: Not Connected')
        else:
            port_name = "COM3"  # Change this to your Arduino's port
            self.serial_port.setPortName(port_name)

            if self.serial_port.open(QIODevice.ReadWrite):
                self.lbl_status.setText(f'Status: Connected to {port_name}')
            else:
                self.lbl_status.setText(f'Error: Could not open {port_name}')

    def send_analog_data(self):
        if self.serial_port.isOpen():
            data = str(self.slider.value())
            # self.serial_port.write(data.encode())
            print(data)
            print("\n")
            print((data + '\n').encode())
            self.serial_port.write((data + '\n').encode())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    analog_sender_app = AnalogDataSender()
    sys.exit(app.exec_())
