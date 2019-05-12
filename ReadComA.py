import serial
import time
from time import sleep
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# labels='frogs','hogs','dogs','logs'
# sizes=15,20,45,10
# colors='yellowgreen','gold','lightskyblue','lightcoral'
# explode=0,0.1,0,0
# plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)
# plt.axis('equal')
# plt.show()


def recv(serial):
    while True:
        data = serial.readline()
        if data == '':
            continue
        else:
            break
        sleep(2)
    return data

if __name__ == '__main__':
    serial = serial.Serial('COM5', 115200, timeout=0.5)  #/dev/ttyUSB0
    # KK=0
    TempRec = []
    PresRec = []
    TimeRec = []
    StyleTime =[]
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
                Temp = data[6:12]
                Pres = data[24:30]
                Pres=float(Pres)
                PresRec.append(Pres)
                Temp=float(Temp)
                TempRec.append(Temp)
                TimeRec.append(int(time.time()))
                np.save('kk.txt',TimeRec)
                RecData.append(Temp)
                RecData.append(Pres)
                RecData.append(int(time.time()))

                file_handle = open('A1.txt', mode='w')
                file_handle.write(str(RecData))
                # print(RecData)
                file_handle.close
                # print(StyleTime)
                # print(TimeRec)
                # print(TempRec)
                # print(PresRec)
                fig = plt.figure()
                cb_dark_blue = (0 / 255, 107 / 255, 164 / 255)  # 设置rgb颜色值
                cb_orange = (255 / 255, 128 / 255, 14 / 255)
                ax1 = fig.add_subplot(2, 1, 1)  # 画2行1列个图形的第1个
                ax2 = fig.add_subplot(2, 1, 2)  # 画2行1列个图形的第2个

                ax1.plot(TimeRec,TempRec)
                ax2.plot(TimeRec,PresRec)
                TimeTick=np.linspace(TimeRec[0], TimeRec[-1], 6)
                print(TimeRec[0])
                print(TimeTick[0])
                TimeTickLabel = []
                n = 0
                for n in range(0,5,1):

                    # print(TimeTick[n])
                    # print(n)
                    # print(time.localtime(TimeTick[n]))
                    ADA=time.asctime(time.localtime(TimeTick[n]))
                    ADA=ADA[10:19]
                    TimeTickLabel.append(ADA)
                    n = n + 1
                # print(TimeTickLabel)
                # TimeTickLabel=time.strftime("%H:%M:%S", tuple(TimeTick))
                ax1.set_xticks(TimeTick)
                ax1.set_xticklabels(TimeTickLabel)
                ax2.set_xticks(TimeTick)
                ax2.set_xticklabels(TimeTickLabel)
                plt.xlabel("Time")
                plt.ylabel("Pres(mbar)")
                plt.legend('upper right')
                plt.show()

                # serial.write(data) #数据写回
                sleep(0.1)
    except KeyboardInterrupt:
        print('计时完成')