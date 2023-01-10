import sounddevice as sd
import numpy as np
import pyqtgraph as pg
from pyqtgraph.Qt import QtGui, QtCore
import time

# Définissez les paramètres de l'enregistrement audio
sample_rate = 44100  # Fréquence d'échantillonnage en Hz
buffer_size = 1024  # Taille du tampon en échantillons

mic = sd.InputStream(samplerate=sample_rate, channels=1)


# Créez un tableau NumPy pour stocker les données audio
buffer = np.zeros(buffer_size, dtype=np.int16)

# Affichez le graphique pour la première fois
plt = pg.plot()
pg.QtGui.QApplication.processEvents()
win = pg.GraphicsWindow(title="Un graphique")
win.resize(1000, 800)

with mic:
    # Boucle infinie pour lire les données audio en continu et mettre à jour le graphique en temps réel
    while True:
        # Lisez les données audio du microphone
        data = mic.read(buffer_size)[0]
        # Convertir les données en un tableau NumPy
        data = np.frombuffer(data, dtype=np.int16)
        # Mettre à jour le tampon avec les nouvelles données
        buffer = np.append(buffer, data)
        # Créer un histograme de fréquence à partir du spectre
        freqs = np.fft.fftfreq(buffer.size, 1 / sample_rate)
        # Mettre à jour le graphique avec les nouvelles données
        plt.cla()
        plt.plot(freqs, np.abs(np.fft.fft(buffer)))
        plt.xlim(0, 2000)
        plt.ylim(0, 10000)
        plt.draw()
        plt.pause(0.001)

