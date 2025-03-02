# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yaosuFig.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_yaosu(object):
    def setupUi(self, Form_yaosu):
        Form_yaosu.setObjectName("Form_yaosu")
        Form_yaosu.resize(1047, 660)
        Form_yaosu.setStyleSheet("")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form_yaosu)
        self.verticalLayout.setContentsMargins(0, 6, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Form_yaosu)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 2, 0, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.dateTimeEdit_ysstart = QtWidgets.QDateTimeEdit(self.widget)
        self.dateTimeEdit_ysstart.setCalendarPopup(True)
        self.dateTimeEdit_ysstart.setObjectName("dateTimeEdit_ysstart")
        self.horizontalLayout.addWidget(self.dateTimeEdit_ysstart)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.dateTimeEdit_ysend = QtWidgets.QDateTimeEdit(self.widget)
        self.dateTimeEdit_ysend.setCalendarPopup(True)
        self.dateTimeEdit_ysend.setObjectName("dateTimeEdit_ysend")
        self.horizontalLayout.addWidget(self.dateTimeEdit_ysend)
        self.pushButton_updatetime = QtWidgets.QPushButton(self.widget)
        self.pushButton_updatetime.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_updatetime.setText("")
        self.pushButton_updatetime.setAutoRepeatDelay(299)
        self.pushButton_updatetime.setObjectName("pushButton_updatetime")
        self.horizontalLayout.addWidget(self.pushButton_updatetime)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_Tyaosu = QtWidgets.QPushButton(self.widget)
        self.pushButton_Tyaosu.setObjectName("pushButton_Tyaosu")
        self.horizontalLayout.addWidget(self.pushButton_Tyaosu)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.pushButton_Syaosu = QtWidgets.QPushButton(self.widget)
        self.pushButton_Syaosu.setObjectName("pushButton_Syaosu")
        self.horizontalLayout.addWidget(self.pushButton_Syaosu)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButton_clean = QtWidgets.QPushButton(self.widget)
        self.pushButton_clean.setObjectName("pushButton_clean")
        self.horizontalLayout.addWidget(self.pushButton_clean)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addWidget(self.widget)
        self.widget_yaosuFig = QtWidgets.QWidget(Form_yaosu)
        self.widget_yaosuFig.setObjectName("widget_yaosuFig")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_yaosuFig)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout_yaosufig = QtWidgets.QGridLayout()
        self.gridLayout_yaosufig.setObjectName("gridLayout_yaosufig")
        self.gridLayout_2.addLayout(self.gridLayout_yaosufig, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.widget_yaosuFig)
        self.verticalLayout.setStretch(1, 20)

        self.retranslateUi(Form_yaosu)
        QtCore.QMetaObject.connectSlotsByName(Form_yaosu)

    def retranslateUi(self, Form_yaosu):
        _translate = QtCore.QCoreApplication.translate
        Form_yaosu.setWindowTitle(_translate("Form_yaosu", "Form"))
        self.label.setText(_translate("Form_yaosu", "时间段："))
        self.dateTimeEdit_ysstart.setDisplayFormat(_translate("Form_yaosu", "yyyy/MM/dd HH:mm:ss.zzz"))
        self.label_2.setText(_translate("Form_yaosu", "至"))
        self.dateTimeEdit_ysend.setDisplayFormat(_translate("Form_yaosu", "yyyy/MM/dd HH:mm:ss.zzz"))
        self.pushButton_Tyaosu.setText(_translate("Form_yaosu", "温度要素图"))
        self.pushButton_Syaosu.setText(_translate("Form_yaosu", "盐度要素图"))
        self.pushButton_clean.setText(_translate("Form_yaosu", "清除画图"))
