import time
import r2r_adc as adc_mod 
import adc_plot 


voltage_values = []
time_values = []
duration = 3.0

if __name__ == "__main__":
    adc = adc_mod.R2R_ADC(3.3, verbose=False)

    try:
        t_0 = time.time()

        while time.time() - t_0 < duration:
            voltage = adc.get_sc_voltage()
            voltage_values.append(voltage)
            time_values.append(time.time() - t_0)
        adc_plot.plot_voltage_vs_time(time_values, voltage_values, adc.dynamic_range)
    finally:
        adc.deinit()






















        