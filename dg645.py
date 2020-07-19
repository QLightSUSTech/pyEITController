from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(150, 110, 421, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_Trig = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_Trig.setObjectName("lineEdit_Trig")
        self.gridLayout.addWidget(self.lineEdit_Trig, 0, 0, 1, 2)
        self.lineEdit_A = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_A.setObjectName("lineEdit_A")
        self.gridLayout.addWidget(self.lineEdit_A, 1, 0, 1, 1)
        self.lineEdit_B = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_B.setObjectName("lineEdit_B")
        self.gridLayout.addWidget(self.lineEdit_B, 1, 1, 1, 1)
        self.lineEdit_C = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_C.setObjectName("lineEdit_C")
        self.gridLayout.addWidget(self.lineEdit_C, 2, 0, 1, 1)
        self.lineEdit_D = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_D.setObjectName("lineEdit_D")
        self.gridLayout.addWidget(self.lineEdit_D, 2, 1, 1, 1)
        self.lineEdit_E = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_E.setObjectName("lineEdit_E")
        self.gridLayout.addWidget(self.lineEdit_E, 3, 0, 1, 1)
        self.lineEdit_F = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_F.setObjectName("lineEdit_F")
        self.gridLayout.addWidget(self.lineEdit_F, 3, 1, 1, 1)
        self.lineEdit_G = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_G.setObjectName("lineEdit_G")
        self.gridLayout.addWidget(self.lineEdit_G, 4, 0, 1, 1)
        self.lineEdit_H = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_H.setObjectName("lineEdit_H")
        self.gridLayout.addWidget(self.lineEdit_H, 4, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 145, 47, 14))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 175, 50, 20))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 205, 50, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(80, 235, 50, 20))
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 115, 80, 20))
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(580, 115, 50, 20))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(580, 145, 50, 20))
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(580, 175, 50, 20))
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(580, 205, 50, 20))
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(580, 235, 50, 20))
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(150, 60, 400, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Delay AB"))
        self.label_2.setText(_translate("MainWindow", "Delay CD"))
        self.label_3.setText(_translate("MainWindow", "Delay EF"))
        self.label_4.setText(_translate("MainWindow", "Delay GH"))
        self.label_5.setText(_translate("MainWindow", "Trigger Rate"))
        self.label_6.setText(_translate("MainWindow", "Hz"))
        self.label_7.setText(_translate("MainWindow", "s"))
        self.label_8.setText(_translate("MainWindow", "s"))
        self.label_9.setText(_translate("MainWindow", "s"))
        self.label_10.setText(_translate("MainWindow", "s"))
        self.label_11.setText(_translate("MainWindow", "DG645 Control Panel"))