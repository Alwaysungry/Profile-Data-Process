# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SDFig.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_SDFig(object):
    def setupUi(self, Form_SDFig):
        Form_SDFig.setObjectName("Form_SDFig")
        Form_SDFig.resize(1047, 640)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form_SDFig)
        self.verticalLayout.setContentsMargins(0, 6, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form_SDFig)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 2, 0, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBoxSD_start = QtWidgets.QSpinBox(self.widget)
        self.spinBoxSD_start.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBoxSD_start.setMinimum(1)
        self.spinBoxSD_start.setMaximum(999)
        self.spinBoxSD_start.setObjectName("spinBoxSD_start")
        self.horizontalLayout.addWidget(self.spinBoxSD_start)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.spinBoxSD_stop = QtWidgets.QSpinBox(self.widget)
        self.spinBoxSD_stop.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBoxSD_stop.setMinimum(1)
        self.spinBoxSD_stop.setMaximum(999)
        self.spinBoxSD_stop.setObjectName("spinBoxSD_stop")
        self.horizontalLayout.addWidget(self.spinBoxSD_stop)
        self.comboBox_SDFig = QtWidgets.QComboBox(self.widget)
        self.comboBox_SDFig.setObjectName("comboBox_SDFig")
        self.comboBox_SDFig.addItem("")
        self.comboBox_SDFig.addItem("")
        self.comboBox_SDFig.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_SDFig)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_SDFig = QtWidgets.QPushButton(self.widget)
        self.pushButton_SDFig.setObjectName("pushButton_SDFig")
        self.horizontalLayout.addWidget(self.pushButton_SDFig)
        self.pushButton_clear = QtWidgets.QPushButton(self.widget)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout.addWidget(self.pushButton_clear)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(6, 1)
        self.horizontalLayout.setStretch(9, 1)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(Form_SDFig)
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_SDFig = QtWidgets.QGridLayout()
        self.gridLayout_SDFig.setContentsMargins(0, -1, -1, -1)
        self.gridLayout_SDFig.setObjectName("gridLayout_SDFig")
        self.gridLayout_2.addLayout(self.gridLayout_SDFig, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget_2)
        self.verticalLayout.setStretch(1, 20)

        self.retranslateUi(Form_SDFig)
        QtCore.QMetaObject.connectSlotsByName(Form_SDFig)

    def retranslateUi(self, Form_SDFig):
        _translate = QtCore.QCoreApplication.translate
        Form_SDFig.setWindowTitle(_translate("Form_SDFig", "Form"))
        self.label.setText(_translate("Form_SDFig", "选择剖面："))
        self.label_2.setText(_translate("Form_SDFig", "--"))
        self.comboBox_SDFig.setItemText(0, _translate("Form_SDFig", "绘制完整剖面"))
        self.comboBox_SDFig.setItemText(1, _translate("Form_SDFig", "绘制上升剖面"))
        self.comboBox_SDFig.setItemText(2, _translate("Form_SDFig", "绘制下降剖面"))
        self.pushButton_SDFig.setText(_translate("Form_SDFig", "画图"))
        self.pushButton_clear.setText(_translate("Form_SDFig", "清除画图"))
