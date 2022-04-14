from PyQt5 import QtCore, QtGui, QtWidgets
from english_ver import Ui_MainWindow1


class Ui_MainWindow(object):


    def open_english_ver(self):
        self.window =QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow1()
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.score_label = QtWidgets.QLabel(self.centralwidget)
        self.score_label.setGeometry(QtCore.QRect(180, 90, 161, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.score_label.setFont(font)
        self.score_label.setObjectName("score_label")
        
        self.score_lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.score_lineEdit.setGeometry(QtCore.QRect(260, 109, 113, 31))
        self.score_lineEdit.setObjectName("score_lineEdit")
       #self.score_lineEdit.setText(Score.scr)
        
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setGeometry(QtCore.QRect(140, 280, 171, 51))
        self.start_btn.setObjectName("start_btn")
        self.start_btn.clicked.connect(self.open_english_ver)
        
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(350, 280, 171, 51))
        self.exit_btn.setObjectName("exit_btn")
        
        self.title_label = QtWidgets.QLabel(self.centralwidget)
        self.title_label.setGeometry(QtCore.QRect(180, 30, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.title_label.setFont(font)
        self.title_label.setObjectName("title_label")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.score_label.setText(_translate("MainWindow", "SCORE:"))
        self.start_btn.setText(_translate("MainWindow", "START"))
        self.exit_btn.setText(_translate("MainWindow", "EXIT"))
        self.title_label.setText(_translate("MainWindow", "LTO EXAM REVIEWER"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
