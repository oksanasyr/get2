import time
import RPi.GPIO as gpio

class R2R_ADC:
    def __init__ (self, dynamic_range, compare_time = 0.01, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        gpio.setmode(gpio.BCM)
        gpio.setup(self.bits_gpio, gpio.OUT, initial = 0)
        gpio.setup(self.comp_gpio, gpio.IN)

    def deinit(self):
        gpio.output(self.bits_gpio, 0)
        gpio.cleanup()

    def number_to_dac(self, number):
        number = [int(i) for i in bin(number)[2:].zfill(8)]
        gpio.output(self.bits_gpio, number)

    def sequential_counting_adc(self):
        max_number = 2**len(self.bits_gpio)-1
        for number in range(max_number+1):
            self.number_to_dac(number)
            time.sleep(self.compare_time)

            if gpio.input(self.comp_gpio) == 1:
                return number
        return max_number

    def get_sc_voltage(self):
        number = self.sequential_counting_adc()
        voltage = number / (2**len(self.bits_gpio)-1) * self.dynamic_range
        if self.verbose:
            print(f"Число {number}, нарпяжение: {voltage:.3f} В")
        return voltage


if __name__ == "__main__":
    adc = R2R_ADC(3.3, verbose=False)
    try:
        while True:
             voltage = adc.get_sc_voltage()
    finally:
        adc.deinit()