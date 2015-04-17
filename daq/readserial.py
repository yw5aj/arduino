# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import serial
import time
import matplotlib.pyplot as plt

if __name__ == '__main__':
    ser = serial.Serial('COM3', baudrate=921600)
    data = []
    rawdata = []
    flawdata = []
    time_ = []
    time0 = time.time()
    flag = 0
    while (time.time() - time0 < 12):
        try:
            rawdata.append(ser.readline())
            data.append(int(rawdata[-1]))
            time_.append(time.time() - time0)
        except ValueError:
            flag += 1
            flawdata.append(rawdata[-1])
            pass
    ser.close()
    fig, axs = plt.subplots(figsize=(6, 4))
    axs.plot(data)
    axs.set_xlabel('Time (s)')
    axs.set_ylabel('Data (0-1023)')
    fig.savefig('temp.png', dpi=300)
    print(len(data) / (time_[-1] - time_[0]))
