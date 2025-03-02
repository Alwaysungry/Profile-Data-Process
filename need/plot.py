import random

from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import numpy as np
import threading
import pyqtgraph as pg
from PyQt5.QtWidgets import QWidget, QMessageBox, QProgressBar

import matplotlib

from UIdesign.SDFig import Ui_Form_SDFig
from UIdesign.SProFig import Ui_Form_SProFig
from UIdesign.TDFig import Ui_Form_TDFig
from UIdesign.TProFig import Ui_Form_TProFig
from UIdesign.yaosuFig import Ui_Form_yaosu

matplotlib.use("Qt5Agg")  # 声明使用QT5

import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FC

from UIdesign.data import Ui_Form_data

import need.Function as fc
from need import Function



class MyFigure(QWidget,Ui_Form_data):
    def __init__(self):
        super(MyFigure, self).__init__()

    def plotfigure1(self):
        if len(Function.time_) != 0:
            time1 = self.dateTimeEdit_datastart.dateTime()
            time2 = self.dateTimeEdit_dataend.dateTime()
            start_datetime = time1.toString('yyyy-MM-dd HH:mm:ss.zzz')
            stop_datetime = time2.toString('yyyy-MM-dd HH:mm:ss.zzz')
            if start_datetime < stop_datetime:
                for i in range(len(Function.time_)):
                    if start_datetime == Function.time_[i]:
                        start_index = i

                for j in range(len(Function.time_)):
                    if stop_datetime == Function.time_[j]:
                        stop_index = j

                self.depth_array = np.array(Function.depth[start_index:stop_index])
                self.depth_array = self.depth_array.astype(np.float).tolist()
                self.x_time = []
                self.x_time.clear()
                self.x_time = Function.time_[start_index:stop_index]



                self.gridLayout_fig.removeWidget(self.figure1)  # F1为定义的图
                self.figure1.deleteLater()  # 此处为加入的代码

                self.figure1 = pg.PlotWidget(self, background='w')
                self.gridLayout_fig.addWidget(self.figure1)

                xax = self.figure1.getAxis('bottom')  # 坐标轴x
                ticks = [list(zip(range(0,len(self.x_time),10000), self.x_time))]  # 声明五个坐标，分别是
                xax.setTicks(ticks)
                self.figure1.getViewBox().invertY(True)
                self.figure1.showGrid(x=True,y=True)
                self.figure1.setLabel('left', "Depth", units='m')

                self.plot_data = self.figure1.plot( self.depth_array,pen = 'b')
                self.plot_data.setData( self.depth_array)
                print(Function.depth[0])
                print (self.depth_array[0])





            else:
                QMessageBox.warning(None,'提示！','时间间隔设置错误！')
        else:
            QMessageBox.information(None, "提示！", "请先导入数据！")


