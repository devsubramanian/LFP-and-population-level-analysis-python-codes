# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 11:20:00 2019

@author: sdevl
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 14:11:58 2019

@author: sdevl
"""

import hdf5storage as hdf5
data1 = hdf5.loadmat(r'C:\Users\sdevl\Desktop\Recording\Sivaji Anna\HPC_wbwb_mtx_R1784_2013_10_23.mat')
import numpy as np
import os
#  col 0 is time
#  col 1 is rat x position
#   col 2 is rat y position
#  col 3 is cluster ids of spike events
#   col 4 is event flag
#   col 5 is visit number
# col 6 is ripple detected or not

np.savez('Matrix_cscdata.npz', lfp_data = data1['m'][0,:])
print("Load arrays from the 'Matrix_cscdata.npz' file:")
with np.load('Matrix_cscdata.npz') as data:
    print(data['lfp_data'])
    #print(x2)
    #print(y2)