import pwm_dac as pwm
import signal_generator as sg
import time

amplitude = 1.4
signal_frequency = 10
sampling_frequency = 200
if __name__ == "__main__":
    dac = pwm.PWM_DAC(16, 500, 3.183, False)
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