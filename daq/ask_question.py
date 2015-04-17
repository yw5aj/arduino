import serial
import time
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    ser = serial.Serial('COM3', baudrate=2000000)
    f = open('data.csv', 'w')
    ser.readline()
    time0 = time.time()
    for i in range(10000):
        try:
            data = float(ser.readline())
            current_time = time.time() - time0
            f.write('%f, %f\n' % (current_time, data))
            f.flush()
        except ValueError:
            pass
    time1 = time.time()
    ser.close()
    f.close()
    fs = 10000 / (time1 - time0)
    # %% Plot data
    time_array, data_array = np.loadtxt('data.csv', delimiter=',').T
    plt.figure(figsize=(6, 4))
    plt.plot(time_array, data_array)
#    plt.ylim(-100, 1500)
    plt.xlabel('Time (s)')
    plt.ylabel('Data (0-1023)')
    plt.tight_layout()
    plt.savefig('data.png')
