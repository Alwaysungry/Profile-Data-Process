import os
import sys
import _socket


from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QStackedLayout, QTableView, QHeaderView, QTableWidgetItem, QWidget
import pyqtgraph as pg
import numpy as np



from need.Function import function as fc
from UIdesign.mainwindow  import Ui_MainWindow
from UIdesign.home import Ui_Form_home
from need.plot import MyFigure, TDFigWidget, SDFigWidget, TProFigWidget,SProFigWidget, yaosuFigWidget

def getRealpath(s):
    import os, sys
    p = os.path.realpath(sys.path[0])
    p = p.replace(r'\base_library.zip', '')
    p = p + s
    return p


class FramehomePage(QtWidgets.QWidget, Ui_Form_home):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.gif = QMovie('.\\image\\ass.gif')
        self.label.setMovie(self.gif)
        self.gif.setScaledSize(QSize(1154,664))
        self.gif.start()


class FramedataPage(fc,MyFigure):
    def __init__(self):
        super().__init__()
        # self.setupUi(self)
        self.tableWidget_datainfo.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.pushButton_daorusj.clicked.connect(self.loaddata)
        self.pushButton_txt.clicked.connect(self.generatetxt)
        self.pushButton_plotfig.clicked.connect(self.plotfigure1)
        self.figure1 = pg.PlotWidget(self, background='w')
        self.gridLayout_fig.addWidget(self.figure1)
        self.figure1.getViewBox().invertY(True)
        self.figure1.showGrid(x=True,y=True)
        self.figure1.setLabel('left', "Depth", units='m')

        self.label.setStyleSheet('''Qlabel{
        font:13px}''')
        self.label_2.setStyleSheet('''Qlabel{
        font:13px}''')

        self.dateTimeEdit_datastart.setStyleSheet('''#dateTimeEdit_datastart{
                                                                padding-right: 15px; /* make room for the arrows */
                                                                border:1px solid gray;
                                                                border-radius:5px;
                                                                padding: 5px;
                                                                height : 14px;
                                                                font:13px
                                                                }
                                                                #dateTimeEdit_datastart QAbstractItemView::item{
                                                                height:20px;
                                                                }
                                                                #dateTimeEdit_datastart::drop-down{
                                                                border: 0px;
                                                                }
                                                                #dateTimeEdit_datastart::down-arrow{
                                                                image:url("./image/downarrow.png");
                                                                width: 15px;
                                                                height:15px;
                                                                }
                                                    ''')


        self.dateTimeEdit_dataend.setStyleSheet('''#dateTimeEdit_dataend{
                                                                padding-right: 15px; /* make room for the arrows */
                                                                border:1px solid gray;
                                                                border-radius:5px;
                                                                padding: 5px;
                                                                height : 14px;
                                                                font:13px
                                                                }
                                                                #dateTimeEdit_dataend QAbstractItemView::item{
                                                                height:20px;
                                                                }
                                                                #dateTimeEdit_dataend::drop-down{
                                                                border: 0px;
                                                                }
                                                                #dateTimeEdit_dataend::down-arrow{
                                                                image:url("./image/downarrow.png");
                                                                width: 15px;
                                                                height:15px;
                                                                }
                                                    ''')

        self.pushButton_daorusj.setStyleSheet(''' 
                                                                    QPushButton
                                                                    {text-align : center;
                                                                    background-color : white;
                                                                    font: normal;
                                                                    border-color: gray;
                                                                    border-width: 1px;
                                                                    border-radius: 5px;
                                                                    padding: 7px;
                                                                    height : 14px;
                                                                    border-style: outset;
                                                                    font : 13px;}
                                                                    QPushButton:pressed
                                                                    {text-align : center;
                                                                    background-color : light gray;
                                                                    font: bold;
                                                                    border-color: gray;
                                                                    border-width: 2px;
                                                                    border-radius: 5px;
                                                                    padding: 7px;
                                                                    height : 14px;
                                                                    border-style: outset;
                                                                    font : 13px;}
                                                                    ''')
        self.pushButton_plotfig.setStyleSheet(''' 
                                                            QPushButton
                                                            {text-align : center;
                                                            background-color : white;
                                                            font: bold;
                                                            border-color: gray;
                                                            border-width: 1px;
                                                            border-radius: 5px;
                                                            padding: 7px;
                                                            height : 14px;
                                                            border-style: outset;
                                                            font : 13px;}
                                                            QPushButton:pressed
                                                            {text-align : center;
                                                            background-color : light gray;
                                                            font: bold;
                                                            border-color: gray;
                                                            border-width: 2px;
                                                            border-radius: 5px;
                                                            padding: 7px;
                                                            height : 14px;
                                                            border-style: outset;
                                                            font : 13px;}
                                                            ''')
        self.pushButton_txt.setStyleSheet(''' 
                                                                   QPushButton
                                                                   {text-align : center;
                                                                   background-color : white;
                                                                   font: bold;
                                                                   border-color: gray;
                                                                   border-width: 1px;
                                                                   border-radius: 5px;
                                                                   padding: 7px;
                                                                   height : 14px;
                                                                   border-style: outset;
                                                                   font : 13px;}
                                                                   QPushButton:pressed
                                                                   {text-align : center;
                                                                   background-color : light gray;
                                                                   font: bold;
                                                                   border-color: gray;
                                                                   border-width: 2px;
                                                                   border-radius: 5px;
                                                                   padding: 7px;
                                                                   height : 14px;
                                                                   border-style: outset;
                                                                   font : 13px;}
                                                                   ''')


