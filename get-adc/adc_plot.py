import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage, label = "Напряжение на АЦП")
    plt.xlabel("время")
    plt.ylabel("напряжение")
    plt.title("напряжение на ацп")
    plt.grid(True)
    plt.xlim(0, max(time) if time else 1)
    plt.ylim(0, max_voltage)
    plt.show()

def plot_sampling_period_hist(time):
    sampling_periods = []
    for i in range(1, len(time)):
        sampling_periods.append(time[i] - time[i-1])
    plt.figure(figsize=(10,6))
    plt.hist(sampling_periods, bins = 30)
    plt.xlabel("Период измерения")
    plt.ylabel("Количество измерений")
    plt.title("распределение периодов измерений")
    plt.xlim(0, 0.06)
    plt.grid(True)
    plt.show()