from PyQt5 import QtCore, QtGui, QtWidgets
# from q2 import Ui_MainWindow2



class Ui_MainWindow3(object):

    

    def psh_check(self):
       
        x = int(self.lineEdit_q3.text())
        sd = x+1
        self.lineEdit_q3.setText(str(sd))
        print(x)

   

   
    def setupUi(self, MainWindow3):
        MainWindow3.setObjectName("MainWindow3")
        MainWindow3.resize(653, 483)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("license.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow3.setWindowIcon(icon)
        MainWindow3.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow3)
        self.centralwidget.setObjectName("centralwidget")
        
        
        self.lineEdit_q3= QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_q3.setGeometry(QtCore.QRect(30, 79, 81, 21))
        self.lineEdit_q3.setObjectName("lineEdit_q3")

        
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(20, 150, 601, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton1.setFont(font)
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton1.clicked.connect(lambda:self.label_error.show())
        self.pushButton1.clicked.connect(lambda:self.pushButton_2.setEnabled(False))
        self.pushButton1.clicked.connect(lambda:self.pushButton_3.setEnabled(False))
        
       
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 220, 601, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda:self.label_error2.show())
        # score +=1
        # print("you got " + str(score) + " correct")
        self.pushButton_2.clicked.connect(lambda:self.pushButton1.setEnabled(False))
        self.pushButton_2.clicked.connect(lambda:self.pushButton_3.setEnabled(False))
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 300, 601, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda:self.label_check.show())
        self.pushButton_3.clicked.connect(lambda:self.pushButton1.setEnabled(False))
        self.pushButton_3.clicked.connect(lambda:self.pushButton_2.setEnabled(False))
        self.pushButton_3.clicked.connect(self.psh_check)
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 641, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.label_check = QtWidgets.QLabel(self.centralwidget)
        self.label_check.setGeometry(QtCore.QRect(570, 310, 41, 41))
        self.label_check.setText("")
        self.label_check.setPixmap(QtGui.QPixmap("icon/check.png"))
        self.label_check.setScaledContents(True)
        self.label_check.setObjectName("label_check")
        self.label_check.hide()
        
        self.label_error2 = QtWidgets.QLabel(self.centralwidget)
        self.label_error2.setGeometry(QtCore.QRect(570, 230, 41, 41))
        self.label_error2.setText("")
        self.label_error2.setPixmap(QtGui.QPixmap("icon/error.png"))
        self.label_error2.setScaledContents(True)
        self.label_error2.setObjectName("label_error2")
        self.label_error2.hide()
        
        self.label_error = QtWidgets.QLabel(self.centralwidget)
        self.label_error.setGeometry(QtCore.QRect(570, 160, 41, 41))
        self.label_error.setText("")
        self.label_error.setPixmap(QtGui.QPixmap("icon/error.png"))
        self.label_error.setScaledContents(True)
        self.label_error.setObjectName("label_error")
        self.label_error.hide()


        self.next_btn = QtWidgets.QPushButton(self.centralwidget)
        self.next_btn.setGeometry(QtCore.QRect(520, 370, 101, 81))
        self.next_btn.setText("")
        self.next_btn.setObjectName("next_btn")
        #self.next_btn.clicked.connect(self.psh_check)

        
        self.label_next = QtWidgets.QLabel(self.centralwidget)
        self.label_next.setGeometry(QtCore.QRect(540, 380, 61, 61))
        self.label_next.setText("")
        self.label_next.setPixmap(QtGui.QPixmap("icon/next.png"))
        self.label_next.setScaledContents(True)
        self.label_next.setObjectName("label_next")
        
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(20, 430, 75, 23))
        self.exit_btn.setObjectName("exit_btn")
        

        MainWindow3.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow3)
        self.statusbar.setObjectName("statusbar")
        MainWindow3.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow3)

    def retranslateUi(self, MainWindow3):
        _translate = QtCore.QCoreApplication.translate
        MainWindow3.setWindowTitle(_translate("MainWindow3", "LTO EXAM REVIEW"))
        self.pushButton1.setText(_translate("MainWindow3", "SUSPENSION OF LISCENSE"))
        self.pushButton_2.setText(_translate("MainWindow3", "FINES AND IMPRISONMENT"))
        self.pushButton_3.setText(_translate("MainWindow3", "ALL ANSWERS ARE CORRECT"))
        self.label.setText(_translate("MainWindow3", "A person who drives while under influence of alcohol or \ndrugs is punishable by law with:"))
        self.exit_btn.setText(_translate("MainWindow3", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow3 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow3()
    ui.setupUi(MainWindow3)
    MainWindow3.show()
    sys.exit(app.exec_())