class FrameyaosuFigPage(yaosuFigWidget):
    def __init__(self):
        super(FrameyaosuFigPage,self).__init__()

        self.label.setStyleSheet('''font:13px''')
        self.label_2.setStyleSheet('font:13px')

        self.dateTimeEdit_ysstart.setStyleSheet('''             #dateTimeEdit_ysstart{
                                                                padding-right: 15px; /* make room for the arrows */
                                                                border:1px solid gray;
                                                                border-radius:5px;
                                                                padding: 5px;
                                                                height : 14px;
                                                                font:13px
                                                                }
                                                                #dateTimeEdit_ysstart QAbstractItemView::item{
                                                                height:20px;
                                                                }
                                                                #dateTimeEdit_ysstart::drop-down{
                                                                border: 0px;
                                                                }
                                                                #dateTimeEdit_ysstart::down-arrow{
                                                                image:url("./image/downarrow.png");
                                                                width: 15px;
                                                                height:15px;
                                                                }
                                                    ''')
        self.dateTimeEdit_ysend.setStyleSheet('''#dateTimeEdit_ysend{
                                                                padding-right: 15px; /* make room for the arrows */
                                                                border:1px solid gray;
                                                                border-radius:5px;
                                                                padding: 5px;
                                                                height : 14px;
                                                                font:13px
                                                                }
                                                                #dateTimeEdit_ysend QAbstractItemView::item{
                                                                height:20px;
                                                                }
                                                                #dateTimeEdit_ysend::drop-down{
                                                                border: 0px;
                                                                }
                                                                #dateTimeEdit_ysend::down-arrow{
                                                                image:url("./image/downarrow.png");
                                                                width: 15px;
                                                                height:15px;
                                                                }
                                                    ''')

        self.pushButton_updatetime.setIcon(QIcon(".\\image\\refresh.png"))
        self.pushButton_updatetime.setStyleSheet("border:none;")

        self.pushButton_Tyaosu.setStyleSheet(''' 
                                                                    QPushButton
                                                                    {text-align : center;
                                                                    background-color : white;
                                                                    font: normal;
                                                                    border-color: gray;
                                                                    border-width: 1px;
                                                                    border-radius: 5px;
                                                                    padding: 7px;
                                                                    height : 14px;
                                                                    border-style: outset;
                                                                    font : 13px;}
                                                                    QPushButton:pressed
                                                                    {text-align : center;
                                                                    background-color : light gray;
                                                                    font: bold;
                                                                    border-color: gray;
                                                                    border-width: 2px;
                                                                    border-radius: 5px;
                                                                    padding: 7px;
                                                                    height : 14px;
                                                                    border-style: outset;
                                                                    font : 13px;}
                                                                    ''')
        self.pushButton_Syaosu.setStyleSheet(''' 
                                                                    QPushButton
                                                                    {text-align : center;
                                                                    background-color : white;
                                                                    font: normal;
                                                                    border-color: gray;
                                                                    border-width: 1px;
                                                                    border-radius: 5px;
                                                                    padding: 7px;
                                                                    height : 14px;
                                                                    border-style: outset;
                                                                    font : 13px;}
                                                                    QPushButton:pressed
                                                                    {text-align : center;
                                                                    background-color : light gray;
                                                                    font: bold;
                                                                    border-color: gray;
                                                                    border-width: 2px;
                                                                    border-radius: 5px;
                                                                    padding: 7px;
                                                                    height : 14px;
                                                                    border-style: outset;
                                                                    font : 13px;}
                                                                    ''')

        self.pushButton_clean.setIcon(QIcon('.\\image\\eraser.png'))
        self.pushButton_clean.setStyleSheet(''' 
                                                                    QPushButton
                                                                    {text-align : center;
                                                                    background-color : white;
                                                                    font: bold;
                                                                    border-color: gray;
                                                                    border-width: 1px;
                                                                    border-radius: 5px;
                                                                    padding: 6px;
                                                                    height : 14px;
                                                                    border-style: outset;
                                                                    font : 13px;}
                                                                    QPushButton:pressed
                                                                    {text-align : center;
                                                                    background-color : light gray;
                                                                    font: bold;
                                                                    border-color: gray;
                                                                    border-width: 2px;
                                                                    border-radius: 5px;
                                                                    padding: 6px;
                                                                    height : 14px;
                                                                    border-style: outset;
                                                                    font : 13px;}
                                                                    ''')


