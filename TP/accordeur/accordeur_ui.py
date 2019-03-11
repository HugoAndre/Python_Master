# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Accordeur.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Accordeur(object):
    def setupUi(self, Accordeur):
        Accordeur.setObjectName("Accordeur")
        Accordeur.resize(294, 398)
        self.centralwidget = QtWidgets.QWidget(Accordeur)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Courbe = MplWidget(self.centralwidget)
        self.Courbe.setObjectName("Courbe")
        self.verticalLayout.addWidget(self.Courbe)
        self.Note = QtWidgets.QLabel(self.centralwidget)
        self.Note.setMaximumSize(QtCore.QSize(16777215, 20))
        self.Note.setAlignment(QtCore.Qt.AlignCenter)
        self.Note.setObjectName("Note")
        self.verticalLayout.addWidget(self.Note)
        self.Ajustement = QtWidgets.QProgressBar(self.centralwidget)
        self.Ajustement.setMinimum(-50)
        self.Ajustement.setMaximum(50)
        self.Ajustement.setProperty("value", 0)
        self.Ajustement.setObjectName("Ajustement")
        self.verticalLayout.addWidget(self.Ajustement)
        self.Demarrer = QtWidgets.QPushButton(self.centralwidget)
        self.Demarrer.setObjectName("Demarrer")
        self.verticalLayout.addWidget(self.Demarrer)
        self.Quitter = QtWidgets.QPushButton(self.centralwidget)
        self.Quitter.setObjectName("Quitter")
        self.verticalLayout.addWidget(self.Quitter)
        Accordeur.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Accordeur)
        self.statusbar.setObjectName("statusbar")
        Accordeur.setStatusBar(self.statusbar)

        self.retranslateUi(Accordeur)
        QtCore.QMetaObject.connectSlotsByName(Accordeur)

    def retranslateUi(self, Accordeur):
        _translate = QtCore.QCoreApplication.translate
        Accordeur.setWindowTitle(_translate("Accordeur", "Accordeur"))
        self.Note.setText(_translate("Accordeur", "Pause : Pas de note"))
        self.Demarrer.setText(_translate("Accordeur", "Démarrer"))
        self.Quitter.setText(_translate("Accordeur", "Quitter"))

from mplwidget import MplWidget