class yaosuFigWidget(QWidget,Ui_Form_yaosu):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_Tyaosu.clicked.connect(self.plot_click1)
        self.pushButton_Syaosu.clicked.connect(self.plot_click2)
        self.pushButton_updatetime.clicked.connect(self.updatetime)
        self.pushButton_clean.clicked.connect(self.cleanfig)

        self.fig = plt.Figure()
        self.canvas = FC(self.fig)
        self.ysfigure = self.fig.add_subplot(111)
        self.ysfigure.set_xlabel('Time')
        self.ysfigure.set_ylabel('Depth(m)')

        # self.ysfigure.invert_yaxis()

        self.picture_h_tb = NavigationToolbar(self.canvas, self.widget)

        self.gridLayout_yaosufig.addWidget(self.canvas)
        self.gridLayout_yaosufig.addWidget(self.picture_h_tb)

    def plot_click1(self):
        # plot1 = pool.submit(self.plottysfig)
        self.thread_plot_tys =threading.Thread(target=self.plottysfig)
        self.thread_plot_tys.start()

    def plot_click2(self):
        self.thread_plot_sys = threading.Thread(target=self.plotsysfig)
        self.thread_plot_sys.start()
        # plot2 = pool.submit(self.plotsysfig)

    def updatetime(self):
        self.dateTimeEdit_ysstart.setDateTime(fc.real_startdate)
        self.dateTimeEdit_ysend.setDateTime(fc.real_stopdate)
        self.dateTimeEdit_ysstart.setMinimumDateTime(fc.real_startdate)
        self.dateTimeEdit_ysstart.setMaximumDateTime(fc.real_stopdate)
        self.dateTimeEdit_ysend.setMinimumDateTime(fc.real_startdate)
        self.dateTimeEdit_ysend.setMaximumDateTime(fc.real_stopdate)

    def cleanfig(self):
        self.gridLayout_yaosufig.removeWidget(self.canvas)
        self.canvas.deleteLater()
        self.gridLayout_yaosufig.removeWidget(self.picture_h_tb)
        self.picture_h_tb.deleteLater()

        self.fig = plt.Figure()
        self.canvas = FC(self.fig)
        self.ysfigure = self.fig.add_subplot(111)

        self.ysfigure.set_xlabel('Time')
        self.ysfigure.set_ylabel('Depth(m)')
        self.gridLayout_yaosufig.addWidget(self.canvas)
        self.picture_h_tb = NavigationToolbar(self.canvas, self.widget)
        self.gridLayout_yaosufig.addWidget(self.picture_h_tb)


    def plottysfig(self):

        if len(Function.time_) != 0:
            time1 = self.dateTimeEdit_ysstart.dateTime()
            time2 = self.dateTimeEdit_ysend.dateTime()
            start_datetime = time1.toString('yyyy-MM-dd HH:mm:ss.zzz')
            stop_datetime = time2.toString('yyyy-MM-dd HH:mm:ss.zzz')
            if start_datetime < stop_datetime:
                for i in range(len(Function.time_)):
                    if start_datetime == Function.time_[i]:
                        self.start_index = i

                for j in range(len(Function.time_)):
                    if stop_datetime == Function.time_[j]:
                        self.stop_index = j

                self.x_time = []
                self.x_time.clear()
                self.x_time = Function.time_[self.start_index:self.stop_index]
                self.temperature = fc.temperature[self.start_index:self.stop_index]
                self.salinity = fc.salinity[self.start_index:self.stop_index]
                self.depth = fc.depth[self.start_index:self.stop_index]
                self.y_depth = np.array(self.depth)
                self.y_depth = self.y_depth.astype(np.float).tolist()
                self.y_temperature = np.array(self.temperature)
                self.y_temperature = self.y_temperature.astype(np.float).tolist()
                self.y_salinity = np.array(self.salinity)
                self.y_salinity = self.y_salinity.astype(np.float).tolist()

                cmp = plt.get_cmap('jet')
                norm = plt.Normalize(vmin=np.min(self.y_temperature), vmax=np.max(self.y_temperature), clip=True)
                # self.cleanfig()
                # self.ysfigure.cla()
                self.ysfigure.set_title('Temperature-Depth')
                self.ysfigure.set_xlabel('Time')
                self.ysfigure.set_ylabel('Depth(m)')
                self.ysax = self.ysfigure.scatter(self.x_time, self.y_depth, c=self.y_temperature, cmap=cmp,
                                                  norm=norm,
                                                  s=2)
                self.ysfigure.invert_yaxis()
                self.ysfigure.set_xticks([fc.time_[self.start_index],fc.time_[self.stop_index]])
                self.fig.colorbar(self.ysax, ax=self.ysfigure)

                self.canvas.draw()
            # else:
            #     QMessageBox.information(self, '提示！', '时间间隔设置错误！')

        # else:
        #     QMessageBox.information(None, '提示！', '请先导入数据！')


    def plotsysfig(self):

        if len(Function.time_) != 0:
            time1 = self.dateTimeEdit_ysstart.dateTime()
            time2 = self.dateTimeEdit_ysend.dateTime()
            start_datetime = time1.toString('yyyy-MM-dd HH:mm:ss.zzz')
            stop_datetime = time2.toString('yyyy-MM-dd HH:mm:ss.zzz')
            if start_datetime < stop_datetime:
                for i in range(len(Function.time_)):
                    if start_datetime == Function.time_[i]:
                        self.start_index = i

                for j in range(len(Function.time_)):
                    if stop_datetime == Function.time_[j]:
                        self.stop_index = j

                self.x_time = []
                self.x_time.clear()
                self.x_time = Function.time_[self.start_index:self.stop_index]
                self.temperature = fc.temperature[self.start_index:self.stop_index]
                self.salinity = fc.salinity[self.start_index:self.stop_index]
                self.depth = fc.depth[self.start_index:self.stop_index]
                self.y_depth = np.array(self.depth)
                self.y_depth = self.y_depth.astype(np.float).tolist()
                self.y_temperature = np.array(self.temperature)
                self.y_temperature = self.y_temperature.astype(np.float).tolist()
                self.y_salinity = np.array(self.salinity)
                self.y_salinity = self.y_salinity.astype(np.float).tolist()
                cmp = plt.get_cmap('jet')
                norm = plt.Normalize(vmin=np.min(self.y_salinity), vmax=np.max(self.y_salinity), clip=True)
                # self.cleanfig()
                # self.ysfigure.cla()
                self.ysfigure.set_title('Salinity-Depth')
                self.ysfigure.set_xlabel('Time')
                self.ysfigure.set_ylabel('Depth(m)')
                self.ysax = self.ysfigure.scatter(self.x_time, self.y_depth, c=self.y_salinity, cmap=cmp, norm=norm,
                                                  s=2)
                self.ysfigure.invert_yaxis()
                self.ysfigure.set_xticks([fc.time_[self.start_index],fc.time_[self.stop_index]])

                self.fig.colorbar(self.ysax, ax=self.ysfigure)

                self.canvas.draw()
        #     else:
        #         QMessageBox.warning(None, '提示！', '时间间隔设置错误！')
        # else:
        #     QMessageBox.warning(None, '提示！', '请先导入数据！')




