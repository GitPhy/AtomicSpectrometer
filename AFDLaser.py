# laser frequency stablization
# 2019年5月15日

import numpy as np
import matplotlib.pyplot as plt

NumFreq = 1001;
Freq = np.linspace(-10e9,10e9,NumFreq)
R1 =  np.exp(-(Freq-3.2e9)**2/12e18)
R2 = np.exp(-(Freq+3.2e9)**2/12e18)
# R2 = 1- np.exp(-(Freq+8e9)**2/10e18)-np.exp(-(Freq-8e9)**2/10e18)

plt.subplot(1,2,1)
plt.plot(Freq,R1)
plt.plot(Freq,R2)

plt.subplot(1,2,2)
plt.plot(R1,R2)
plt.axis('tight')
plt.show()

