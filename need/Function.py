from cmath import sqrt

import numpy as np
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import os
import datetime
from itertools import islice
from UIdesign.data import Ui_Form_data


time_ = []
depth = []
temperature = []
salinity = []
all_p_t = []
max_depth = None
min_depth = None
start_time = None
end_time = None
final_peaks = []
final_troughs = []
depth_profile = []

class function(QWidget,Ui_Form_data):
    print(depth)

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        pass
    def loaddata(self,filename = None):
        time_.clear()
        depth.clear()
        temperature.clear()
        salinity.clear()
        final_peaks.clear()
        final_troughs.clear()
        if filename == False or filename == None:
            filename, _ = QFileDialog.getOpenFileName(self, '导入数据', os.getcwd(), "All Files (*);;Text Files (*.txt)")
            pass
            global dataname
            dataname = os.path.basename(filename)
            dataname = dataname.split('.')[0]
            if filename != '':
                input_file = open(filename, 'r')
                File_rfind = filename.rfind('.')
                global f
                f= filename[File_rfind + 1:]
                if f != 'txt':
                    QMessageBox.warning(None,'提示','请导入txt文件！')
                else:
                    for line in islice(input_file, 1, None):  # 去除txt文件的第一行
                        temp = line.split(',')

                        if (len(temp) != 10):
                            QMessageBox.critical(None, "message", "数据格式错误！")
                            break

                        time_.append(temp[0])
                        temperature.append(temp[2])
                        depth.append(temp[5])
                        salinity.append(temp[6])

                    if (len(time_) == len(depth) and len(time_) != 0 and len(time_[0])==23):
                        function.split_profile(self)

                        array_depth = np.array(depth).astype(np.float).tolist()
                        max_depth = max(array_depth)
                        min_depth = min(array_depth)



                        start_time = time_[final_troughs[0][0]]
                        stop_time = time_[final_troughs[-1][0]]
                        global real_startdate,real_stopdate
                        real_startdate = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S.%f")
                        real_stopdate = datetime.datetime.strptime(stop_time, "%Y-%m-%d %H:%M:%S.%f")

                        self.dateTimeEdit_datastart.setDateTime(real_startdate)
                        self.dateTimeEdit_dataend.setDateTime(real_stopdate)
                        self.dateTimeEdit_datastart.setMinimumDateTime(real_startdate)
                        self.dateTimeEdit_datastart.setMaximumDateTime(real_stopdate)
                        self.dateTimeEdit_dataend.setMinimumDateTime(real_startdate)
                        self.dateTimeEdit_dataend.setMaximumDateTime(real_stopdate)

                        profile_num = str(len(final_peaks))
                        items = [dataname,profile_num,start_time,stop_time,min_depth,max_depth]
                        for i in range(len(items)):
                            item = QTableWidgetItem(items[i])
                            item.setTextAlignment(Qt.AlignCenter)
                            self.tableWidget_datainfo.setItem(0,i,QTableWidgetItem(item))

                        QMessageBox.information(None, "提示！", "数据导入成功")
                        return 1

                    else:
                        QMessageBox.warning(None,'提示！','数据格式错误！')

        # def fileQuit(self):
        #     self.close()

    def find_peaks_troughs(self,depth, rangesize):
        '''
        给定一个数组depth, 从左往右扫描。
        用S记录当前的状态（未知0， 下潜1，上浮2)
        当S=0, 如果 depth[i] > depth[i+1]  修改状态为 下潜1， 否则为上浮 2
        当S=1, 如果 depth[i] < depth[i+1], 则判断为由下潜变为上浮， 此处为一个波谷（开始上浮）。
        如果该波谷比上一个rangesize范围内的波谷更低，则修改上一个波谷的值。 否则就将该波谷加入波谷列表。
        当S=2, 如果 depth[i] > depth[i+1], 则判断为由上浮变为下潜， 此处为一个波峰（开始下潜）。
        如果该波峰比上一个rangesize范围内的波峰更高，则修改上一个波谷的值。 否则就将该波峰加入波峰列表。

        :param depth:深度数据
        :param rangesize:判断的距离
        :return:波峰波谷列表，列表第三个元素status 波峰：2，波谷：1 [index,depth,status]
        '''
        peaks = list()
        troughs = list()
        S = 0
        for i in range(1, len(depth) - 1):
            if S == 0:
                if depth[i] > depth[i + 1]:
                    S = 1
                    pass
                else:
                    S = 2
                    pass
                pass
            elif S == 1:
                if depth[i] < depth[i + 1]:
                    S = 2  # 由下潜变为上浮
                    if len(troughs):
                        (prev_i, prev_trough, prev_status) = troughs[-1]
                        if i - prev_i < rangesize:
                            if prev_trough > depth[i]:
                                troughs[-1] = (i, depth[i], 1)
                                pass
                        else:
                            troughs.append((i, depth[i], 1))
                    else:
                        troughs.append((i, depth[i], 1))

            elif S == 2:
                if depth[i] > depth[i + 1]:
                    S = 1  # 由上浮变为下潜
                    if len(peaks):
                        prev_i, prev_peak, prev_status = peaks[-1]
                        if i - prev_i < rangesize:
                            if prev_peak < depth[i]:
                                peaks[-1] = (i, depth[i], 2)
                        else:
                            peaks.append((i, depth[i], 2))

                    else:
                        peaks.append((i, depth[i], 2))

        return peaks, troughs

    def split_profile(self):
        # depth = function.depth
        # time = function.time
        # depth_array = np.array(depth)
        # depth_array = depth_array.astype(np.float).tolist()

        true_peaks = []
        true_troughs = []
        p_t_error = []
        true_peaks.clear()
        true_troughs.clear()
        p_t_error.clear()
        peaks, troughs = function.find_peaks_troughs(self, depth[0:-1], 1000)
        max_depth = float(max(depth))
        '''第一次筛选'''
        for i in range(len(peaks)):
            if float(peaks[i][1]) >= max_depth/2:
                true_peaks.append(peaks[i])

        for j in range(len(troughs)):
            if float(troughs[j][1]) >= 0.05 and float(troughs[j][1]) < max_depth/2:
                true_troughs.append(troughs[j])
        # true_peaks.pop(0)

        '''使开头为波谷'''
        if true_peaks[0][0] < true_troughs[0][0]:
            true_peaks.pop(0)
        '''使结尾为波谷'''
        if true_peaks[-1][0] > true_troughs[-1][0]:
            true_peaks.pop(-1)

        '''将波峰波谷的数列合并并排序，以便后续筛选'''
        global all_p_t
        all_p_t = true_peaks + true_troughs
        all_p_t.sort()

        '''第二次筛选，判断合成的数列中，波峰和波谷是否一一对应，‘+*+*+*’not‘+*++*+’'''
        for k in range(len(all_p_t)):
            if k >= 1:
                if (all_p_t[k][2]) == (all_p_t[k - 1][2]):
                    p_t_error.append(k)
            else:
                continue

        '''同时删除筛选出来的多余数据'''
        all_p_t = [all_p_t[i] for i in range(0, len(all_p_t), 1) if i not in p_t_error]


        '''将合成的数列再次分开'''
        for index in range(len(all_p_t)):
            if float(all_p_t[index][1]) >= 5:
                final_peaks.append(all_p_t[index])
            else:
                final_troughs.append(all_p_t[index])

    def generatetxt(self,full_path = None):

        if final_peaks == []:
            QMessageBox.warning(None, "提示！", "请先导入数据！")
        else:
            if full_path == False or full_path == None:
                full_path = QFileDialog.getSaveFileName(self, "保存文件", "C:\\Users\\Administrator\\Desktop",
                                                "txt files (*.txt);;all files(*.*)")
                if full_path != ('', ''):
                    f = open(full_path[0], 'a')
                    for index in range(len(final_peaks)):
                        f.write(
                            str(index) + ':' + time_[final_troughs[index][0]] + ':开始下潜，深度为:' + depth[
                                final_troughs[index][0]] + '\n')
                        f.write(str(index) + ':' + time_[final_peaks[index][0]] + ':达到此次最大下潜深度，开始上浮，深度为：' + depth[
                            final_peaks[index][0]] + '\n')

                    f.write(time_[final_troughs[-1][0]] + ':结束运动，此时深度为：' + depth[final_troughs[-1][0]])
                    f.close()
                    QMessageBox.information(None, '提示', '生成成功！')
                    return 1






    # def open_file(self):



    def calculate_rangesize(self,m,t,D,p,g,V,T):
        '''
        :param m: 浮标质量，单位kg
        :param t: 采样间隔，单位s
        :param D: 上浮距离，单位m
        :param p: 海水密度
        :param g: 当地重力加速度
        :param V: 浮标排水体积，单位m³
        :param T: 上浮时间，单位s
        :return: rangesize，筛选步长，步长越小，筛选出的数据越多
        '''
        T = sqrt(2*m*D/(p*g*V-m*g))
        rangesize = T/t
        return rangesize