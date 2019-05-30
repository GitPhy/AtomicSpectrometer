# laser frequency stablization
# 2019年5月15日
# Show The principle for laser frequency stabliaztion with two AFD

import numpy as np
import matplotlib.pyplot as plt

NumFreq = 81;
Freq = np.linspace(-10e9,10e9,NumFreq)
Sigma = 4e9
R1 =  np.exp(-(Freq-3.2e9)**2/Sigma**2)
R2 = np.exp(-(Freq+3.2e9)**2/Sigma**2)
# R2 = 1- np.exp(-(Freq+8e9)**2/10e18)-np.exp(-(Freq-8e9)**2/10e18)

FreqShow = Freq*1e-9

plt.subplot(1,2,1)
plt.plot(FreqShow,R1)
plt.plot(FreqShow,R2)
plt.legend(['R1','R2'])
plt.xlabel('Frequency (GHz)')
plt.ylabel('Ratio')

plt.subplot(1,2,2)
plt.plot(R1,R2,'o')
plt.xlabel('R1')
plt.ylabel('R2')

plt.show()