class TDFigWidget(QWidget,Ui_Form_TDFig):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.fig = plt.Figure()
        self.canvas = FC(self.fig)
        self.tdfigure = self.fig.add_subplot(111)
        self.tdfigure.set_xlabel('Temperature(℃)')
        self.tdfigure.set_ylabel('Depth(m)')
        self.tdfigure.set_title('Temperature-Depth')
        self.tdfigure.invert_yaxis()
        self.picture_h_tb = NavigationToolbar(self.canvas,self.widget)
        self.gridLayout_TDFig.addWidget(self.canvas)
        self.gridLayout_TDFig.addWidget(self.picture_h_tb)

        self.pushButton_TDFig.clicked.connect(self.plottdfig)
        self.pushButton_clear.clicked.connect(self.cleanfig)


    def setUi(self):

        self.spinBoxTD_start.setMaximum(len(fc.final_peaks))
        self.spinBoxTD_stop.setMaximum(len(fc.final_peaks))

    def plottdfig(self):
        self.index = None
        self.start_index = None
        self.stop_index = None
        self.temperature = []
        self.depth = []
        self.x_temperature = []
        self.y_depth = []
        self.num = []
        if len(Function.time_) != 0:
            if self.spinBoxTD_start.value()<=len(fc.final_peaks) and \
                    self.spinBoxTD_stop.value()<=len(fc.final_peaks) and \
                    self.spinBoxTD_start.value()<=self.spinBoxTD_stop.value():
                for i in range(self.spinBoxTD_start.value(),self.spinBoxTD_stop.value()+1,1):
                    self.index = i - 1
                    if self.comboBox_TDFig.currentIndex() == 0:
                        self.start_index = fc.all_p_t[self.index * 2][0]
                        self.stop_index = fc.all_p_t[self.index * 2 + 2][0]
                    elif self.comboBox_TDFig.currentIndex() == 1:
                        self.start_index = fc.all_p_t[self.index * 2 + 1][0]
                        self.stop_index = fc.all_p_t[self.index * 2 + 2][0]
                    elif self.comboBox_TDFig.currentIndex() == 2:
                        self.start_index = fc.all_p_t[self.index * 2][0]
                        self.stop_index = fc.all_p_t[self.index * 2 + 1][0]

                    self.temperature = fc.temperature[self.start_index:self.stop_index]
                    self.depth = fc.depth[self.start_index:self.stop_index]
                    self.y_depth = np.array(self.depth)
                    self.y_depth = self.y_depth.astype(np.float).tolist()
                    self.x_temperature = np.array(self.temperature)
                    self.x_temperature = self.x_temperature.astype(np.float).tolist()

                    # self.tdfigure.invert_yaxis()
                    # self.tdfigure.cla()
                    # self.tdfigure.plot(self.x_temperature, self.y_depth)
                    linestyle_tuple = [
                        ('loosely dotted', (0, (1, 10))),
                        ('dotted', (0, (1, 1))),
                        ('densely dotted', (0, (1, 2))), ('loosely dashed', (0, (5, 10))),
                        ('dashed', (0, (5, 5))),
                        ('densely dashed', (0, (5, 1))), ('loosely dashdotted', (0, (3, 10, 1, 10))),
                        ('dashdotted', (0, (3, 5, 1, 5))),
                        ('densely dashdotted', (0, (3, 1, 1, 1))), ('dashdotdotted', (0, (3, 5, 1, 5, 1, 5))),
                        ('loosely dashdotdotted', (0, (3, 10, 1, 10, 1, 10))),
                        ('densely dashdotdotted', (0, (3, 1, 1, 1, 1, 1)))]
                    suiyi = random.randint(0,12)
                    # marker = ['1', '>', '<', '+', '*','o','v','8','s','D','d','p','H',',','v','3','P',"X"]
                    self.tdfigure.plot(self.x_temperature, self.y_depth)
                    # self.tdfigure.legend()
                    self.tdfigure.set_xlabel('Temperature(℃)')
                    self.tdfigure.set_ylabel('Depth(m)')
                    # self.tdfigure.set_xticks(np.linspace(min(self.temperature), max(self.temperature), 5))
                    self.canvas.draw()
            else:
                QMessageBox.information(self, "提示！", "超出最大剖面数或间隔设置错误！")
        else:
            QMessageBox.information(self, "提示！", "请先导入数据！")


    def cleanfig(self):
        self.gridLayout_TDFig.removeWidget(self.canvas)
        self.canvas.deleteLater()
        self.gridLayout_TDFig.removeWidget(self.picture_h_tb)
        self.picture_h_tb.deleteLater()
        self.fig = plt.Figure()
        self.canvas = FC(self.fig)
        self.tdfigure = self.fig.add_subplot(111)
        self.tdfigure.set_xlabel('Temperature(℃)')
        self.tdfigure.set_ylabel('Depth(m)')
        self.tdfigure.set_title('Temperature-Depth')
        self.tdfigure.invert_yaxis()
        self.gridLayout_TDFig.addWidget(self.canvas)
        self.picture_h_tb = NavigationToolbar(self.canvas, self.widget)
        self.gridLayout_TDFig.addWidget(self.picture_h_tb)


