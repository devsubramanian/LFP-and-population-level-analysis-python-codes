# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 14:01:48 2019

@author: sdevl
"""

# All of the data for the problems in this problem set come from
#
#  Warden & Miller, "The representation of multiple objects in prefrontal neuronal delay activity,"
#  Cereb. Cortex (2007)
#
#  We will be reproducing the analysis of
#
#  Siegel, Warden, and Miller, "Phase-dependent neuronal coding of objects in short-term memory", PNAS 2009
#
#  showing beta band oscillations in the LFP of electrode recordings as monkeys remembered items in
#  a sequence. The data we are analyzing is a different recording than the one shown in the paper.
#
#  The loaded data is stored as lfp_data which is a [8, 4000, 837] tensor.
#  8        Electrodes
#  4000     Samples recorded at 1000 Hz (4 second recording)
#  837      Trials
#
#  Each trial, the monkey was shown two images. The first image was shown from t = 1 to t = 1.5
#  The second image was shown from t = 2.5 to t = 3
#
#  In this problem we will compute the spectrum of the data and use a notch filter to remove the 60 Hz noise

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


# Part A
# Compute the power spectrum using fftpack.fft(x, axis=?) and np.square(np.abs()).
# Then average the power spectrum over the trials and electrodes and store the
# result as lfp_data_ft.
#
# Also compute a list of omegas, which should range from 0 to 1 and be the same length as lft_data_ft
# ===========================================================================================================
lfp = fftpack.fft(lfp_data, axis=0)
lfp_power = np.square(np.abs(lfp))
#lfp_data_ft  =  np.mean(lfp_power, axis= (0,2))
omegas = np.linspace(0, 1 , num=len(lfp_data))
# ===========================================================================================================

plt.plot(omegas*1000.0, lfp_power)
plt.xlim([0, 100])
plt.show()

# Note the enormous 60 Hz peak. Let's filter it out
#
# For this we use a notch filter b, a = signal.iirnotch(frequency, Q=quality, fs=sampling_rate). I recommend
# Q = 10
#
# Filter the data with b, a and signal.filtfilt() along the appropriate axis and store the result in
# lfp_data_notch_filtered

# Part B
# ===========================================================================================================
#b, a = signal.iirnotch(60, Q= 10, fs=fs)
#lfp_data_notch_filtered = signal.filtfilt(b,a,lfp_data, axis = 1)
## ===========================================================================================================
#
## Finally, replot the power spectrum for lfp_data_notch_filtered. The is exactly the same as part A, but for
## notch filtered data
#
## ===========================================================================================================
#lfp_notch = fftpack.fft(lfp_data_notch_filtered, axis=1)
#lfp_power_notch = np.square(np.abs(lfp_notch)) 
#lfp_data_ft_notch_filtered = np.mean(lfp_power_notch, axis= (0,2))
#omegas = np.linspace(0, 1 , num=len(lfp_data_ft_notch_filtered))
## ===========================================================================================================
#
#plt.plot(omegas*1000.0, lfp_data_ft_notch_filtered)
#plt.xlim([0, 100])
#plt.show()
#
## Note the peak at ~ 25 Hz. This  beta-frequency power is what we will be analyzing in the next parts.