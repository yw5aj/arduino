import serial
import time
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    ser = serial.Serial('COM3', baudrate=115200)
    f = open('data.csv', 'w')
    ser.readline()
    time0 = time.time()
    datalen = 1000
    data = np.zeros(datalen, dtype=int)
    for i in range(datalen):
        try:
            data[i] = int(ser.readline())
        except ValueError:
            pass
    time1 = time.time()
    ser.close()
    f.close()
    fs = datalen / (time1 - time0)
