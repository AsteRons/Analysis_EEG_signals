from scipy.io import loadmat
import mne



#Pobieranie danych
path = 'A:/Repozytorium/Analysis_EEG_signals/standard_16.elc'
annots = loadmat('data/Subject_1/sessions_5Hz.mat')
oct_y = annots['Y']
oct_x = annots['Xa']

#Budowa zmiennej raw

ch_names=('O2', 'AF3', 'AF4', 'P4', 'P3', 'F4', 'Fz', 'F3', 'FCz', 'Pz', 'C4', 'C3', 'CPz', 'Cz', 'Oz', 'O1')
info = mne.create_info(ch_names, 256, 'eeg')
raw = mne.io.RawArray(oct_x, info)

#Ustawianie sensorów

ten_twenty_montage = mne.channels.make_standard_montage('standard_1020')
raw_1020 = raw.copy().set_montage(ten_twenty_montage)
raw_1020.plot_sensors()

#Wyświetlenie pobranych danych
scalings = {'mag': 1, 'grad': 1}
raw_1020.plot(n_channels=16, scalings=scalings, title='Data from arrays',
       show=True, block=True)

#Tworzenie zdarzenia migania iodą i wyświetlanie tych danych
event = mne.make_fixed_length_events(raw_1020, start=0, stop=30, duration=0.2)
raw.plot(events=event, start=0, duration=5, color='gray', event_color='r')

#Analiza PSD
raw_1020.plot_psd(fmax=200)


#Analiza ICE
ica = mne.preprocessing.ICA(n_components=16, random_state=97, max_iter=800)
ica.fit(raw_1020)
ica.exclude = [1, 2]  # details on how we picked these are omitted here
ica.plot_properties(raw_1020, picks=ica.exclude)

ica.plot_components()
ica.plot_overlay(raw_1020, exclude=[0], picks='eeg')

