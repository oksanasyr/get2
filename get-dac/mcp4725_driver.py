import smbys

class MCP4725:
    def __init__(self, dynamic_range, address = 0x61, verbose = True):
        self.bus = smbus.SMBus(1)
        self.address = address 
        self.pwm = 0x00
        self.pds = 0x00
        self.verbose = verbose 
        self.dynamic_range = dynamic_range
    
    def deinit(self):
        self.bus.close()
    
    def set_number(self, number):
        if not isinstance((number, int):
            print("На вход можно подавать только целые числа")
            return
        if not (0 <= voltage <= 4095):
            print("Число выходит за разрядность MCP4725 (12 bit ) ")
            return
        first_byte = self.wm | self.pds | (number >> 8)
        second_byte = number & 0xFF
        self.bus.write_byte_data(self.address, first_byte, second_byte)

        if self.verbose:
            print(f"число: {number},отправленные по I2C данные : [0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]\n")
    
    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} B)")
            print( "Устанавливаем 0.0 В")
            self.set_number(0)
            return 
        
        number = int( voltage / self.dynamic_range *4095)
        self.set_number(number) 

    if __name__ == "__main__":
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, True)
        try:
            while True:
                try:
                    voltage = float(input("Введите нпряжение в вольтах: "))
                    dac.set_voltage(voltage)
                except ValueError:
                    print("Вы ввели не число")
        finally:
            dac.deinit()      