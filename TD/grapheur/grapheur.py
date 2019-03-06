#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 21:58:58 2019

@author: frederic
"""

import sys # Requis pour PyQt5

from PyQt5.QtWidgets import QMainWindow,QApplication,QLabel,QLineEdit,QPushButton
from PyQt5.QtCore    import pyqtSlot

# Etape 3
import matplotlib.pyplot as plt
import numpy as np


# Importe la classe Ui_grapheur contenue dans grapheur_ui.py généré par nos soins
from grapheur_ui import Ui_Grapheur

# Crée une classe définie à partir QMainWindow et de Ui_Grapheur
class GraphWindow(QMainWindow,Ui_Grapheur):
    # Méthode appelée lorsque l'on crée l'objet
    def __init__(self,parent=None):
        # Appel la méthode __init__ de QMainWindow
        super(GraphWindow,self).__init__(parent)
        # Appelle la méthode setupUi de Ui_grapheur pour remplir la fenêtre
        self.setupUi(self)
        
    @pyqtSlot() # Définit un slot pour recevoir un signal
    def on_btValider_clicked(self): # signal clicked associé à l'élément btValider
        # Etape 1
        ##########
        # print("test") # On affiche simplement test sur la console
        # Etape 2
        #########
        #freq=self.txtFreq.text() # Range le contenu de la zone de texte txtFreq dans freq
        #message="Sin à "+freq+" Hz" # Crée un message (ici freq est un texte)
        #self.btValider.setText(message) # Ce message devient le texte associé au bouton valider
        # Etape 3
        ##########
        f1=float(self.txtFreq.text())
        a=float(self.txtBruit.text())
        t=np.arange(1000)/200000
        x=np.sin(2*np.pi*t*f1)+a*np.random.randn(len(t))
        #plt.plot(t,x)
        # Etape 4
        ##########
        self.wdGraph.canvas.ax.cla()
        self.wdGraph.canvas.ax.plot(t,x)
        self.wdGraph.canvas.draw()
        

# Appellé au lancement le l'application
if __name__ == '__main__':
    # Initialise le gestionnaire Qt si cela n'a pas encore été fait
    if 'app' not in locals():
        app = QApplication(sys.argv)
    # Crée un objet associé à la fenêtre
    graphWin = GraphWindow()
    # Affiche la fenêtre
    graphWin.show()
    rc = app.exec_() 
    sys.exit(rc)