class SDFigWidget(QWidget,Ui_Form_SDFig):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.fig = plt.Figure()
        self.canvas = FC(self.fig)
        self.sdfigure = self.fig.add_subplot(111)
        self.sdfigure.set_xlabel('Salinity')
        self.sdfigure.set_ylabel('Depth(m)')
        self.sdfigure.set_title('Salinity-Depth')
        self.sdfigure.invert_yaxis()
        self.picture_h_tb = NavigationToolbar(self.canvas,self.widget)
        self.gridLayout_SDFig.addWidget(self.canvas)
        self.gridLayout_SDFig.addWidget(self.picture_h_tb)

        self.pushButton_SDFig.clicked.connect(self.plotsdfig)
        self.pushButton_clear.clicked.connect(self.cleanfig)
        # self.plottdfig()


    def plotsdfig(self):
        self.index = None
        self.start_index = None
        self.stop_index = None
        self.salinity = []
        self.depth = []
        self.x_salinity = []
        self.y_depth = []
        if len(Function.time_) != 0:
            if self.spinBoxSD_start.value() <= len(fc.final_peaks) and \
                    self.spinBoxSD_stop.value() <= len(fc.final_peaks) and \
                    self.spinBoxSD_start.value() <=self.spinBoxSD_stop.value():
                for i in range(self.spinBoxSD_start.value(), self.spinBoxSD_stop.value()+1, 1):
                    self.index = i - 1
                    if self.comboBox_SDFig.currentIndex() == 0:
                        self.start_index = fc.all_p_t[self.index * 2][0]
                        self.stop_index = fc.all_p_t[self.index * 2 + 2][0]
                    elif self.comboBox_SDFig.currentIndex() == 1:
                        self.start_index = fc.all_p_t[self.index * 2 + 1][0]
                        self.stop_index = fc.all_p_t[self.index * 2 + 2][0]
                    elif self.comboBox_SDFig.currentIndex() == 2:
                        self.start_index = fc.all_p_t[self.index * 2][0]
                        self.stop_index = fc.all_p_t[self.index * 2 + 1][0]

                    self.salinity = fc.salinity[self.start_index:self.stop_index]
                    self.depth = fc.depth[self.start_index:self.stop_index]
                    self.y_depth = np.array(self.depth)
                    self.y_depth = self.y_depth.astype(np.float).tolist()
                    self.x_salinity = np.array(self.salinity)
                    self.x_salinity = self.x_salinity.astype(np.float).tolist()

                    # self.tdfigure.invert_yaxis()
                    # self.tdfigure.cla()
                    self.sdfigure.plot(self.x_salinity, self.y_depth)
                    # self.tdfigure.set_xlabel('Temperature(℃)')
                    # self.tdfigure.set_ylabel('Depth(m)')
                    # self.sdfigure.set_xticks(np.linspace(32, 33, 5))
                    self.canvas.draw()
            else:
                QMessageBox.information(None, "提示！", "超出最大剖面数！")
        else:
            QMessageBox.information(None, "提示！", "请先导入数据！")


    def cleanfig(self):
        self.gridLayout_SDFig.removeWidget(self.canvas)
        self.canvas.deleteLater()
        self.gridLayout_SDFig.removeWidget(self.picture_h_tb)
        self.picture_h_tb.deleteLater()
        self.fig = plt.Figure()
        self.canvas = FC(self.fig)
        self.sdfigure = self.fig.add_subplot(111)
        self.sdfigure.set_xlabel('Salinity')
        self.sdfigure.set_ylabel('Depth(m)')
        self.sdfigure.set_title('Salinity-Depth')
        self.sdfigure.invert_yaxis()
        self.gridLayout_SDFig.addWidget(self.canvas)
        self.picture_h_tb = NavigationToolbar(self.canvas, self.widget)
        self.gridLayout_SDFig.addWidget(self.picture_h_tb)


