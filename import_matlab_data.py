# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:11:58 2019

@author: sdevl
"""

import hdf5storage as hdf5
data1 = hdf5.loadmat(r'C:\Users\sdevl\Desktop\Recording\Adam RSC Data\PCIA\RSC ABAB matrix files.mat')
#data = hdf5.loadmat(r'C:\Users\sdevl\Desktop\Recording\RSC-DREADD Controls\R2016\Sessions\ABAB\08-12-2019\08-12-2019.mat')
import numpy as np
import os
#  col 0 is time
#  col 1 is rat x position
#   col 2 is rat y position
#  col 3 is cluster ids of spike events
#   col 4 is event flag
#   col 5 is visit number
# col 6 is ripple detected or not

## np.savez('Matrix_data.npz', Time = data1['mtx_R1877_rec01_wbwb_9_13_16'][:,0], X_pos = data1['mtx_R1877_rec01_wbwb_9_13_16'][:,1], Y_pos = data1['mtx_R1877_rec01_wbwb_9_13_16'][:,2], Spikes = data1['mtx_R1877_rec01_wbwb_9_13_16'][:,3], Event = data1['mtx_R1877_rec01_wbwb_9_13_16'][:,4], Visit  = data1['mtx_R1877_rec01_wbwb_9_13_16'][:,5])
## print("Load arrays from the 'Matrix_data.npz' file:")
##with np.load('Matrix_data.npz') as data:
 ##   print(data['Spikes'])
    #print(x2)
    #print(y2)