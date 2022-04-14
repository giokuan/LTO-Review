from PyQt5 import QtCore, QtGui, QtWidgets
from q2 import Ui_MainWindow2
import sys

  
class Score:
    scr = 0
    

class Ui_MainWindow1(object):


    def open_window(self):
        self.window =QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow2()
        self.ui.setupUi(self.window)
    
        # MainWindow1.hide()
        self.window.show()

        

    def psh_btn2(self):
      
        s = Score.scr+1
        x = self.lineEdit_score.setText(str(s))
           

    def next(self):
        
        x = self.lineEdit_score.text()
        self.ui.lineEdit_q2.setText(x)



    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.resize(653, 483)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("license.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow1.setWindowIcon(icon)
        MainWindow1.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow1)
        self.centralwidget.setObjectName("centralwidget")
        
        

        
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
        #self.pushButton1.clicked.connect(lambda:print("Score is ", Score.scr))
        
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 220, 601, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(lambda:self.label_check.show())
        self.pushButton_2.clicked.connect(lambda:self.pushButton1.setEnabled(False))
        self.pushButton_2.clicked.connect(lambda:self.pushButton_3.setEnabled(False))
        #self.pushButton_2.clicked.connect(lambda:print("Score is ", Score.scr+1))
        self.pushButton_2.clicked.connect(self.psh_btn2)


        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 300, 601, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(lambda:self.label_error2.show())
        self.pushButton_3.clicked.connect(lambda:self.pushButton1.setEnabled(False))
        self.pushButton_3.clicked.connect(lambda:self.pushButton_2.setEnabled(False))
        #score +=1

        self.lineEdit_score = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_score.setGeometry(QtCore.QRect(30, 79, 81, 21))
        self.lineEdit_score.setObjectName("lineEdit_score")
        self.lineEdit_score.setText(str(Score.scr))

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 641, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.label_check = QtWidgets.QLabel(self.centralwidget)
        self.label_check.setGeometry(QtCore.QRect(570, 230, 41, 41))
        self.label_check.setText("")
        self.label_check.setPixmap(QtGui.QPixmap("icon/check.png"))
        self.label_check.setScaledContents(True)
        self.label_check.setObjectName("label_check")
        self.label_check.hide()
        
        self.label_error2 = QtWidgets.QLabel(self.centralwidget)
        self.label_error2.setGeometry(QtCore.QRect(570, 310, 41, 41))
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
        self.next_btn.clicked.connect(self.open_window)
        self.next_btn.clicked.connect(self.next)


       
        
        self.label_next = QtWidgets.QLabel(self.centralwidget)
        self.label_next.setGeometry(QtCore.QRect(540, 380, 61, 61))
        self.label_next.setText("")
        self.label_next.setPixmap(QtGui.QPixmap("icon/next.png"))
        self.label_next.setScaledContents(True)
        self.label_next.setObjectName("label_next")
        
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(20, 430, 75, 23))
        self.exit_btn.setObjectName("exit_btn")
        

        MainWindow1.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow1)
        self.statusbar.setObjectName("statusbar")
        MainWindow1.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow1", "LTO EXAM REVIEW"))
        self.pushButton1.setText(_translate("MainWindow1", "THE ROAD IS TWO-WAY"))
        self.pushButton_2.setText(_translate("MainWindow1", "THE ROAD HAS TWO OR MORE LANES GOING IN ONE DIRECTION"))
        self.pushButton_3.setText(_translate("MainWindow1", "THE SIDEWALK IS WIDE"))
        self.label.setText(_translate("MainWindow1", "YOU CAN OVERTAKE IN THE RIGHT SIDE OF YOUR VEHICLE IF:"))
        self.exit_btn.setText(_translate("MainWindow1", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow1)
    MainWindow1.show()
    sys.exit(app.exec_())