class TProFigWidget(QWidget,Ui_Form_TProFig):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.fig = plt.Figure()
        self.canvas = FC(self.fig)
        self.TProfigure = self.fig.add_subplot(111)
        self.TProfigure.set_xlabel('Time(hour)')
        self.TProfigure.set_ylabel('Depth(m)')
        self.TProfigure.set_title('Temperature-Depth')
        self.TProfigure.invert_yaxis()
        self.picture_h_tb = NavigationToolbar(self.canvas, self.widget_TPro)
        self.gridLayout_TPro.addWidget(self.canvas)
        self.gridLayout_TPro.addWidget(self.picture_h_tb)

        self.pushButton_TPro.clicked.connect(self.plot_click)
        self.pushButton_clear.clicked.connect(self.cleanfig)

    def plot_click(self):
        self.thread_plot = threading.Thread(target=self.plottprofig)
        self.thread_plot.start()
        print(self.thread_plot.isAlive())

    def plottprofig(self):
        if len(Function.time_) != 0:
            x = range(len(fc.depth))
            depth_array = np.array(fc.depth)
            depth_array = depth_array.astype(np.float).tolist()
            temperature_array = np.array(fc.temperature)
            temperature_array = temperature_array.astype(np.float).tolist()

            cmp = plt.get_cmap('jet')
            norm = plt.Normalize(vmin=np.min(temperature_array), vmax=np.max(temperature_array), clip=True)
            self.TProax = self.TProfigure.scatter(fc.time_, depth_array, c=temperature_array, cmap=cmp, norm=norm,
                                                  s=0.1)
            # self.TProfigure.invert_yaxis()
            # ticks = [list(zip(range(0, len(fc.time_),280000), fc.time_))]
            self.TProfigure.set_xticks([fc.time_[fc.final_troughs[0][0]], fc.time_[fc.final_troughs[-1][0]]])
            self.fig.colorbar(self.TProax, ax=self.TProfigure)

            self.canvas.draw()
            pass

    def cleanfig(self):
        self.gridLayout_TPro.removeWidget(self.canvas)
        self.canvas.deleteLater()
        self.gridLayout_TPro.removeWidget(self.picture_h_tb)
        self.picture_h_tb.deleteLater()
        self.fig = plt.Figure()
        self.canvas = FC(self.fig)
        self.TProfigure = self.fig.add_subplot(111)
        self.TProfigure.set_xlabel('Time(hour)')
        self.TProfigure.set_ylabel('Depth(m)')
        self.TProfigure.set_title('Temperature-Depth')
        self.TProfigure.invert_yaxis()
        self.picture_h_tb = NavigationToolbar(self.canvas, self.widget_TPro)
        self.gridLayout_TPro.addWidget(self.canvas)
        self.gridLayout_TPro.addWidget(self.picture_h_tb)




