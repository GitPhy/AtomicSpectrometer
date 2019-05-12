import serial
import time
from time import sleep
import numpy as np
import matplotlib.pyplot as plt
import re

def  recv(serial):
    while True:
        data = serial.readline()
        # print(data)
        sleep(1/5)  #降低速度
        if data == '':
            continue
        else:
            break
    return data

if __name__ == '__main__':

    serial = serial.Serial('COM3', 115200, timeout=0.5)  #/dev/ttyUSB0

    # KK=0
    TempRec = []
    PresRec = []
    TimeRec = []
    StyleTime = []
    RecData = []

    if serial.isOpen() :
        print("open success")
    else :
        print("open failed")
    try:
        while True:
            data =recv(serial)
            if data != b'':
                # print("receive : ",data)
                data = data.decode('utf-8')
                # b' temp: 28.44 degC pres: 901.29 mbar\r\n'
                TempPattern = re.compile(r'(?<=temp: )\d+\.?\d*')
                TempText = TempPattern.findall(data)
                Temp = TempText[0]
                Temp = float(Temp)
                TempRec.append(Temp)

                PresPattern = re.compile(r'(?<=pres: )\d+\.?\d*')
                PresText = PresPattern.findall(data)
                Pres = PresText[0]
                Pres = float(Pres)
                PresRec.append(Pres)

                TimeRec.append(int(time.time()))
                # np.save('kk.txt', TimeRec)

                RecData.append(Temp)
                RecData.append(Pres)
                RecData.append(int(time.time()))

                FileHandle = open('A1.txt', mode='w')
                FileHandle.write(str(RecData))
                FileHandle.close

                NumTick = 6
                TimeTick = np.linspace(TimeRec[0], TimeRec[-1], NumTick)
                TimeTickLabel = []
                NN = 0
                for NN in range(0, NumTick, 1):
                    ADA = time.asctime(time.localtime(TimeTick[NN]))
                    ADA = ADA[10:19]
                    TimeTickLabel.append(ADA)
                    NN = NN + 1

                plt.subplot(2, 1, 1)
                plt.plot(TimeRec, TempRec, color='r')
                plt.xticks(TimeTick, TimeTickLabel)
                plt.ylabel("Temperature(C)")
                plt.legend(['Temperature'])

                plt.subplot(2, 1, 2)
                plt.plot(TimeRec, PresRec)
                plt.xticks(TimeTick, TimeTickLabel)
                plt.ylabel("Pressure(mBar)")
                plt.legend(['Pressure'])

                plt.show()

                # serial.write(data) #数据写回
                sleep(0.1)
    except KeyboardInterrupt:
        print('计时完成')

