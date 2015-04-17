# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import serial
import time


if __name__ == '__main__':
    ser = serial.Serial('COM3', baudrate=500000)
    time0 = time.time()
    flag = 0
    f = open('data.csv', 'w')
    single_byte = False
    if single_byte:
        ser.read()
    else:
        ser.readline()
    while (time.time() - time0 < 10):
        try:
            if single_byte:
                data = int.from_bytes(ser.read(), 'big')
            else:
                data = int(ser.readline())
            current_time = time.time() - time0
            f.write('%.8f, %d\n' % (current_time, data))
            f.flush()
        except ValueError:
            flag += 1
            pass
    ser.close()
    f.close()
    # %% Plot data
    import matplotlib.pyplot as plt
    import numpy as np
    time_array, data_array = np.loadtxt('data.csv', delimiter=',').T
    plt.plot(time_array, data_array)
    print(data_array.shape[0] / (time_array[-1] - time_array[0]))