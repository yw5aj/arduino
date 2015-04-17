import serial
import time


if __name__ == '__main__':
    ser = serial.Serial('COM3', baudrate=1000000)
    time0 = time.time()
    f = open('data.csv', 'w')
    ser.readline()
    while (time.time() - time0 < 10):
        try:
            data = int(ser.readline())
            current_time = time.time() - time0
            f.write('%.8f, %d\n' % (current_time, data))
            f.flush()
        except ValueError:
            pass
    ser.close()
    f.close()
    # %% Plot data
    import matplotlib.pyplot as plt
    import numpy as np
    time_array, data_array = np.loadtxt('data.csv', delimiter=',').T
    plt.plot(time_array, data_array)
    plt.ylim(-100, 1500)
    plt.xlabel('Time (s)')
    plt.ylabel('Data (0-1023)')
    plt.tight_layout()
    plt.savefig('data_sensor_alone.png')
#    plt.close()
