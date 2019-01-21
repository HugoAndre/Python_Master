#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Essai Qt 5 + Qt Designer (outil de création de fenêtre)

La fenêtre a été crée avec Qt Designer (disponible dans repertoire anaconda/bin)
Qt Designer produit un fichier .ui (ici gui.ui)
Qu'il suffit de charger avec uic.loadUi("gui.ui",self)
Inconvénient : on ne voit pas les variables associés au éléments de la fenêtre
  dans le script

Alternative : il existe un outils qt permettant de transformer gui.ui en fichier
  Python.
  
Fichier construit en mixant plusieurs exemples sur des sites web :
    - http://zetcode.com/gui/pyqt5/firstprograms/
    - https://likegeeks.com/pyqt5-tutorial/
    - https://matplotlib.org/2.1.0/gallery/user_interfaces/embedding_in_qt5_sgskip.html
@author: Frédéric Bonnardot, Janvier 2019
"""
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5 import uic

import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.backends.backend_qt5agg as pltqt5
 
import numpy as np

mpl.use('Qt5Agg')

class Example(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    """
    Méthode pour gérer l'appui sur btPressMe (CallBack)
    """
    def btPressMeClicked(self):
        # Mise à jour du contenu de txtZone
        # PS : txtZone est crée par uic.loadUi -> pas de réf dans ce fichier
        self.txtZone.setText("Coucou")
        
    def initUI(self):
        
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))        

        # Charge l'interface utilisateur dans gui.ui
        uic.loadUi("gui.ui",self)
        
        # btPressMe définit dans gui.ui
        # On associé l'action clicked à la CallBack btPressMeClicked
        self.btPressMe.clicked.connect(self.btPressMeClicked)
    
        # Crée une figure
        fig=plt.Figure(figsize=(4,1))
        ax=fig.add_subplot(1,1,1)
        t=np.arange(0,0.1,0.001)
        ax.plot(t,np.sin(2*np.pi*t)+np.random.randn(len(t)))
        
        # Ajoute un figure canvas (non disponible dans QtDesigner)
        canvas=pltqt5.FigureCanvasQTAgg(fig)
        canvas.setParent(self)
        canvas.move(0,200)
        
        
    
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = Example()
    #app.exec()
    #sys.exit(app.exec_())

# Redémarrer le noyaux après l'éxécution sinon risque de plantage
    