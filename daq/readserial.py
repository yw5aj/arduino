# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import serial
import time
import matplotlib.pyplot as plt

if __name__ == '__main__':
    ser = serial.Serial('COM3', baudrate=1000000)
    data = []
    time_ = []
    time0 = time.time()
    flag = 0
    while (time.time() - time0 < 5):
        try:
            rawdata = ser.readline()
            data.append(int(rawdata))
            time_.append(time.time() - time0)
        except ValueError:
            flag += 1
            pass
    ser.close()
    fig, axs = plt.subplots(figsize=(6, 4))
    axs.plot(time_, data)
    axs.set_xlabel('Time (s)')
    axs.set_ylabel('Data (0-1023)')
    axs.set_ylim(0, 1024)
    fig.savefig('temp.png', dpi=300)
    print(len(data) / (time_[-1] - time_[0]))
