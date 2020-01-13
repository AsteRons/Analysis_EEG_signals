import mne
from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa

import os

path = 'A:/Repozytorium/Analysis_EEG_signals/standard_16.elc'
annots = loadmat('data/Subject_1/sessions_5Hz.mat')
oct_y = annots['Y']
oct_x = annots['Xa']

ch_names=('O2', 'AF3', 'AF4', 'P4', 'P3', 'F4', 'Fz', 'F3', 'FCz', 'Pz', 'C4', 'C3', 'CPz', 'Cz', 'Oz', 'O1')

ten_twenty_montage = mne.channels.make_standard_montage('standard_1020')
print(ten_twenty_montage)



#montage = mne.channels.read_custom_montage(path)
info = mne.create_info(ch_names, 256, 'eeg')
raw = mne.io.RawArray(oct_x, info)
raw_1020 = raw.copy().set_montage(ten_twenty_montage)

#raw.save('subj1data_raw.fif')
scalings = {'mag': 1, 'grad': 1}
raw_1020.plot(n_channels=16, scalings=scalings, title='Data from arrays',
       show=True, block=True)



raw.pick_types(meg=False, eeg=True, eog=False)
#print(mne.viz.plot_sensors)

raw_1020.plot_sensors()
raw.plot(duration=5, n_channels=16)

raw_1020.plot_psd(fmax=5)

