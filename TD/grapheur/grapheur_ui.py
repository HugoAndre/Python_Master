# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grapheur.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Grapheur(object):
    def setupUi(self, Grapheur):
        Grapheur.setObjectName("Grapheur")
        Grapheur.resize(748, 279)
        self.centralwidget = QtWidgets.QWidget(Grapheur)
        self.centralwidget.setObjectName("centralwidget")
        self.lblFreq = QtWidgets.QLabel(self.centralwidget)
        self.lblFreq.setGeometry(QtCore.QRect(20, 20, 71, 16))
        self.lblFreq.setObjectName("lblFreq")
        self.txtFreq = QtWidgets.QLineEdit(self.centralwidget)
        self.txtFreq.setGeometry(QtCore.QRect(130, 20, 113, 21))
        self.txtFreq.setObjectName("txtFreq")
        self.lblBruit = QtWidgets.QLabel(self.centralwidget)
        self.lblBruit.setGeometry(QtCore.QRect(20, 60, 111, 16))
        self.lblBruit.setObjectName("lblBruit")
        self.txtBruit = QtWidgets.QLineEdit(self.centralwidget)
        self.txtBruit.setGeometry(QtCore.QRect(130, 60, 113, 21))
        self.txtBruit.setObjectName("txtBruit")
        self.btValider = QtWidgets.QPushButton(self.centralwidget)
        self.btValider.setGeometry(QtCore.QRect(10, 100, 113, 32))
        self.btValider.setObjectName("btValider")
        self.wdGraph = MplWidget(self.centralwidget)
        self.wdGraph.setGeometry(QtCore.QRect(260, 20, 461, 191))
        self.wdGraph.setObjectName("wdGraph")
        self.btQuitter = QtWidgets.QPushButton(self.centralwidget)
        self.btQuitter.setGeometry(QtCore.QRect(130, 100, 113, 32))
        self.btQuitter.setObjectName("btQuitter")
        Grapheur.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Grapheur)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 748, 22))
        self.menubar.setObjectName("menubar")
        Grapheur.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Grapheur)
        self.statusbar.setObjectName("statusbar")
        Grapheur.setStatusBar(self.statusbar)

        self.retranslateUi(Grapheur)
        self.btQuitter.clicked.connect(Grapheur.close)
        QtCore.QMetaObject.connectSlotsByName(Grapheur)

    def retranslateUi(self, Grapheur):
        _translate = QtCore.QCoreApplication.translate
        Grapheur.setWindowTitle(_translate("Grapheur", "Grapheur"))
        self.lblFreq.setText(_translate("Grapheur", "Fréquence :"))
        self.txtFreq.setText(_translate("Grapheur", "1000"))
        self.lblBruit.setText(_translate("Grapheur", "Amplitude bruit :"))
        self.txtBruit.setText(_translate("Grapheur", "0.1"))
        self.btValider.setText(_translate("Grapheur", "Valider"))
        self.btQuitter.setText(_translate("Grapheur", "Quitter"))

from mplwidget import MplWidget
