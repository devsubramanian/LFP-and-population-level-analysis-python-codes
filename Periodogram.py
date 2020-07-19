# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 13:41:31 2019

@author: sdevl
"""

from scipy import signal
import matplotlib.pyplot as plt
f, Pxx_spec = signal.periodogram(data1['m'], fs = 1000, scaling='spectrum', axis=0)
plt.figure()
plt.semilogy(f, Pxx_spec)
plt.xlabel('frequency [Hz]')
plt.ylabel('Power spectrum')
plt.show()