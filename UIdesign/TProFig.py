# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TProFig.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_TProFig(object):
    def setupUi(self, Form_TProFig):
        Form_TProFig.setObjectName("Form_TProFig")
        Form_TProFig.resize(1047, 640)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form_TProFig)
        self.verticalLayout.setContentsMargins(0, 6, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_2 = QtWidgets.QWidget(Form_TProFig)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout.setContentsMargins(0, 2, 0, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_TPro = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_TPro.setObjectName("pushButton_TPro")
        self.horizontalLayout.addWidget(self.pushButton_TPro)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_clear = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout.addWidget(self.pushButton_clear)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_TPro = QtWidgets.QWidget(Form_TProFig)
        self.widget_TPro.setObjectName("widget_TPro")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_TPro)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_TPro = QtWidgets.QGridLayout()
        self.gridLayout_TPro.setObjectName("gridLayout_TPro")
        self.gridLayout_2.addLayout(self.gridLayout_TPro, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget_TPro)
        self.verticalLayout.setStretch(1, 20)

        self.retranslateUi(Form_TProFig)
        QtCore.QMetaObject.connectSlotsByName(Form_TProFig)

    def retranslateUi(self, Form_TProFig):
        _translate = QtCore.QCoreApplication.translate
        Form_TProFig.setWindowTitle(_translate("Form_TProFig", "Form"))
        self.pushButton_TPro.setText(_translate("Form_TProFig", "画图"))
        self.pushButton_clear.setText(_translate("Form_TProFig", "清除画图"))
