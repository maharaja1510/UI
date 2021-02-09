from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTime, QTimer,QBasicTimer
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import (QMessageBox,QWidget,QApplication,QProgressBar,QPushButton,QDialog)

#import RPi.GPIO as GPIO
import time
import serial
import sys

Time_limit=100




class firstdialog(QDialog):
    def __init__(self):
        super(firstdialog,self).__init__()
        loadUi(r"C:\Users\MAHA RAJA\Desktop\Qt design\firstDialog.ui",self)
        # if self.serialnumber== " ":
        #     self.nextbutton.clicked.connect(self.show)
        #     def show(self):
        #         msg=QMessageBox()
        #         msg.setWindowTitle("Serial Number")
        #         msg.setText("oops enter a serail number")
        #         x=msg.exec_()
        # else:
        self.nextbutton.clicked.connect(self.nextpage)
        

    def nextpage(self):
       
        serialnumber=self.serialnumber.text()
        if serialnumber!="":
            nextpage=secondDialog()
            widget.addWidget(nextpage)
            widget.setCurrentIndex(widget.currentIndex()+1)

            print("success",serialnumber)
        else:
            mbox=QMessageBox()
            mbox.setWindowTitle("Warning")
            mbox.setText("oops...  \nEnter a serial number")
            mbox.setIcon(QMessageBox.Warning)

            x=mbox.exec_()

class secondDialog(QDialog):
    def __init__(self):
        super(secondDialog,self).__init__()
        loadUi(r"C:\Users\MAHA RAJA\Desktop\Qt design\secondDialog.ui",self)
        self.backbutton.clicked.connect(self.backfunction)
        self.initUI()
        
    def backfunction(self):
        # print("success second")
        backpage=firstdialog()
        widget.addWidget(backpage)
        widget.setCurrentIndex(widget.currentIndex()+1)
        print("firstpage")
    
    def initUI(self):
        
        # self.progress = rs232progressBar(self)
        # self.rs232progressBar.setGeometry(0, 0, 300, 25)
        self. rs232progressBar.setMaximum(100)
        self.rs485progressBar.setMaximum(100)
        
        # self.button = runbutton(self)
        # self.runbutton.move(0, 30)
        self.show()
        self.labelcompletestatus232=self.rs232complelabel
        self.labelcompletestatus232.hide()
        self.labelcompletestatus485=self.rs485complelabel
        self.labelcompletestatus485.hide()


        self.runbutton.clicked.connect(self.onButtonClick)

    def onButtonClick(self):
        
        count = 0
        while count < Time_limit:
            count += 1
            time.sleep(.2)
            self.rs232progressBar.setValue(count)
        if count==100:
            self.rs232progressBar.hide()
            self.labelcompletestatus232.show()
            self.labelcompletestatus232.setStyleSheet("background-color: lightgreen") 
        else:
            self.labelcompletestatus232.setStyleSheet("background-color: red")
        
        if count==100:
            counts=0
            while counts < Time_limit:
                counts +=1
                time.sleep(.2)
                self.rs485progressBar.setValue(counts)
            if counts==100:
                self.rs485progressBar.hide()
                self.labelcompletestatus485.show()
                self.labelcompletestatus485.setStyleSheet("background-color: lightgreen") 
            else:
                self.labelcompletestatus485.setStyleSheet("background-color: red")
        


        maxvalue=self.maxedit.text()
        minvalue=self.minedit.text()
        loadvalue=1220
        resvalue=self.resultlabel
        if loadvalue > int(minvalue) and int(maxvalue)>loadvalue:
           resvalue.setStyleSheet("background-color: lightgreen") 
        else:
           resvalue.setStyleSheet("background-color: red")
           








app=QApplication(sys.argv)
mainwindow=firstdialog()
secondpage=secondDialog()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.addWidget(secondpage)
# widget.SetFixedWidth(800)
widget.setFixedWidth(800)
widget.setFixedHeight(480)
# widget.setFixedHeight(480)
widget.show()
app.exec_()
