#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 12:01:17 2019

@author: frederic
"""

import sys # Requis pour PyQt5
from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QProgressBar,QPushButton
from PyQt5.QtCore    import pyqtSlot

import sounddevice as sd # Gestion du microphone

import numpy as np

# Importe la classe Ui_Accordeur contenue dans accordeur_ui.py
from accordeur_ui import Ui_Accordeur
# Crée une classe définie à partir QMainWindow et de Ui_Grapheur
class GraphWindow(QMainWindow,Ui_Accordeur):
    fs = 11025
    Trec= 1
    recording=False
    
    nomNotes=('Do','Do#','Ré','Ré#','Mi','Fa','Fa#','Sol','Sol#','La','La#','Si')
    
    # Méthode appelée lorsque l’on crée l’objet
    def __init__(self,parent=None):
        # Appel la méthode __init__ de QMainWindow
        super(GraphWindow,self).__init__(parent)
        # Appelle la méthode setupUi de Ui_grapheur pour remplir la fenêtre
        self.setupUi(self)
        
    # Méthode appelée lorsque l'on clique sur Enregistrer
    @pyqtSlot()
    def on_Demarrer_clicked(self):
        # Selon que l'on est en train d'enregistrer ou pas
        if self.recording:
            # Arrêt de l'enregistrement - efface le graphe
            self.flux.stop()
            self.recording=False
            self.Demarrer.setText("Démarrer")
            self.Note.setText("Pause : Pas de Note")
            self.Courbe.canvas.ax.cla()
            self.Courbe.canvas.ax.draw()
        else:
            # Lance l'enregistrement en continu
            self.flux=self.flux=sd.InputStream(samplerate=self.fs,blocksize=int(self.Trec*self.fs),channels=1, callback=self.traitEchantillons)
            self.recording=True
            self.Demarrer.setText("Pause")
            self.flux.start()
            
    # Méthode appelée lorsque l'on cliquer sur Quitter
    @pyqtSlot()
    def on_Quitter_clicked(self):
        # Arrête le flux
        if self.recording:
            self.flux.stop()
            self.recording=False
        # Masque la fenêtre
        self.close()
        
    # Appelée à chaque fois que l'on a enregistré des données sur le micro
    def traitEchantillons(self,indata, frames, time, status):
        # Traitement du signal indata
        N=np.shape(indata)[0]
        mtf=np.abs(np.fft.fft(indata[:,0]))
        # Met à zéro entre 0 et 30 Hz (présence de parasites dans cette zone)
        mtf[0:int(30/self.fs*N)]=0
        pmax=np.argmax(mtf)
        
        # Retrouve la note associée voir tableau https://fr.wikipedia.org/wiki/Note_de_musique
        if pmax>0:
            ref=440*2**(-9/12-3) # Part de la3 pour obtenir de do0 (3 octaves 9 demis ton en -)
            tonf=np.log2(pmax/N*self.fs/ref)*12    # 0 correspond au DO octave 0 (32.7 Hz)
            ton=int(np.round(tonf))
            octave=ton//12
            note=ton % 12
        
            # Affiche la note
            self.Note.setText("{:5d} Hz : {:3s}{:d}".format(int(pmax/N*self.fs),self.nomNotes[note],octave))
            self.Note.update() # Force à redessiner
            
            # Met à jour le curseur d'ajustement
            #self.Ajustement.setValue(int((tonf-ton)*100))
            #self.Ajustement.update() # Force à redessiner
        else:
            self.Note.setText("????")
        
        # Affiche la courbe
        freq=np.arange(N)/N*self.fs
        self.Courbe.canvas.ax.cla()
        self.Courbe.canvas.ax.plot(freq[0:N//2],mtf[0:N//2],'b',freq[pmax],mtf[pmax],'ro')
        #self.Courbe.canvas.ax.plot(indata[:,0])
        self.Courbe.canvas.ax.set_xlabel('Frequence [Hz]')
        self.Courbe.canvas.draw()
        
        app.processEvents()  # Prend le temps de traiter les événements
        
# Appellé au lancement le l’application
if __name__ == '__main__':
    # Initialise le gestionnaire Qt si cela n’a pas encore été fait
    if 'app' not in locals():
        app = QApplication(sys.argv)
    # Crée un objet associé à la fenêtre
    graphWin = GraphWindow()
    # Affiche la fenêtre
    graphWin.show()
    rc = app.exec_()
    sys.exit(rc)