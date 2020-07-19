# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 17:23:16 2019

@author: sdevl
"""

# This problem is a continuation of Problem 1. Instead of computing the spectrum, we will now compute the
# spectrogram of the signal.

import numpy as np
import scipy.signal as signal
import scipy.fftpack as fftpack
import matplotlib.pyplot as plt

# ===========================================================================================================
path = 'Matrix_cscdata.npz'
# ===========================================================================================================

loaded_data = np.load(path)
lfp_data = loaded_data['lfp_data'][0:4591650]
fs = 1000 # This is the sampling rate


# Compute the spectrogram. You may use
# signal.spectrogram(   x = data,
#                       fs = sampling rate,
#                       nperseg = number of samples per window. I recommend 300,
#                       axis = axis along which spectrogram is computed
#                   )
f, t, Sxx1 = signal.spectrogram(x = lfp_data, fs = 1000, nperseg = 300, axis = 0)
# after the spectrogram is computed, compute its mean across trials and electrodes
#Sxx  =  np.mean(Sxx1, axis= (0,2))
# store the spectrogram in Sxx (shape = [151, 15] after averaging)
# store the frequencies in f (shape = [151])
# store the times in t (shape = [15])

# ===========================================================================================================

# ===========================================================================================================

# It is often useful to plot spectrograms in power per octave, which amounts to multiplying the power by the
# frequency. This brings out power at higher frequencies and makes the plots easier to understand
#Sxx1 = Sxx1*np.expand_dims(np.square(f), axis=0)

# Plot the spectrogram
plt.pcolormesh(t, f, Sxx1)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.ylim([0, 250])
plt.show()
