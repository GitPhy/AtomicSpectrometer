# Normal dispersion of air and glass
# 2019年5月6日
import numpy as np
import matplotlib.pyplot as plt


# Wavelength in nm
LambdaVacShow = np.linspace(.20, 3000000, 1000000)
LambdaVac = LambdaVacShow*1E-9
Frequency = 299792458./LambdaVac
# FrequencyShow in THz
FrequencyShow = Frequency*1E-12


LambdaVacum = LambdaVac*1E6
# Fused Silica 熔石英是玻璃材料 不是晶体，没有双折射现象
B1 = 6.96166300*1E-1
B2 = 4.07942600*1E-1
B3 = 8.97479400*1E-1
C1 = 4.67912846*1E-3
C2 = 1.35120631*1E-2
C3 = 9.79340025*1E+1

# 人为加入了一个弛豫项
ComRefractiveIndex2 = 1 + B1 * LambdaVacum ** 2. / (LambdaVacum ** 2 - C1 - 1E-3j) + \
                      B2 * LambdaVacum ** 2. / (LambdaVacum**2-C2 - 2E-3j) + \
                      B3 * LambdaVacum ** 2. / (LambdaVacum**2-C3 - 10E-0j)
ComRefractiveIndex = np.sqrt(ComRefractiveIndex2)

RealRefractiveIndex = np.real(ComRefractiveIndex)
ImagRefractiveIndex = np.imag(ComRefractiveIndex)

# 线性坐标
# plt.plot(LambdaVacShow, RealRefractiveIndex)
# plt.plot(LambdaVacShow, ImagRefractiveIndex)

# x对数坐标
plt.semilogx(LambdaVacShow, RealRefractiveIndex)
plt.semilogx(LambdaVacShow, ImagRefractiveIndex)

# 双对数坐标
# plt.loglog(LambdaVacShow, RealRefractiveIndex)
# plt.loglog(LambdaVacShow, ImagRefractiveIndex)

plt.xlabel('Wavelength (nm)', fontsize=14, color='k')
plt.ylabel('Complex Refractive Index', fontsize=14, color='k')
# plt.ylabel(r'w (pm$^{-1}$)', fontsize=20)

# plt.xlim(20, 30000)
plt.ylim(0, 3)

plt.legend(['n', 'k'], loc='best')
# plt.legend(['n', 'k'], loc='center')

plt.show()
