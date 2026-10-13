import RPi.GPIO as GPIO
import time

class R2R_ADC:
    def __init__(self, dynamic_range, compare_time = 0.005, verbose = False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.compare_time = compare_time
        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial = 0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self): 
        GPIO.output(self.bits_gpio, 0)
        GPIO.cleanup()

    def number_to_dac(self, number):
        number = max(0, min(255, int(number)))
        bits = [int(bit) for bit in bin(number)[2:].zfill(8)]
        GPIO.output(self.bits_gpio, bits)

    def sequential_counting_adc(self):
        for number in range(256):
            self.number_to_dac(number)
            time.sleep(self.compare_time)

            if not GPIO.input(self.comp_gpio):
                if self.verbose:
                    print(f"Сработал компаратор на числе: {number}")
                return number
        return 255

    def get_voltage(self):
        number = self.sequential_counting_adc()
        voltage = number/ 255 * self.dynamic_range

        if self.verbose:
            print(f"Число ЦАП :{number}, Напряжение: {voltage:.3f}B")

        return voltage




if __name__ == "__main__":
    adc = R2R_ADC(3.183, 0.005, True)

    try:
        while True:
            voltage = adc.get_voltage()
            print(f"Измерение напряжения: {voltage:.3f} B\n")
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nИзмерение остановлено")
    finally:
        adc.deinit()  