class FrameSDFigPage(SDFigWidget):
    def __init__(self):
        super(FrameSDFigPage,self).__init__()
        # self.setupUi(self)

        self.label.setStyleSheet('font:13px')
        self.label_2.setStyleSheet('font:13px')

        self.spinBoxSD_start.setStyleSheet('''QSpinBox {
                                                    padding-right: 15px; /* make room for the arrows */
                                                    border:1px solid gray;
                                                    border-radius:5px;
                                                    padding: 5px;
                                                    height : 12px;
                                                    font:13px
                                                    }

                                                    QSpinBox::up-button {
                                                    border-image:url("./image/uparrow.png")
                                                    }

                                                    QSpinBox::down-button {
                                                    border-image:url("./image/downarrow.png")
                                                    }

                                                    QSpinBox::up-button:pressed {
                                                    margin-top:3px;
                                                    }

                                                    QSpinBox::down-button:pressed {
                                                    margin-bottom:3px;
                                                    }''')

        self.spinBoxSD_stop.setStyleSheet('''QSpinBox {
                                                            padding-right: 15px; /* make room for the arrows */
                                                            border:1px solid gray;
                                                            border-radius:5px;
                                                            padding: 5px;
                                                            height : 12px;

                                                            }

                                                            QSpinBox::up-button {
                                                            border-image:url("./image/uparrow.png")
                                                            }

                                                            QSpinBox::down-button {
                                                            border-image:url("./image/downarrow.png")
                                                            }

                                                            QSpinBox::up-button:pressed {
                                                            margin-top:3px;
                                                            }

                                                            QSpinBox::down-button:pressed {
                                                            margin-bottom:3px;
                                                            }''')

        self.comboBox_SDFig.setStyleSheet('''#comboBox_SDFig{
                                                                padding-right: 15px; /* make room for the arrows */
                                                                border:1px solid gray;
                                                                border-radius:5px;
                                                                padding: 5px;
                                                                height : 13px;
                                                                }
                                                                #comboBox_SDFig QAbstractItemView::item{
                                                                height:20px;
                                                                }
                                                                #comboBox_SDFig::drop-down{
                                                                border: 0px;
                                                                }
                                                                #comboBox_SDFig::down-arrow{
                                                                image:url("./image/downarrow.png");
                                                                width: 15px;
                                                                height:15px;
                                                                }
                                                    ''')
        self.pushButton_clear.setStyleSheet(''' 
                                             QPushButton
                                             {text-align : center;
                                             background-color : white;
                                             font: bold;
                                             border-color: gray;
                                             border-width: 1px;
                                             border-radius: 5px;
                                             padding: 6px;
                                             height : 14px;
                                             border-style: outset;
                                             font : 14px;}
                                             QPushButton:pressed
                                             {text-align : center;
                                             background-color : light gray;
                                             font: bold;
                                             border-color: gray;
                                             border-width: 2px;
                                             border-radius: 5px;
                                             padding: 6px;
                                             height : 14px;
                                             border-style: outset;
                                             font : 14px;}
                                             ''')
        self.pushButton_SDFig.setIcon(QIcon(".\\image\\plot1.png"))
        self.pushButton_SDFig.setStyleSheet(''' 
                                             QPushButton
                                             {text-align : center;
                                             background-color : white;
                                             font: bold;
                                             border-color: gray;
                                             border-width: 1px;
                                             border-radius: 5px;
                                             padding: 6px;
                                             height : 14px;
                                             border-style: outset;
                                             font : 13px;}
                                             QPushButton:pressed
                                             {text-align : center;
                                             background-color : light gray;
                                             font: bold;
                                             border-color: gray;
                                             border-width: 2px;
                                             border-radius: 5px;
                                             padding: 6px;
                                             height : 14px;
                                             border-style: outset;
                                             font : 13px;}
                                             ''')
        self.pushButton_clear.setIcon(QIcon('.\\image\\eraser.png'))
        self.pushButton_clear.setStyleSheet(''' 
                                                            QPushButton
                                                            {text-align : center;
                                                            background-color : white;
                                                            font: bold;
                                                            border-color: gray;
                                                            border-width: 1px;
                                                            border-radius: 5px;
                                                            padding: 6px;
                                                            height : 14px;
                                                            border-style: outset;
                                                            font : 13px;}
                                                            QPushButton:pressed
                                                            {text-align : center;
                                                            background-color : light gray;
                                                            font: bold;
                                                            border-color: gray;
                                                            border-width: 2px;
                                                            border-radius: 5px;
                                                            padding: 6px;
                                                            height : 14px;
                                                            border-style: outset;
                                                            font : 13px;}
                                                            ''')


