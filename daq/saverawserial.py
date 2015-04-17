# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import serial
import time


if __name__ == '__main__':
    ser = serial.Serial('COM3', baudrate=200000)
    time0 = time.time()
    f = open('data', 'w')
    while (time.time() - time0 < 6):
        f.write(ser.read().decode('ascii'))
        f.flush()
    ser.close()
    f.close()
    # %% Plot data
    import matplotlib.pyplot as plt
    import numpy as np
    data = np.loadtxt('data', delimiter=',')
    plt.plot(data)
