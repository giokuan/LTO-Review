# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'english.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow1(object):

    def btn1(self):
        self.pushButton1.setStyleSheet("background-color: rgb(255, 0, 0);")

    def btn2(self):
        self.pushButton_2.setStyleSheet("background-color: rgb(85, 170, 255);")



    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.resize(654, 445)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("license.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow1.setWindowIcon(icon)
        MainWindow1.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow1)
        self.centralwidget.setObjectName("centralwidget")
        
        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.setGeometry(QtCore.QRect(20, 160, 601, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton1.setFont(font)
        self.pushButton1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton1.setDefault(False)
        self.pushButton1.setFlat(False)
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton1.clicked.connect(self.btn1)
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 220, 601, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.btn2)
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 280, 601, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.pushButton_3.setObjectName("pushButton_3")
        
        self.next_btn = QtWidgets.QPushButton(self.centralwidget)
        self.next_btn.setGeometry(QtCore.QRect(514, 340, 101, 81))
        self.next_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.next_btn.setIcon(icon1)
        self.next_btn.setIconSize(QtCore.QSize(76, 76))
        self.next_btn.setObjectName("next_btn")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 641, 71))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
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


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow1)
    MainWindow1.show()
    sys.exit(app.exec_())
