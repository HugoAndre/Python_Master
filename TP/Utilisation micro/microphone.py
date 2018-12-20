# -*- coding: utf-8 -*-
"""
Created on Sat Oct 20 10:24:45 2018

@author: frederic
"""

# Installation du package sounddevice :
#   Pour Windows
#      lancer Anaconda Prompt
#      taper conda install -c conda-forge python-sounddevice
#      accepter l'installation
#   Pour mac
#      utiliser pip install sounddevice
#      conda n'installe pas tout

import matplotlib.pyplot as plt
import numpy as np
import scipy as sp
import scipy.signal as sig
import sounddevice as sd

# Constantes
fech=44100
N=fech*1

## Enregistre le son du microphone et l'affiche
#microphone=sd.rec(frames=N,samplerate=fech,channels=1,blocking=True)
#t=np.arange(0,N/fech,1/fech)
#
#plt.figure("Microphone")
#plt.plot(t,microphone)
#plt.xlabel("Temps [s]")
#plt.show()


# Affichage continu du son du microphone sur un graphe (callback)
def traitEchantillons(indata, frames, time, status):
    #if status:
    #    print(status)
    #
    #print("%i échantillons" % (frames))
    
    # Calcul transformée de Fourier
    f,Pxx=sig.welch(indata[:,0],fs=fech,nperseg=fech//10)
    PxxdB=10*np.log10(Pxx)
    
    # Crée axe temps et fréquence
    t=np.arange(0,frames/fech,1/fech)
    #f=np.arange(0,fech,fech/N)
    
    # Met à jour les données associées sur la courbe
    ligne_temps.set_data(t,indata)
    ligne_freq.set_data(f,PxxdB)
    ax2.set_ylim(min(PxxdB),max(PxxdB))

    # Demande de redessiner le graphe
    fig.canvas.draw()

# Prépare le graphe
fig=plt.figure()
ax1=plt.subplot(2,1,1)
lignes=plt.plot([2,3,4])
ligne_temps=lignes[0]
plt.ylim(-1,1)
plt.xlim(0,1)
plt.xlabel("Temps [s]")
plt.title("Signal temporel")
ax2=plt.subplot(2,1,2)
lignes=plt.plot([2,3,4])
plt.xlim(0,fech/2)
ligne_freq=lignes[0]
plt.xlabel("Fréquence [Hz]")
plt.title("Spectre")


# Crée le flux pour l'acquisition
flux=sd.InputStream(samplerate=fech,blocksize=N,channels=1, callback=traitEchantillons)

# Lance l'acquisition
flux.start()


# Arrêt
# flux.stop()
