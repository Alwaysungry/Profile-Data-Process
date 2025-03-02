# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SProFig.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_SProFig(object):
    def setupUi(self, Form_SProFig):
        Form_SProFig.setObjectName("Form_SProFig")
        Form_SProFig.resize(1047, 640)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form_SProFig)
        self.verticalLayout.setContentsMargins(0, 6, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form_SProFig)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 2, 0, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_SPro = QtWidgets.QPushButton(self.widget)
        self.pushButton_SPro.setObjectName("pushButton_SPro")
        self.horizontalLayout.addWidget(self.pushButton_SPro)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_clear = QtWidgets.QPushButton(self.widget)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout.addWidget(self.pushButton_clear)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.widget)
        self.widget_SPro = QtWidgets.QWidget(Form_SProFig)
        self.widget_SPro.setObjectName("widget_SPro")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_SPro)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_SPro = QtWidgets.QGridLayout()
        self.gridLayout_SPro.setObjectName("gridLayout_SPro")
        self.gridLayout_2.addLayout(self.gridLayout_SPro, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget_SPro)
        self.verticalLayout.setStretch(1, 20)

        self.retranslateUi(Form_SProFig)
        QtCore.QMetaObject.connectSlotsByName(Form_SProFig)

    def retranslateUi(self, Form_SProFig):
        _translate = QtCore.QCoreApplication.translate
        Form_SProFig.setWindowTitle(_translate("Form_SProFig", "Form"))
        self.pushButton_SPro.setText(_translate("Form_SProFig", "画图"))
        self.pushButton_clear.setText(_translate("Form_SProFig", "清除画图"))
