from PyQt5 import QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog,QApplication
import sys



# class Ui_MainWindow(QMainWindow):
#     def __init__(self):
#         super(Ui_MainWindow,self).__init__()
#         # self.ui = Ui_MainWindow()
#         # self.ui.setupUi(self)
#         loadUi(r"C:\Users\MAHA RAJA\Desktop\Qt design\first.ui",self)
#         self.pushButton.clicked.connect(self.Next)
#     # def dialogbox(self):
#     #     self.hide()
#     #     self.myDialog = Ui_Dialog()
#     #     self.myDialog.show()
#     def Next(self):
#         widget.setCurrentIndex(widget.currentIndex()+1)

   
        
# class Ui_Screen2(Screen2):
#     def __init__(self):
#         super(Ui_Screen2,self).__init__()
#         # self.ui = Ui_Dialog()
#         # self.ui.setupUi(self)
#         loadUi(r"C:\Users\MAHA RAJA\Desktop\Qt design\second page.ui",self)


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

# # app = QtWidgets.QApplication(sys.argv)
# # widget=QtWidgets.QStackedWidget()
# # MainWindow=Ui_MainWindow()
# # screen=Ui_Screen2()
# # widget.addWidget(MainWindow)
# # widget.addWidget(Screen)
# # widget.setFixedHeight(300)
# # widget.setFixedHeight(400)
# # widget.show()
# # MainWindow.show()
# # sys.exit(app.exec_())


class firstdialog(QDialog):
    def __init__(self):
        super(firstdialog,self).__init__()
        loadUi(r"C:\Users\MAHA RAJA\Desktop\Qt design\firstDialog.ui",self)
        self.nextbutton.clicked.connect(self.nextpage)
        

    def nextpage(self):
        serialnumber=self.serialnumber.text()
        nextpage=secondDialog()
        widget.addWidget(nextpage)
        widget.setCurrentIndex(widget.currentIndex()+1)

        print("success",serialnumber)

class secondDialog(QDialog):
    def __init__(self):
        super(secondDialog,self).__init__()
        loadUi(r"C:\Users\MAHA RAJA\Desktop\Qt design\secondDialog.ui",self)
        self.backbutton.clicked.connect(self.backfunction)
    def backfunction(self):
        # print("success second")
        backpage=firstdialog()
        widget.addWidget(backpage)
        widget.setCurrentIndex(widget.currentIndex()+1)
        print("firstpage")







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


