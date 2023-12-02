    def send_analog_data(self):
        if self.serial_port.isOpen():
            data = str(self.slider.value())
            # self.serial_port.write(data.encode())
            print(data)
            print("\n")
            print((data + '\n').encode())
            self.serial_port.write((data + '\n').encode())