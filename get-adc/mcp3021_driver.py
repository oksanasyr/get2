import smbus
import time

class MCP3021:
    def __init__(self, dynamic_range, verbose = False):
        self.bus = smbus.SMBus(1)
        self.dynamic_range = dynamic_range
        self.address = 0x4D
        self.verbose = verbose
    def deinit(self):
        self.bus.close()
    def get_number(self):
        data = self.bus.read_word_data(self.address, 0)
        lower_data_byte = data >> 8
        upper_data_byte = data & 0xFF 
        number = (upper_data_byte << 6) | (lower_data_byte >> 2)
        if self.verbose:
            print(f"{data}, {upper_data_byte}, {lower_data_byte}, {number}")
        return number
    def get_voltage(self):
        number = self.get_number()
        voltage = (number * self.dynamic_range)/1024
        if self.verbose:
            print(f"{number}, {voltage:.3f}")
        return voltage

    

if __name__ == "__main__":
    try:
        adc = MCP3021(5.0, verbose=False)
        while True:
            voltage = adc.get_voltage 
            print(f" izmerennoe napryazhenie {voltage:.3f}")
            time.sleep(1)
    finally:
        adc.deinit()