class SProFigWidget(QWidget,Ui_Form_SProFig):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.fig = plt.Figure()
        self.canvas = FC(self.fig)
        self.SProfigure = self.fig.add_subplot(111)
        self.SProfigure.set_xlabel('Time(hour)')
        self.SProfigure.set_ylabel('Depth(m)')
        self.SProfigure.set_title('Salinity-Depth')
        self.SProfigure.invert_yaxis()
        self.picture_h_tb = NavigationToolbar(self.canvas, self.widget_SPro)
        self.gridLayout_SPro.addWidget(self.canvas)
        self.gridLayout_SPro.addWidget(self.picture_h_tb)

        self.pushButton_SPro.clicked.connect(self.plot_click)
        self.pushButton_clear.clicked.connect(self.cleanfig)



    def plot_click(self):
        self.thread_plot = threading.Thread(target=self.plotsprofig)
        self.thread_plot.start()

    def plotsprofig(self):
        if len(Function.time_) != 0:
            x = range(len(fc.depth))
            depth_array = np.array(fc.depth)
            depth_array = depth_array.astype(np.float).tolist()
            salinity_array = np.array(fc.salinity)
            salinity_array = salinity_array.astype(np.float).tolist()
            cmp = plt.get_cmap('jet')
            norm = plt.Normalize(vmin=np.min(salinity_array), vmax=np.max(salinity_array), clip=True)
            self.SProax = self.SProfigure.scatter(fc.time_, depth_array, c=salinity_array, cmap=cmp, norm=norm, s=0.2)
            # self.TProfigure.invert_yaxis()
            # ticks = [list(zip(range(0, len(fc.time_),280000), fc.time_))]
            self.SProfigure.set_xticks([fc.time_[fc.final_troughs[0][0]],fc.time_[fc.final_troughs[-1][0]]])
            self.fig.colorbar(self.SProax, ax=self.SProfigure)

            self.canvas.draw()
            pass

    def cleanfig(self):
        self.gridLayout_SPro.removeWidget(self.canvas)
        self.canvas.deleteLater()
        self.gridLayout_SPro.removeWidget(self.picture_h_tb)
        self.picture_h_tb.deleteLater()
        self.fig = plt.Figure()
        self.canvas = FC(self.fig)
        self.SProfigure = self.fig.add_subplot(111)
        self.SProfigure.set_xlabel('Time(hour)')
        self.SProfigure.set_ylabel('Depth(m)')
        self.SProfigure.set_title('Salinity-Depth')
        self.SProfigure.invert_yaxis()
        self.picture_h_tb = NavigationToolbar(self.canvas, self.widget_SPro)
        self.gridLayout_SPro.addWidget(self.canvas)
        self.gridLayout_SPro.addWidget(self.picture_h_tb)
