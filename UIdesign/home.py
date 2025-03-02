# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'home.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_home(object):
    def setupUi(self, Form_home):
        Form_home.setObjectName("Form_home")
        Form_home.resize(1049, 640)
        self.gridLayout = QtWidgets.QGridLayout(Form_home)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form_home)
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(Form_home)
        QtCore.QMetaObject.connectSlotsByName(Form_home)

    def retranslateUi(self, Form_home):
        _translate = QtCore.QCoreApplication.translate
        Form_home.setWindowTitle(_translate("Form_home", "Form"))