class FrameTDFigPage(TDFigWidget):
    def __init__(self):
        super(FrameTDFigPage,self).__init__()
        # self.setupUi(self)
        # self.tdfigure = NewFigure1()
        # self.gridLayout_TDFig.addWidget(self.tdfigure)
        self.label.setStyleSheet('font:13px')
        self.label_2.setStyleSheet('font:13px')

        self.spinBoxTD_start.setStyleSheet('''QSpinBox {
                                            padding-right: 15px; /* make room for the arrows */
                                            border:1px solid gray;
                                            border-radius:5px;
                                            padding: 5px;
                                            height : 12px;
                                            font:13px
                                            }

                                            QSpinBox::up-button {
                                            border-image:url("./image/uparrow.png")
                                            }

                                            QSpinBox::down-button {
                                            border-image:url("./image/downarrow.png")
                                            }

                                            QSpinBox::up-button:pressed {
                                            margin-top:3px;
                                            }

                                            QSpinBox::down-button:pressed {
                                            margin-bottom:3px;
                                            }''')

        self.spinBoxTD_stop.setStyleSheet('''QSpinBox {
                                                    padding-right: 15px; /* make room for the arrows */
                                                    border:1px solid gray;
                                                    border-radius:5px;
                                                    padding: 5px;
                                                    height : 12px;

                                                    }

                                                    QSpinBox::up-button {
                                                    border-image:url("./image/uparrow.png")
                                                    }

                                                    QSpinBox::down-button {
                                                    border-image:url("./image/downarrow.png")
                                                    }

                                                    QSpinBox::up-button:pressed {
                                                    margin-top:3px;
                                                    }

                                                    QSpinBox::down-button:pressed {
                                                    margin-bottom:3px;
                                                    }''')

        self.comboBox_TDFig.setStyleSheet('''#comboBox_TDFig{
                                                        padding-right: 15px; /* make room for the arrows */
                                                        border:1px solid gray;
                                                        border-radius:5px;
                                                        padding: 5px;
                                                        height : 13px;
                                                        }
                                                        #comboBox_TDFig QAbstractItemView::item{
                                                        height:20px;
                                                        }
                                                        #comboBox_TDFig::drop-down{
                                                        border: 0px;
                                                        }
                                                        #comboBox_TDFig::down-arrow{
                                                        image:url("./image/downarrow.png");
                                                        width: 15px;
                                                        height:15px;
                                                        }
                                            ''')
        self.pushButton_clear.setIcon(QIcon('.\\image\\eraser.png'))
        self.pushButton_clear.setStyleSheet(''' 
                                                    QPushButton
                                                    {text-align : center;
                                                    background-color : white;
                                                    font: bold;
                                                    border-color: gray;
                                                    border-width: 1px;
                                                    border-radius: 5px;
                                                    padding: 6px;
                                                    height : 14px;
                                                    border-style: outset;
                                                    font : 13px;}
                                                    QPushButton:pressed
                                                    {text-align : center;
                                                    background-color : light gray;
                                                    font: bold;
                                                    border-color: gray;
                                                    border-width: 2px;
                                                    border-radius: 5px;
                                                    padding: 6px;
                                                    height : 14px;
                                                    border-style: outset;
                                                    font : 13px;}
                                                    ''')
        self.pushButton_TDFig.setIcon(QIcon(".\\image\\plot1.png"))
        self.pushButton_TDFig.setStyleSheet(''' 
                                                    QPushButton
                                                    {text-align : center;
                                                    background-color : white;
                                                    font: bold;
                                                    border-color: gray;
                                                    border-width: 1px;
                                                    border-radius: 5px;
                                                    padding: 6px;
                                                    height : 14px;
                                                    border-style: outset;
                                                    font : 13px;}
                                                    QPushButton:pressed
                                                    {text-align : center;
                                                    background-color : light gray;
                                                    font: bold;
                                                    border-color: gray;
                                                    border-width: 2px;
                                                    border-radius: 5px;
                                                    padding: 6px;
                                                    height : 14px;
                                                    border-style: outset;
                                                    font : 13px;}
                                                    ''')


