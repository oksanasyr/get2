import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10,6))
    plt.plot(time, voltage, label = "Напряжение на АЦП")
    plt.xlabel("время")
    plt.ylabel("напряжение")
    plt.title("напряжение на ацп")
    plt.grid(True)
    plt.show()
    plt.xlim(0, max(time) if time else 1)
    plt.ylim(0, max_voltage)
