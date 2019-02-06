#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Essai Qt 5 + Qt Designer (outil de création de fenêtre)
             AVEC GRAPHIQUE PYPLOT PLACE DANS QT DESIGNER

Fenêtre crée avec Qt Designer (disponible dans repertoire anaconda/bin)
>>> Pour placer le graphique non disponible dans les widgets :
      - Placer un container de type Widget où l'on veut le PYPLOT
      - Cliquer à droite sur le Widget et choisir Promouvoir en... dans le menu contextuel
      - Remplir nom de la classe promue : MplWidget, Fichier d'en tête : mplwidget (sans .h)
      - Cliquer sur Ajouter puis sur Promouvoir
      - Placer le ficher mplwidget.py dans le même répertoire que ce fichier (qtdesign2.py)

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

Pour l'astuce pour PYPLOT (promouvoir, mplwidget.py) :
    https://stackoverflow.com/questions/43947318/plotting-matplotlib-figure-inside-qwidget-using-qt-designer-form-and-pyqt5

@author: Frédéric Bonnardot, Février 2019
"""

import sys # Requis pour PyQt5

# Charge les packages associés à PyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5 import uic


import matplotlib as mpl
#import matplotlib.pyplot as plt
#import matplotlib.backends.backend_qt5agg as pltqt5


import numpy as np

mpl.use('Qt5Agg')

class Example2(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
    
    """
    Méthode pour gérer l'appui sur graphBt (CallBack)
    """
    def graphBtClicked(self):
        # Dessine dans la figure
        t=np.arange(0,0.1,0.001)
        self.graph.canvas.ax.plot(t,np.sin(2*np.pi*t)+np.random.randn(len(t)))
        self.graph.canvas.draw() # Demande de mettre à jour l'affichage

        
    """
    Méthode pour décrire le contenu la fenêtre
    """
    def initUI(self):
        
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))        

        # Charge l'interface utilisateur dans gui.ui
        uic.loadUi("gui2.ui",self)
        
        # graphBt définit dans gui.ui
        # On associé l'action clicked à la CallBack graphBtClicked
        self.graphBt.clicked.connect(self.graphBtClicked)
            
        self.show()
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example2()
    app.exec()
    sys.exit(app.exec_())

# Redémarrer le noyaux après l'éxécution sinon risque de plantage
    