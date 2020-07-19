# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 17:31:07 2019

@author: sdevl
"""

"""Copy of Copy of Copy of load_steinmetz_decisions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14aT_xJZEnTYndO0B9MXxsoFEGzHFHYg8

## Loading of Steinmetz data

includes some visualizations
"""

#@title Data retrieval
import os, requests

fname = ['steinmetz_NMA_part1.npz']
fname.append('steinmetz_NMA_part2.npz')
url = ["https://osf.io/ex9zk/download"]
url.append("https://osf.io/cvjrf/download")

for j in range(2):
  if not os.path.isfile(fname[j]):
    try:
      r = requests.get(url[j])
    except requests.ConnectionError:
      print("!!! Failed to download data !!!")
    else:
      if r.status_code != requests.codes.ok:
        print("!!! Failed to download data !!!")
      else:
        with open(fname[j], "wb") as fid:
          fid.write(r.content)

#@title Data loading
import numpy as np

alldat = np.load('steinmetz_NMA_part1.npz', allow_pickle=True)['dat']
alldat = np.hstack((alldat, np.load('steinmetz_NMA_part2.npz', allow_pickle=True)['dat']))

# select just one of the recordings here. 11 is nice because it has some neurons in vis ctx.
dat = alldat[38]
print(dat)

"""`alldat` contains 39 sessions from 10 mice, data from Steinmetz et al, 2019. Time bins for all measurements are 10ms, starting 500ms before stimulus onset. The mouse had to determine which side has the highest contrast. For each `dat = alldat[k]`, you have the following fields:

* `dat['mouse_name']`: mouse name
* `dat['date_exp']`: when a session was performed
* `dat['spks']`: neurons by trials by time bins.    
* `dat['brain_area']`: brain area for each neuron recorded. 
* `dat['contrast_right']`: contrast level for the right stimulus, which is always contralateral to the recorded brain areas.
* `dat['contrast_left']`: contrast level for left stimulus. 
* `dat['gocue']`: when the go cue sound was played. 
* `dat['response_times']`: when the response was registered, which has to be after the go cue. The mouse can turn the wheel before the go cue (and always does!). 
* `dat['response']`: which side the response was (-1, 0, 1). Choices for the right stimulus are -1.  
* `dat['feedback_time']`: when feedback was provided. 
* `dat['feedback_type']`: if the feedback was positive (+1, reward) or negative (-1, white noise burst).  
* `dat['wheel']`: exact position of the wheel that the mice uses to make a response, binned at 10ms. 
* `dat['pupil']`: pupil area  (noisy, because pupil is very small) + pupil horizontal and vertical position. 
* `dat['lfp']`: recording of the local field potential in each brain area from this experiment, binned at 10ms.
* `dat['brain_area_lfp']`: brain area names for the LFP channels. 
* `dat['trough_to_peak']`: measures the width of the action potential waveform for each neuron. Widths <=10 samples are "putative fast spiking neurons". 
* `dat['waveform_w']`: temporal components of spike waveforms. w@u reconstructs the time by channels action potential shape. 
* `dat['waveform_u]`: spatial components of spike waveforms.
"""


#df = pd.read_csv('Freq_matrix.csv') # Do it manually after going to the folder path
X = df.iloc[:,1:32].values
y = df.iloc[:,0].values
pca = PCA(n_components=2)
Y = pca.fit_transform(X)
principal_components = pca.components_
explained_variance = pca.explained_variance_

with plt.style.context('seaborn-whitegrid'):
    plt.figure(figsize=(6, 4))
    for lab, col in zip(('White_V1', 'Black_V1', 'White_V2', 'Black_V2'),
                        ('blue', 'red', 'green', 'yellow')):
        plt.scatter(Y[y==lab, 0],
                    Y[y==lab, 1],
                    label=lab,
                    c=col)
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.legend()
    plt.tight_layout()
    plt.show()