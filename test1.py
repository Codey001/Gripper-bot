#sample to test the data transfer from pyqt to arduino

import sys
from PyQt5.QtCore import Qt, QIODevice
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel, QHBoxLayout, QLineEdit
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo

class SerialCommunication(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.serial_port = QSerialPort()

        self.lbl_status = QLabel('Status: Not Connected')
        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)

        self.btn_connect = QPushButton('Connect', self)
        self.btn_connect.clicked.connect(self.connect_serial)

        self.btn_send = QPushButton('Send Data', self)
        self.btn_send.clicked.connect(self.send_data)

        self.line_edit = QLineEdit(self)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.lbl_status)
        self.layout.addWidget(self.text_edit)
        self.layout.addWidget(self.line_edit)
        self.layout.addWidget(self.btn_send)
        self.layout.addWidget(self.btn_connect)

        self.setWindowTitle('Serial Communication')
        self.setGeometry(300, 300, 400, 300)
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
                self.serial_port.readyRead.connect(self.receive_data)
            else:
                self.lbl_status.setText(f'Error: Could not open {port_name}')

    def send_data(self):
        if self.serial_port.isOpen():
            data = self.line_edit.text()
            self.serial_port.write(data.encode())
            self.line_edit.clear()

    def receive_data(self):
        while self.serial_port.canReadLine():
            data = self.serial_port.readLine().data().decode()
            self.text_edit.append(f'Received: {data}')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    serial_app = SerialCommunication()
    sys.exit(app.exec_())
