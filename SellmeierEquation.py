# Normal dispersion of air and glass
# 2019年5月6日
import numpy as np
import matplotlib.pyplot as plt

# Wavelength in nm
LambdaVacShow = np.linspace(400,700,100001)
LambdaVac = LambdaVacShow*1E-9
Frequency = 299792458./LambdaVac
# FrequencyShow in THz
FrequencyShow = Frequency*1E-12;
# plt.plot(LambdaVacShow,FrequencyShow)
# plt.show()

LambdaVacum = LambdaVac*1E6
# Fused Silicon
B1 = 6.96166300*1E-1
B2 = 4.07942600*1E-1
B3 = 8.97479400*1E-1
C1 = 4.67912846*1E-3
C2 = 1.35120631*1E-2
C3 = 9.79340025*1E+1
RrefractiveIndex = np.sqrt(1+B1*LambdaVacum**2./(LambdaVacum**2-C1)+B2*LambdaVacum**2./(LambdaVacum**2-C2)+B3*LambdaVacum**2./(LambdaVacum**2-C3))
RrefractiveIndexDiff = np.diff(RrefractiveIndex)
# RrefractiveIndexDiff[]
plt.plot(LambdaVacShow,RrefractiveIndex)
# plt.plot(LambdaVacShow,RrefractiveIndexDiff)
plt.show()



