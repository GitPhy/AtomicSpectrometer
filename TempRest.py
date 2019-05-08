import numpy as np
import matplotlib.pyplot as plt

Temp = np.linspace(-50, 300, 1001)
# Temp = np.linspace(199, 201, 1001)
NamePT = 'PT100'
NamePT = 'PT1000'
# RT = np.linspace(100, 200, 1001)

# print(RT)
if NamePT == 'PT1000':
    # PT1000
    RT = 1000 + (2120.2-1000)/(300-0)*Temp #PT1000
    DRT2DT=(2120.2-1000)/(300-0)
    R122 = 10E3
    R132 = 10E3
    c = R132/R122
    URef = 2.5*(1+150E-6)   #3ppm精度
    R131 = 0
    R139 = 5490
    R121 = 1540
    R139 = 5620
    R121 = 1500


if NamePT == 'PT100':
    # PT100
    RT = 100 + (212 - 100) / (300 - 0) * Temp  # PT100
    DRT2DT = (212 - 100) / (300 - 0)
    R122 = 10E3
    R132 = 10E3
    c = R132 / R122
    URef = 2.5
    R131 = 0
    R139 = 549
    R121 = 154
    # URef = 3.3
    # R131 = 0
    # R139 = 600
    # R121 = 150


    # R122 = 10E3
    # R132 = 15E3
    # c = R132/R122
    # URef = 2.5
    # R131 = 20
    # R139 = 200
    # R121 = 200

LST = 0.152E-3  # V
UBT = URef*(c-R139/R121)/(c+1)+c/(c+1)*URef*R139/(R131+RT)  # V

DiffUBT2DT = -DRT2DT*c/(c+1)*URef*R139/((R131+RT)**2)  # V/K
DiffUBT2DTmV = np.abs(DiffUBT2DT)*1E3  # mV/K

TempRes = LST/DiffUBT2DT
TempRes_mK = np.abs(TempRes)*1E3

plt.subplot(1, 3, 1)
plt.plot(Temp, UBT)
plt.grid(1)
plt.xlim(-50, 300)
# plt.ylim(0, 5)
plt.ylim(0.575, 0.595)
plt.xlim(199, 201)
plt.xlabel('Temperature (C)')
plt.ylabel('U(V)')
plt.title(['R121=',R121])

plt.subplot(1, 3, 2)
plt.plot(Temp, DiffUBT2DTmV)
# plt.xlim(-50, 300)
plt.ylim(0, 40)
plt.xlabel('Temperature (C)')
plt.ylabel('Diff(mV/K)')
plt.grid(1)
# plt.title('PT 1000')
plt.title(['URef=',URef,'V',NamePT])

plt.subplot(1, 3, 3)
plt.plot(Temp, TempRes_mK)
# plt.xlim(-50, 300)
plt.ylim(0, 30)
plt.xlabel('Temperature (C)')
plt.ylabel('Temp Res(mK)')
plt.grid(1)
plt.title(['R139=',R139])
plt.show()
print(R121)

print(DRT2DT)
