#!/usr/bin/env python3
import sys
import time
from PyQt5.QtCore import QObject, QUrl, Qt, pyqtProperty, pyqtSignal, QTimer,QDateTime
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QApplication, QListWidget, QGridLayout, QLabel
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType, QQmlEngine, QQmlComponent
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtQuick import QQuickView
from PyQt5.QtGui import QFont, QFontDatabase
import pyqtgraph as pg
import numpy as np

import plotly.graph_objects as go




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 768)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        #Grafik1
        self.labelx = QtWidgets.QLabel(self.centralwidget)
        self.labelx.setGeometry(QtCore.QRect(5, 460, 500, 300))
        self.labelx.setAutoFillBackground(True)
        self.labelx.setFrameShape(QtWidgets.QFrame.Panel)
        self.labelx.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.labelx.setLineWidth(3)
        self.labelx.setMidLineWidth(3)
        self.labelx.setText("")
        self.labelx.setScaledContents(True)
        self.labelx.setObjectName("labelx")
        
        #Grafik2
        self.grafik2 = QtWidgets.QLabel(self.centralwidget)
        self.grafik2.setGeometry(QtCore.QRect(510, 460, 500, 300))
        self.grafik2.setAutoFillBackground(True)
        self.grafik2.setFrameShape(QtWidgets.QFrame.Panel)
        self.grafik2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.grafik2.setLineWidth(3)
        self.grafik2.setMidLineWidth(3)
        self.grafik2.setText("")
        self.grafik2.setScaledContents(True)
        self.grafik2.setObjectName("grafik2")
        
        '''
        #Analog1
        self.analog1 = QtWidgets.QLabel(self.centralwidget)
        self.analog1.setGeometry(QtCore.QRect(5, 330, 250, 250))
        self.analog1.setAutoFillBackground(True)
        self.analog1.setFrameShape(QtWidgets.QFrame.Panel)
        self.analog1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.analog1.setLineWidth(3)
        self.analog1.setMidLineWidth(3)
        self.analog1.setText("")
        self.analog1.setScaledContents(True)
        self.analog1.setObjectName("analog1")
        '''



        self.templabel = QtWidgets.QLabel(self.centralwidget)
        self.templabel.setGeometry(QtCore.QRect(25, 25, 300, 50))
        self.templabel.setObjectName("templabel")
        self.templabel.setStyleSheet("font: normal 30px; color: black; background-color: white; border: 1px solid black;")
        self.templabel.setAlignment(QtCore.Qt.AlignCenter)
        self.templabel.setText("TEMPERATURE (°C)")

        self.tempvalue = QtWidgets.QLabel(self.centralwidget)
        self.tempvalue.setGeometry(QtCore.QRect(25, 75, 300, 150))
        self.tempvalue.setObjectName("tempvalue")
        self.tempvalue.setStyleSheet("font: bold 120px; color: green; background-color: white; border: 1px solid black;")
        self.tempvalue.setAlignment(QtCore.Qt.AlignCenter)
        self.tempvalue.setText("-")

        

        self.humlabel = QtWidgets.QLabel(self.centralwidget)
        self.humlabel.setGeometry(QtCore.QRect(345, 25, 300, 50))
        self.humlabel.setObjectName("humlabel")
        self.humlabel.setStyleSheet("font: normal 30px; color: black; background-color: white; border: 1px solid black;")
        self.humlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.humlabel.setText("HUMIDITY (%Rh)")

        self.humvalue = QtWidgets.QLabel(self.centralwidget)
        self.humvalue.setGeometry(QtCore.QRect(345, 75, 300, 150))
        self.humvalue.setObjectName("humvalue")
        self.humvalue.setStyleSheet("font: bold 120px; color: green; background-color: white; border: 1px solid black;")
        self.humvalue.setAlignment(QtCore.Qt.AlignCenter)
        self.humvalue.setText("-")


        self.presslabel = QtWidgets.QLabel(self.centralwidget)
        self.presslabel.setGeometry(QtCore.QRect(665, 25, 300, 50))
        self.presslabel.setObjectName("presslabel")
        self.presslabel.setStyleSheet("font: normal 30px; color: black; background-color: white; border: 1px solid black;")
        self.presslabel.setAlignment(QtCore.Qt.AlignCenter)
        self.presslabel.setText("PRESSURE (Atm)")

        self.pressvalue = QtWidgets.QLabel(self.centralwidget)
        self.pressvalue.setGeometry(QtCore.QRect(665, 75, 300, 150))
        self.pressvalue.setObjectName("pressvalue")
        self.pressvalue.setStyleSheet("font: bold 120px; color: green; background-color: white; border: 1px solid black;")
        self.pressvalue.setAlignment(QtCore.Qt.AlignCenter)
        self.pressvalue.setText("-")



        self.rel1label = QtWidgets.QLabel(self.centralwidget)
        self.rel1label.setGeometry(QtCore.QRect(25, 250, 300, 50))
        self.rel1label.setObjectName("rel1label")
        self.rel1label.setStyleSheet("font: normal 30px; color: black; background-color: white; border: 1px solid black;")
        self.rel1label.setAlignment(QtCore.Qt.AlignCenter)
        self.rel1label.setText("RELAY 1 POSITION")

        self.rel1value = QtWidgets.QLabel(self.centralwidget)
        self.rel1value.setGeometry(QtCore.QRect(25, 300, 300, 150))
        self.rel1value.setObjectName("rel1value")
        self.rel1value.setStyleSheet("font: bold 120px; color: green; background-color: white; border: 1px solid black;")
        self.rel1value.setAlignment(QtCore.Qt.AlignCenter)
        self.rel1value.setText("")


        self.noiselabel = QtWidgets.QLabel(self.centralwidget)
        self.noiselabel.setGeometry(QtCore.QRect(345, 250, 300, 50))
        self.noiselabel.setObjectName("noiselabel")
        self.noiselabel.setStyleSheet("font: normal 30px; color: black; background-color: white; border: 1px solid black;")
        self.noiselabel.setAlignment(QtCore.Qt.AlignCenter)
        self.noiselabel.setText("NOISE (dB)")

        self.noisevalue = QtWidgets.QLabel(self.centralwidget)
        self.noisevalue.setGeometry(QtCore.QRect(345, 300, 300, 150))
        self.noisevalue.setObjectName("noisevalue")
        self.noisevalue.setStyleSheet("font: bold 120px; color: green; background-color: white; border: 1px solid black;")
        self.noisevalue.setAlignment(QtCore.Qt.AlignCenter)
        self.noisevalue.setText("-")



        self.rel2abel = QtWidgets.QLabel(self.centralwidget)
        self.rel2abel.setGeometry(QtCore.QRect(665, 250, 300, 50))
        self.rel2abel.setObjectName("rel2abel")
        self.rel2abel.setStyleSheet("font: normal 30px; color: black; background-color: white; border: 1px solid black;")
        self.rel2abel.setAlignment(QtCore.Qt.AlignCenter)
        self.rel2abel.setText("RELAY 2 POSITION")

        self.rel2value = QtWidgets.QLabel(self.centralwidget)
        self.rel2value.setGeometry(QtCore.QRect(665, 300, 300, 150))
        self.rel2value.setObjectName("rel2value")
        self.rel2value.setStyleSheet("font: bold 120px; color: green; background-color: white; border: 1px solid black;")
        self.rel2value.setAlignment(QtCore.Qt.AlignCenter)
        self.rel2value.setText("")






        #Zaman   
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(0, 0, 200, 20))
        self.label_15.setObjectName("Zaman")
        

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 668, 21))
        self.menubar.setObjectName("menubar")
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)


        '''
        view = QQuickView()
        view.setSource(QUrl('gauge.qml'))
        gauge=view.findChild(QObject,'test_gauge')
        gauge.setProperty('gauge_value',500)
        view.show()
        '''        

        self.retranslateUi(MainWindow)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("DashBoard", "DashBoard"))

        #self.label_15.setText(_translate("MainWindow", "Total Expenses"))
        #self.label_16.setText(_translate("MainWindow", "Total Income"))

        


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.label_15.setText("Zaman")

        self.timer=QTimer()
        self.timer.timeout.connect(self.showTime)
        self.timer.start(2000)

        #Grafik1
        lay = QtWidgets.QVBoxLayout(self.labelx)
        lay.setContentsMargins(0, 0, 0, 0)
        self.plt = pg.plot()
        lay.addWidget(self.plt)

        #Grafik2
        lay = QtWidgets.QVBoxLayout(self.grafik2)
        lay.setContentsMargins(0, 0, 0, 0)
        self.plt2 = pg.plot()
        lay.addWidget(self.plt2)

        '''
        #Analog1
        lay = QtWidgets.QVBoxLayout(self.analog1)
        lay.setContentsMargins(0, 0, 0, 0)
        #self.analogview1 = self.view()
        lay.addWidget(self.view.show())
        '''
        '''
        self.view = QQuickView()
        self.view.setSource(QUrl('gauge.qml'))
        self.gauge=self.view.findChild(QObject,'test_gauge')
        self.gauge.setProperty('gauge_value',4500)
        self.view.show()
        '''



    #def plot_sensor1(self):
        title = "Sensor1"
        t = 8
        self.y = np.random.randint(0, 100, 10)

        self.x = range(0, 10)

        self.plt.showGrid(x=True, y=True)

        # adding legend
        self.plt.addLegend()

        # set properties of the label for y axis
        self.plt.setLabel("left", "Sensor1-Sicaklik", units="°C")

        # set properties of the label for x axis
        self.plt.setLabel("bottom", "Zaman", units="Saniye")

        # setting horizontal range
        self.plt.setXRange(0, 10)

        # setting vertical range
        self.plt.setYRange(0, 100)

        # setting window title
        self.plt.setWindowTitle(title)

        # ploting line in green color
        #line1 = self.plt.plot(x, y, pen="g", symbol="x", symbolPen="g", symbolBrush=0.2, name="Sicaklik")
        self.line1 = self.plt.plot(self.x, self.y, pen="g", symbol="x", symbolPen="g", symbolBrush=0.2)
    


    #def plot_sensor1(self):
        title2 = "Sensor2"
        t2 = 8
        self.y2 = np.random.randint(0, 100, 10)

        self.x2 = range(0, 10)

        self.plt2.showGrid(x=True, y=True)

        # adding legend
        self.plt2.addLegend()

        # set properties of the label for y axis
        self.plt2.setLabel("left", "Sensor2-Nem", units="°RH")

        # set properties of the label for x axis
        self.plt2.setLabel("bottom", "Zaman", units="Dakika")

        # setting horizontal range
        self.plt2.setXRange(0, 10)

        # setting vertical range
        self.plt2.setYRange(0, 100)

        # setting window title
        self.plt2.setWindowTitle(title)

        # ploting line in green color
        #line1 = self.plt.plot(x, y, pen="g", symbol="x", symbolPen="g", symbolBrush=0.2, name="Sicaklik")
        self.line2 = self.plt2.plot(self.x2, self.y2, pen="g", symbol="x", symbolPen="g", symbolBrush=0.2)




    def showTime(self):
        current_time=QDateTime.currentDateTime()
        formatted_time=current_time.toString('dd-MM-yyyy hh:mm:ss dddd')
        self.label_15.setText(formatted_time)

        self.y = np.delete(self.y,0)
        self.y = np.append(self.y,np.random.randint(0, 100))
        #print(self.y)
        self.line1.clear()
        self.line1 = self.plt.plot(self.x, self.y, pen="g", symbol="x", symbolPen="g", symbolBrush=0.2)

        self.y2 = np.delete(self.y2,0)
        self.y2 = np.append(self.y2,np.random.randint(0, 100))
        #print(self.y)
        self.line2.clear()
        self.line2 = self.plt2.plot(self.x2, self.y2, pen="g", symbol="x", symbolPen="g", symbolBrush=0.2)

        self.tempvalue.setText(str(np.random.randint(0, 200)))

        self.humvalue.setText(str(np.random.randint(0, 100)))

        self.pressvalue.setText(str(np.random.randint(0, 90)))

        self.noisevalue.setText(str(np.random.randint(0, 10)))

        if (np.random.randint(0, 10)) > 5:
            self.rel1value.setStyleSheet("font: bold 120px; color: green; background-color: green; border: 1px solid black;")
        else:
            self.rel1value.setStyleSheet("font: bold 120px; color: green; background-color: red; border: 1px solid black;")

        if (np.random.randint(0, 10)) > 5:
            self.rel2value.setStyleSheet("font: bold 120px; color: green; background-color: green; border: 1px solid black;")
        else:
            self.rel2value.setStyleSheet("font: bold 120px; color: green; background-color: red; border: 1px solid black;")


        '''
        self.gauge.setProperty('gauge_value',np.random.randint(0, 10000))
        self.view.show()
        '''




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()

    '''
    view = QQuickView()
    view.setSource(QUrl('gauge.qml'))
    gauge=view.findChild(QObject,'test_gauge')
    gauge.setProperty('gauge_value',500)
    view.show()
    '''


    sys.exit(app.exec_())