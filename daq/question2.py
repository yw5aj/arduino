import serial
import matplotlib.pyplot as plt

LEN = 10000
data = []
ser = serial.Serial('COM3', baudrate=2000000)
for i in range(LEN):
    try:
        data.append(int(ser.readline()))
    except:
        pass
ser.close()

# %% Plot data
plt.figure(figsize=(6, 4))
plt.plot(data)
plt.savefig('data.png')
