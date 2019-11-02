import mne
from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa

import os


annots = loadmat('data/Subject_1/sessions_5Hz.mat')
oct_y = annots['Y']
oct_x = annots['Xa']

ch_names=('O2', 'AF3', 'AF4', 'P4', 'P3', 'F4', 'Fz', 'F3', 'FCz', 'Pz', 'C4', 'C3', 'CPz', 'Cz', 'Oz', 'O1')
info = mne.create_info(ch_names, 256, 'eeg')

raw = mne.io.RawArray(oct_x, info)
#raw.save('subj1data_raw.fif')

#scalings = {'mag': 1, 'grad': 1}
#raw.plot(n_channels=16, scalings=scalings, title='Data from arrays',
#       show=True, block=True)


raw.pick_types(meg=False, eeg=True, eog=False)
print(mne.viz.plot_sensors)

#biosemi_layout = mne.channels.read_layout('biosemi')
#biosemi_layout.plot()  # same result as: mne.viz.plot_layout(biosemi_layout)

raw.plot_sensors()


