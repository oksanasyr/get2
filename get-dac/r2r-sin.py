import r2r_dac as r2r
import signal_generator as sg
import time
#import RPi.GPIO as GPIO


amplitude = 3.0
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    dac = r2r.R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, False)
    try:    
        start_time= time.time()
        while True:
            curr_time = time.time() - start_time
            ampl = sg.get_sin_wave_amplitude(signal_frequency, curr_time)
            voltage = ampl*amplitude
            dac.set_voltage(voltage)
            sg.wait_for_sampling_period(sampling_frequency)
    finally:
        dac.deinit()