class FrameSProFigPage(SProFigWidget):
    def __init__(self):
        super().__init__()
        # self.setupUi(self)

        self.pushButton_SPro.setIcon(QIcon(".\\image\\plot2.png"))
        self.pushButton_SPro.setStyleSheet(''' 
                                                            QPushButton
                                                            {text-align : center;
                                                            background-color : white;
                                                            font: bold;
                                                            border-color: gray;
                                                            border-width: 1px;
                                                            border-radius: 5px;
                                                            padding: 6px;
                                                            height : 14px;
                                                            border-style: outset;
                                                            font : 14px;}
                                                            QPushButton:pressed
                                                            {text-align : center;
                                                            background-color : light gray;
                                                            font: bold;
                                                            border-color: gray;
                                                            border-width: 2px;
                                                            border-radius: 5px;
                                                            padding: 6px;
                                                            height : 14px;
                                                            border-style: outset;
                                                            font : 14px;}
                                                            ''')
        self.pushButton_clear.setIcon(QIcon(".\\image\\eraser.png"))
        self.pushButton_clear.setStyleSheet(''' 
                                                                    QPushButton
                                                                    {text-align : center;
                                                                    background-color : white;
                                                                    font: bold;
                                                                    border-color: gray;
                                                                    border-width: 1px;
                                                                    border-radius: 5px;
                                                                    padding: 6px;
                                                                    height : 14px;
                                                                    border-style: outset;
                                                                    font : 14px;}
                                                                    QPushButton:pressed
                                                                    {text-align : center;
                                                                    background-color : light gray;
                                                                    font: bold;
                                                                    border-color: gray;
                                                                    border-width: 2px;
                                                                    border-radius: 5px;
                                                                    padding: 6px;
                                                                    height : 14px;
                                                                    border-style: outset;
                                                                    font : 14px;}
                                                                    ''')


