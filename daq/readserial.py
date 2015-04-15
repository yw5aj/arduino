# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import serial
import time
import matplotlib.pyplot as plt

if __name__ == '__main__':
    ser = serial.Serial('COM3', baudrate=200000)
    data = []
    time_ = []
    time0 = time.time()
    flag = 0
    while (time.time() - time0 < 5):
        try:
            data.append(int(ser.readline()))
            time_.append(time.time() - time0)
        except ValueError:
            flag += 1
            pass
    ser.close()
    plt.plot(time_, data)
    print(len(data) / (time_[-1] - time_[0]))
