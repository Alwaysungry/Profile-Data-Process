# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TDFig.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_TDFig(object):
    def setupUi(self, Form_TDFig):
        Form_TDFig.setObjectName("Form_TDFig")
        Form_TDFig.resize(1047, 640)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form_TDFig)
        self.verticalLayout.setContentsMargins(0, 6, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form_TDFig)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 2, 0, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBoxTD_start = QtWidgets.QSpinBox(self.widget)
        self.spinBoxTD_start.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBoxTD_start.setMinimum(1)
        self.spinBoxTD_start.setMaximum(999)
        self.spinBoxTD_start.setObjectName("spinBoxTD_start")
        self.horizontalLayout.addWidget(self.spinBoxTD_start)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.spinBoxTD_stop = QtWidgets.QSpinBox(self.widget)
        self.spinBoxTD_stop.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBoxTD_stop.setMinimum(1)
        self.spinBoxTD_stop.setMaximum(999)
        self.spinBoxTD_stop.setObjectName("spinBoxTD_stop")
        self.horizontalLayout.addWidget(self.spinBoxTD_stop)
        self.comboBox_TDFig = QtWidgets.QComboBox(self.widget)
        self.comboBox_TDFig.setObjectName("comboBox_TDFig")
        self.comboBox_TDFig.addItem("")
        self.comboBox_TDFig.addItem("")
        self.comboBox_TDFig.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_TDFig)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_TDFig = QtWidgets.QPushButton(self.widget)
        self.pushButton_TDFig.setObjectName("pushButton_TDFig")
        self.horizontalLayout.addWidget(self.pushButton_TDFig)
        self.pushButton_clear = QtWidgets.QPushButton(self.widget)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout.addWidget(self.pushButton_clear)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(6, 1)
        self.horizontalLayout.setStretch(9, 1)
        self.verticalLayout.addWidget(self.widget)
        self.widget_TDFig = QtWidgets.QWidget(Form_TDFig)
        self.widget_TDFig.setObjectName("widget_TDFig")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_TDFig)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setHorizontalSpacing(6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_TDFig = QtWidgets.QGridLayout()
        self.gridLayout_TDFig.setHorizontalSpacing(6)
        self.gridLayout_TDFig.setObjectName("gridLayout_TDFig")
        self.gridLayout_2.addLayout(self.gridLayout_TDFig, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget_TDFig)
        self.verticalLayout.setStretch(1, 20)

        self.retranslateUi(Form_TDFig)
        QtCore.QMetaObject.connectSlotsByName(Form_TDFig)

    def retranslateUi(self, Form_TDFig):
        _translate = QtCore.QCoreApplication.translate
        Form_TDFig.setWindowTitle(_translate("Form_TDFig", "Form"))
        self.label.setText(_translate("Form_TDFig", "选择剖面："))
        self.label_2.setText(_translate("Form_TDFig", "--"))
        self.comboBox_TDFig.setItemText(0, _translate("Form_TDFig", "绘制完整剖面"))
        self.comboBox_TDFig.setItemText(1, _translate("Form_TDFig", "绘制上升剖面"))
        self.comboBox_TDFig.setItemText(2, _translate("Form_TDFig", "绘制下降剖面"))
        self.pushButton_TDFig.setText(_translate("Form_TDFig", "画图"))
        self.pushButton_clear.setText(_translate("Form_TDFig", "清除画图"))
