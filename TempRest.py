import numpy as np
import matplotlib.pyplot as plt

Temp = np.linspace(0, 270, 1001)
RT = 100 + (212-100)/(300-0)*Temp #PT100
RT = 1000 + (2120.2-1000)/(300-0)*Temp #PT1000
# RT = np.linspace(100, 200, 1001)
print(RT)

R122 = 10E3
R132 = 10E3
c = R132/R122
URef = 3.3
R131 = 0
R139 = 500
R121 = 100

# PT100
R122 = 10E3
R132 = 10E3
c = R132/R122
URef = 3.3
R131 = 0
R139 = 600
R121 = 150

# PT1000
R122 = 15E3
R132 = 15E3
c = R132/R122
URef = 3.3
R131 = 0
R139 = 6000
R121 = 1500


LST = 0.152E-3

UBT = URef*(c-R139/R121)/(c+1)+c/(c+1)*URef*R139/(R131+RT)

DiffUBT = -c/(c+1)*URef*R139/(R131+RT)**2
DiffTemp = LST/DiffUBT
DiffTempmK = np.abs(DiffTemp)*1E3
DiffUBTmV = np.abs(DiffUBT)*1E3

plt.subplot(1, 3, 1)
plt.plot(Temp, UBT)
plt.grid(1)
plt.xlim(0, 270)
# plt.ylim(0, 5)
plt.xlabel('Temperature (C)')
plt.ylabel('U(V)')

plt.subplot(1, 3, 2)
plt.plot(Temp, DiffUBTmV)
plt.xlim(0, 270)
# plt.ylim(0, 100)
plt.xlabel('Temperature (C)')
plt.ylabel('Diff(mV/K)')
plt.grid(1)
plt.title('PT 1000')
# plt.title('PT 100')

plt.subplot(1, 3, 3)
plt.plot(Temp, DiffTempmK)
plt.xlim(0, 270)
# plt.ylim(0, 10)
plt.xlabel('Temperature (C)')
plt.ylabel('Diff(mK)')
plt.grid(1)
plt.show()

