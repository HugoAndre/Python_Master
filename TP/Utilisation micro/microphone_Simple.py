# -*- coding: utf-8 -*-
"""
Created on March 10 2018

@author: frederic, hugo
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
fech=44100 #Fréquence d'échantillonnage de la carte son du système.
N=fech*3 # Durée du signal (en nombre de points)

# Affichage continu du son du microphone sur un graphe (callback)
def traitEchantillons(indata, frames, time, status):    
    # Crée axe temps
    t=np.arange(0,frames/fech,1/fech)
    
    # Met à jour les données associées sur la courbe
    Courbe.set_data(t,indata)
    ax.set_ylim(min(indata),max(indata))

    # Demande de redessiner le graphe
    fig.canvas.draw()

# Prépare le graphe
fig=plt.figure() # créer une figure pour héberger l'axe.
Courbes=plt.plot([2,3,4]) # creer une première courbe (ce qui fait apparaitre un cadre cartésien)
ax = fig.axes[0] # référencer le cadre créé lors de la ligne précédente.
Courbe=Courbes[0] # référencer la courbe 
plt.xlim(0,N/fech) # définir les limites des absisces
plt.xlabel("Temps [s]")
plt.title("Signal temporel")


# Crée le flux pour l'acquisition
flux=sd.InputStream(samplerate=fech,blocksize=N,channels=1, callback=traitEchantillons)

# Lance l'acquisition
flux.start()