class FrameTProFigPage(TProFigWidget):
    def __init__(self):
        super().__init__()
        # self.setupUi(self)

        self.pushButton_TPro.setIcon(QIcon(".\\image\\plot2.png"))
        self.pushButton_TPro.setStyleSheet(''' 
                                                                    QPushButton
                                                                    {text-align : center;
                                                                    background-color : white;
                                                                    font: bold;
                                                                    border-color: gray;
                                                                    border-width: 1px;
                                                                    border-radius: 5px;
                                                                    padding: 6px;
                                                                    height : 14px;
                                                                    border-style: outset;
                                                                    font : 14px;}
                                                                    QPushButton:pressed
                                                                    {text-align : center;
                                                                    background-color : light gray;
                                                                    font: bold;
                                                                    border-color: gray;
                                                                    border-width: 2px;
                                                                    border-radius: 5px;
                                                                    padding: 6px;
                                                                    height : 14px;
                                                                    border-style: outset;
                                                                    font : 14px;}
                                                                    ''')
        self.pushButton_clear.setIcon(QIcon(".\\image\\eraser.png"))
        self.pushButton_clear.setStyleSheet(''' 
                                                                            QPushButton
                                                                            {text-align : center;
                                                                            background-color : white;
                                                                            font: bold;
                                                                            border-color: gray;
                                                                            border-width: 1px;
                                                                            border-radius: 5px;
                                                                            padding: 6px;
                                                                            height : 14px;
                                                                            border-style: outset;
                                                                            font : 14px;}
                                                                            QPushButton:pressed
                                                                            {text-align : center;
                                                                            background-color : light gray;
                                                                            font: bold;
                                                                            border-color: gray;
                                                                            border-width: 2px;
                                                                            border-radius: 5px;
                                                                            padding: 6px;
                                                                            height : 14px;
                                                                            border-style: outset;
                                                                            font : 14px;}
                                                                            ''')



