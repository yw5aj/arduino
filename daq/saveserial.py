# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import serial


if __name__ == '__main__':
    with serial.Serial('COM4', baudrate=1000000) as ser:
        with open('data.dat', 'wb') as f:
            for i in range(1000):
                data = ser.read(1000)
                f.write(data)
                f.flush()
    # %% Plot data
    import matplotlib.pyplot as plt
    import numpy as np
    with open('data.dat', 'rb') as f:
        rawbytedata = f.read()
    bytedata = rawbytedata.split(b'\n')[10:-10]
    data = np.array(bytedata, dtype='int')
    plt.plot(data * 1e-6, np.r_[0, np.diff(data)])
