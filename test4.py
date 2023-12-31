import sys
from PyQt5.QtCore import Qt, QIODevice
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QSlider,
)

from PyQt5.QtSerialPort import QSerialPort

class AnalogDataSender(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.serial_port = QSerialPort()

        self.lbl_status = QLabel("Status: Not Connected")
        self.btn_connect = QPushButton("Connect", self)
        self.btn_connect.clicked.connect(self.connect_serial)

        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(180)  # Assuming the analog data range is 0-180
        self.slider.valueChanged.connect(self.send_analog_data)

        self.lbl_min = QLabel("Min: {}".format(self.slider.minimum()))
        self.lbl_max = QLabel("Max: {}".format(self.slider.maximum()))
        self.lbl_value = QLabel("Value: {}".format(self.slider.value()))


        font_status = QFont()
        font_status.setPointSize(11)  # Adjust the font size as needed
        self.lbl_status.setFont(font_status)

        # Increase the font size for value label
        font_value = QFont()
        font_value.setPointSize(11)  # Adjust the font size as needed
        self.lbl_value.setFont(font_value)

        slider_layout = QHBoxLayout()
        slider_layout.addWidget(self.lbl_min)
        slider_layout.addWidget(self.slider)
        slider_layout.addWidget(self.lbl_max)

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.lbl_status, alignment=Qt.AlignHCenter)
        self.layout.addWidget(self.btn_connect)
        self.layout.addWidget(self.lbl_value, alignment=Qt.AlignHCenter)
        self.layout.addLayout(slider_layout)

        self.setWindowTitle("Analog Data Sender")
        self.setGeometry(400, 400, 400, 400)
        self.show()

    def connect_serial(self):
        if self.serial_port.isOpen():
            self.serial_port.close()
            self.lbl_status.setText("Status: Not Connected")
        else:
            port_name = "COM3"  # Change this to your Arduino's port
            self.serial_port.setPortName(port_name)

            if self.serial_port.open(QIODevice.ReadWrite):
                self.lbl_status.setText(f"Status: Connected to {port_name}")
            else:
                self.lbl_status.setText(f"Error: Could not open {port_name}")

    def send_analog_data(self):
        if self.serial_port.isOpen():
            data = str(self.slider.value())
            self.lbl_value.setText("Value: {}".format(data))
            self.serial_port.write((data + "\n").encode())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    analog_sender_app = AnalogDataSender()
    sys.exit(app.exec_())