class Mainwindow(Ui_MainWindow,QtWidgets.QMainWindow):
    def __init__(self):
        super(Mainwindow,self).__init__()
        self.setupUi(self)
        #实例化一个堆叠布局
        self.qsl = QStackedLayout(self.frame_3)
        #实例化分页页面
        self.home = FramehomePage()
        self.data = FramedataPage()
        self.yaosu = FrameyaosuFigPage()
        self.SDFig = FrameSDFigPage()
        self.TDFig = FrameTDFigPage()
        self.SProFig = FrameSProFigPage()
        self.TProFig = FrameTProFigPage()

        #加入到布局
        self.qsl.addWidget(self.home)
        self.qsl.addWidget(self.data)
        self.qsl.addWidget(self.yaosu)
        self.qsl.addWidget(self.TDFig)
        self.qsl.addWidget(self.SDFig)
        self.qsl.addWidget(self.TProFig)
        self.qsl.addWidget(self.SProFig)

        #设置控制函数
        self.controller()



        self.pushButton_zuixiao.clicked.connect(self.minsize)
        self.pushButton_fanda.clicked.connect(self.maxsize)
        self.pushButton_guanbi.clicked.connect(self.close)
        self.pushButton_help.clicked.connect(self.open_helpfile)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Dialog)#窗口移动

        self.setWindowFlags(Qt.FramelessWindowHint)#窗口无边框

        self.pushButton_icon.setIcon(QIcon('.\\image\\ouc.png'))
        self.pushButton_icon.setIconSize(QSize(192,90))
        self.pushButton_icon.setStyleSheet("border:none")

        self.widget_header.setStyleSheet('''QWidget{background-color:#5AA8F8 }''')
        self.pushButton_zuixiao.setIcon(QIcon('.\\image\\min.png'))
        self.pushButton_zuixiao.setIconSize(QSize(20,30))
        self.pushButton_zuixiao.setStyleSheet(''' 
                                             QPushButton{
                                              border:none;
        text-align:center}
        QPushButton:hover{background-color:gray}
        ''')
        self.pushButton_fanda.setIcon(QIcon('.\\image\\max.png'))
        self.pushButton_fanda.setIconSize(QSize(20, 30))
        self.pushButton_fanda.setStyleSheet(''' 
                                             QPushButton{
                                              border:none;
        text-align:center}
        QPushButton:hover{background-color:gray}
         ''')
        self.pushButton_guanbi.setIcon((QIcon('.\\image\\close.png')))

        self.pushButton_guanbi.setIconSize(QSize(20, 30))
        self.pushButton_guanbi.setStyleSheet(''' 
                                             QPushButton{
                                              border:none;
        text-align:center}
        QPushButton:hover{background-color:red}
         ''')

        self.widget_Menu.setStyleSheet('''QWidget{
        background-color:#2C3237 }''')

        self.pushButton_1home.setIcon(QIcon('.\\image\\home.png'))
        self.pushButton_1home.setStyleSheet(''' 
                                             QPushButton{
                                              border:none;
        color:white;
        font:Microsoft YaHei;
        font-size:14px;
        height:55px;
        padding-left:5px;
        padding-right:10px;
        text-align:left;}
         QPushButton:hover{
        color:white;
        border:1px solid #111111;
        border-radius:0px;
        background:#111111;
    }
                                             ''')
        self.pushButton_2data.setIcon(QIcon('.\\image\\data.png'))
        self.pushButton_2data.setStyleSheet(''' 
                                                     QPushButton{
                                                      border:none;
                color:white;
                font:Microsoft YaHei;
                font-size:14px;
                height:55px;
                padding-left:5px;
                padding-right:10px;
                text-align:left;}
                 QPushButton:hover{
                color:white;
                border:1px solid #111111;
                border-radius:0px;
                background:#111111;
            }
                                                     ''')
        self.pushButton_3Fig.setIcon(QIcon('.\\image\\fig.png'))
        self.pushButton_3Fig.setStyleSheet(''' 
                                                             QPushButton{
                                                              border:none;
                        color:white;
                        font:Microsoft YaHei;
                        font-size:14px;
                        height:55px;
                        padding-left:5px;
                        padding-right:10px;
                        text-align:left;}
                        
                                                             ''')
        self.pushButton_4yaosu.setIcon(QIcon('.\\image\\plot1.png'))
        self.pushButton_4yaosu.setStyleSheet(''' 
                                                                     QPushButton{
                                                                      border:none;
                                color:white;
                                font:Microsoft YaHei;
                                font-size:12px;
                                height:55px;
                                padding-left:5px;
                                padding-right:10px;
                                text-align:center;}
                                 QPushButton:hover{
                                color:white;
                                border:1px solid #111111;
                                border-radius:0px;
                                background:#111111;
                            }
                                                                     ''')
        self.pushButton_5TDFig.setIcon(QIcon('.\\image\\plot1.png'))
        self.pushButton_5TDFig.setStyleSheet(''' 
                                                                            QPushButton{
                                                                             border:none;
                                       color:white;
                                       font:Microsoft YaHei;
                                       font-size:12px;
                                       height:55px;
                                       padding-left:5px;
                                       padding-right:10px;
                                       text-align:center;}
                                        QPushButton:hover{
                                       color:white;
                                       border:1px solid #111111;
                                       border-radius:0px;
                                       background:#111111;
                                   }
                                                                            ''')
        self.pushButton_6SDFig.setIcon(QIcon('.\\image\\plot1.png'))
        self.pushButton_6SDFig.setStyleSheet(''' 
                                                                                    QPushButton{
                                                                                     border:none;
                                               color:white;
                                               font:Microsoft YaHei;
                                               font-size:12px;
                                               height:55px;
                                               padding-left:5px;
                                               padding-right:10px;
                                               text-align:center;}
                                                QPushButton:hover{
                                               color:white;
                                               border:1px solid #111111;
                                               border-radius:0px;
                                               background:#111111;
                                           }
                                                                                    ''')
        self.pushButton_7TProFig.setIcon(QIcon('.\\image\\plot2.png'))
        self.pushButton_7TProFig.setStyleSheet(''' 
                                                                                            QPushButton{
                                                                                             border:none;
                                                       color:white;
                                                       font:Microsoft YaHei;
                                                       font-size:12px;
                                                       height:55px;
                                                       padding-left:5px;
                                                       padding-right:10px;
                                                       text-align:center;}
                                                        QPushButton:hover{
                                                       color:white;
                                                       border:1px solid #111111;
                                                       border-radius:0px;
                                                       background:#111111;
                                                   }
                                                                                            ''')
        self.pushButton_8SProFig.setIcon(QIcon('.\\image\\plot2.png'))
        self.pushButton_8SProFig.setStyleSheet(''' 
                                                                                                   QPushButton{
                                                                                                    border:none;
                                                              color:white;
                                                              font:Microsoft YaHei;
                                                              font-size:12px;
                                                              height:55px;
                                                              padding-left:5px;
                                                              padding-right:10px;
                                                              text-align:center;}
                                                               QPushButton:hover{
                                                              color:white;
                                                              border:1px solid #111111;
                                                              border-radius:0px;
                                                              background:#111111;
                                                          }
                                                                                                   ''')
        self.pushButton_help.setIcon(QIcon('.\\image\\help.png'))
        self.pushButton_help.setStyleSheet(''' 
                                                    QPushButton{
                                                     border:none;
               color:white;
               font:Microsoft YaHei;
               font-size:14px;
               height:55px;
               padding-left:5px;
               padding-right:10px;
               text-align:left;}
                QPushButton:hover{
               color:white;
               border:1px solid #111111;
               border-radius:0px;
               background:#111111;
           }
                                                    ''')


    def controller(self):
        self.pushButton_1home.clicked.connect(self.switch)
        self.pushButton_2data.clicked.connect(self.switch)
        self.pushButton_4yaosu.clicked.connect(self.switch)
        self.pushButton_5TDFig.clicked.connect(self.switch)
        self.pushButton_6SDFig.clicked.connect(self.switch)
        self.pushButton_7TProFig.clicked.connect(self.switch)
        self.pushButton_8SProFig.clicked.connect(self.switch)



    def switch(self):
        sender = self.sender().objectName()

        index = {
            "pushButton_1home":0,
            "pushButton_2data":1,
            "pushButton_4yaosu":2,
            "pushButton_5TDFig":3,
            "pushButton_6SDFig":4,
            "pushButton_7TProFig":5,
            "pushButton_8SProFig":6,
            "pushButton_yjxx":7,
            "pushButton_yjsz":8
        }

        self.qsl.setCurrentIndex(index[sender])

        # 无边框的拖动



    def mouseMoveEvent(self, e: QtGui.QMouseEvent):  # 重写移动事件
        if (e.x() >= 0 and e.x() <= 1240 and e.y() >= 0 and e.y() < 81):
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QtGui.QMouseEvent):
        if e.button() == QtCore.Qt.LeftButton:
            self._isTracking = True
            self._startPos = QtCore.QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QtGui.QMouseEvent):
        if e.button() == QtCore.Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

    def minsize(self):
        # 最小化
        self.showMinimized()

    def maxsize(self):
        # 最大化与复原
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def open_helpfile(self):
        self.msg_box = QtWidgets.QMessageBox
        self.msg_box.about(self,"使用帮助",'''进入软件后，首先导入数据，获得剖面个数、开始结束时间（剖面运动开始结束的时间，不是数据开始的时间）等信息。
生成运动图像：会获得在选定时间段浮标的深度-时间运动图像，选定时间可以在‘时间段’选择。
生成运动状态拐点文件：会生成一个txt文件，记录了浮标剖面运动开始和结束的时间、深度数据。
要素-深度分布图：在原来的运动图像上叠加温度或者盐度信息。
温度/盐度剖面图：绘制导入文件所有数据的温度/盐度剖面图。
注意：
    1.当键入‘时间段’中的数字无反应时，请点击时间框中的下拉按钮，选择时间。
    2.在点击‘导入数据’按钮后，之前导入的所有数据都会被清除，即使没有导入新文件。
    3.当选择的‘时间段’间隔过大时，绘图时间会变长；同样，在绘制温度/盐度剖面图时，所需的时间也会较长，并且此时软件可能会有卡顿。
''')




if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = Mainwindow()
    dialog.setWindowIcon(QIcon('.\\image\\icon.png'))
    # dialog.setWindowTitle("浮标数据分析系统")
    dialog.setWindowTitle("基于机器学习的海洋剖面观测设备仿真系统")

    dialog.show()
    sys.exit(app.exec_())