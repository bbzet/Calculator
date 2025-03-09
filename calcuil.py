# Form implementation generated from reading ui file '.\calculator.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(459, 517)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.input1 = QtWidgets.QLineEdit(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input1.sizePolicy().hasHeightForWidth())
        self.input1.setSizePolicy(sizePolicy)
        self.input1.setStyleSheet("    color: black;\n"
"    font-size: 32px;\n"
"    font-weight: bold;\n"
"    font-family: \"SF Pro Display\", \"Roboto\", Arial, sans-serif;\n"
"    background-color: #E0E0E0;\n"
"    border-radius: 8px;\n"
"    padding: 10px;\n"
"    min-height: 60px;\n"
"    text-align: right;\n"
"    border: 2px solid #D3D3D3;\n"
"    border-radius: 8px;\n"
"    padding: 10px;")
        self.input1.setText("")
        self.input1.setMaxLength(16)
        self.input1.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.input1.setReadOnly(True)
        self.input1.setObjectName("input1")
        self.verticalLayout.addWidget(self.input1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_equal = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_equal.sizePolicy().hasHeightForWidth())
        self.btn_equal.setSizePolicy(sizePolicy)
        self.btn_equal.setStyleSheet("    font-family: \"Helvetica Neue\", Arial, sans-serif;\n"
"    font-size: 20px;\n"
"    font-weight: 600;\n"
"    background-color: #4AC4F3;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 10px;")
        self.btn_equal.setObjectName("btn_equal")
        self.gridLayout.addWidget(self.btn_equal, 4, 3, 1, 1)
        self.btn_6 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy)
        self.btn_6.setStyleSheet("    font-family: \"Helvetica Neue\", Arial, sans-serif; \n"
"    font-size: 20px;  \n"
"    font-weight: 600;  \n"
"    color: black;\n"
"    background-color: white;\n"
"    border: 2px solid #D3D3D3;\n"
"    border-radius: 8px;\n"
"    padding: 10px;")
        self.btn_6.setObjectName("btn_6")
        self.gridLayout.addWidget(self.btn_6, 2, 2, 1, 1)
        self.btn_0 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy)
        self.btn_0.setStyleSheet("    font-family: \"Helvetica Neue\", Arial, sans-serif; \n"
"    font-size: 20px;  \n"
"    font-weight: 600;  \n"
"    color: black;\n"
"    background-color: white;\n"
"    border: 2px solid #D3D3D3;\n"
"    border-radius: 8px;\n"
"    padding: 10px;")
        self.btn_0.setObjectName("btn_0")
        self.gridLayout.addWidget(self.btn_0, 4, 0, 1, 2)
        self.btn_1 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy)
        self.btn_1.setStyleSheet("    font-family: \"Helvetica Neue\", Arial, sans-serif; \n"
"    font-size: 20px;  \n"
"    font-weight: 600;  \n"
"    color: black;\n"
"    background-color: white;\n"
"    border: 2px solid #D3D3D3;\n"
"    border-radius: 8px;\n"
"    padding: 10px;")
        self.btn_1.setObjectName("btn_1")
        self.gridLayout.addWidget(self.btn_1, 3, 0, 1, 1)
        self.bt_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bt_4.sizePolicy().hasHeightForWidth())
        self.bt_4.setSizePolicy(sizePolicy)
        self.bt_4.setStyleSheet("    font-family: \"Helvetica Neue\", Arial, sans-serif; \n"
"    font-size: 20px;  \n"
"    font-weight: 600;  \n"
"    color: black;\n"
"    background-color: white;\n"
"    border: 2px solid #D3D3D3;\n"
"    border-radius: 8px;\n"
"    padding: 10px;")
        self.bt_4.setObjectName("bt_4")
        self.gridLayout.addWidget(self.bt_4, 2, 0, 1, 1)
        self.btn_clear = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy)
        self.btn_clear.setStyleSheet("    font-family: \"Helvetica Neue\", Arial, sans-serif;\n"
"    font-size: 20px;\n"
"    font-weight: 600;\n"
"    background-color: #D6D6D6; \n"
"    color: black;\n"
"    border-radius: 8px;\n"
"    padding: 10px;")
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout.addWidget(self.btn_clear, 0, 0, 1, 1)
        self.btn_div = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_div.sizePolicy().hasHeightForWidth())
        self.btn_div.setSizePolicy(sizePolicy)
        self.btn_div.setStyleSheet("    font-family: \"Helvetica Neue\", Arial, sans-serif;\n"
"    font-size: 20px;\n"
"    font-weight: 600;\n"
"    background-color: #4AC4F3;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 10px;")
        self.btn_div.setObjectName("btn_div")
        self.gridLayout.addWidget(self.btn_div, 1, 3, 1, 1)
        self.btn_pands = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_pands.sizePolicy().hasHeightForWidth())
        self.btn_pands.setSizePolicy(sizePolicy)
        self.btn_pands.setStyleSheet("    font-family: \"Helvetica Neue\", Arial, sans-serif;\n"
"    font-size: 20px;\n"
"    font-weight: 600;\n"
"    background-color: #D6D6D6; \n"
"    color: black;\n"
"    border-radius: 8px;\n"
"    padding: 10px;")
        self.btn_pands.setObjectName("btn_pands")
        self.gridLayout.addWidget(self.btn_pands, 0, 1, 1, 1)
        self.btn_backspace = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_backspace.sizePolicy().hasHeightForWidth())
        self.btn_backspace.setSizePolicy(sizePolicy)
        self.btn_backspace.setStyleSheet("    font-family: \"Helvetica Neue\", Arial, sans-serif;\n"
"    font-size: 20px;\n"
"    font-weight: 600;\n"
"    background-color: #D6D6D6; \n"
"    color: black;\n"
"    border-radius: 8px;\n"
"    padding: 10px;")
        self.btn_backspace.setObjectName("btn_backspace")
        self.gridLayout.addWidget(self.btn_backspace, 0, 2, 1, 1)
        self.btn_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy)
        self.btn_5.setStyleSheet("    font-family: \"Helvetica Neue\", Arial, sans-serif; \n"
"    font-size: 20px;  \n"
"    font-weight: 600;  \n"
"    color: black;\n"
"    background-color: white;\n"
"    border: 2px solid #D3D3D3;\n"
"    border-radius: 8px;\n"
"    padding: 10px;")
        self.btn_5.setObjectName("btn_5")
        self.gridLayout.addWidget(self.btn_5, 2, 1, 1, 1)
        self.btn_7 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy)
        self.btn_7.setStyleSheet("    font-family: \"Helvetica Neue\", Arial, sans-serif; \n"
"    font-size: 20px;  \n"
"    font-weight: 600;  \n"
"    color: black;\n"
"    background-color: white;\n"
"    border: 2px solid #D3D3D3;\n"
"    border-radius: 8px;\n"
"    padding: 10px;")
        self.btn_7.setObjectName("btn_7")
        self.gridLayout.addWidget(self.btn_7, 1, 0, 1, 1)
        self.btn_8 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy)
        self.btn_8.setStyleSheet("    font-family: \"Helvetica Neue\", Arial, sans-serif; \n"
"    font-size: 20px;  \n"
"    font-weight: 600;  \n"
"    color: black;\n"
"    background-color: white;\n"
"    border: 2px solid #D3D3D3;\n"
"    border-radius: 8px;\n"
"    padding: 10px;")
        self.btn_8.setObjectName("btn_8")
        self.gridLayout.addWidget(self.btn_8, 1, 1, 1, 1)
        self.btn_dot = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_dot.sizePolicy().hasHeightForWidth())
        self.btn_dot.setSizePolicy(sizePolicy)
        self.btn_dot.setStyleSheet("    font-family: \"Helvetica Neue\", Arial, sans-serif; \n"
"    font-size: 20px;  \n"
"    font-weight: 600;  \n"
"    color: black;\n"
"    background-color: white;\n"
"    border: 2px solid #D3D3D3;\n"
"    border-radius: 8px;\n"
"    padding: 10px;")
        self.btn_dot.setObjectName("btn_dot")
        self.gridLayout.addWidget(self.btn_dot, 4, 2, 1, 1)
        self.btn_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy)
        self.btn_3.setStyleSheet("    font-family: \"Helvetica Neue\", Arial, sans-serif; \n"
"    font-size: 20px;  \n"
"    font-weight: 600;  \n"
"    color: black;\n"
"    background-color: white;\n"
"    border: 2px solid #D3D3D3;\n"
"    border-radius: 8px;\n"
"    padding: 10px;")
        self.btn_3.setObjectName("btn_3")
        self.gridLayout.addWidget(self.btn_3, 3, 2, 1, 1)
        self.btn_add = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy)
        self.btn_add.setStyleSheet("    font-family: \"Helvetica Neue\", Arial, sans-serif;\n"
"    font-size: 20px;\n"
"    font-weight: 600;\n"
"    background-color: #4AC4F3;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 10px;")
        self.btn_add.setObjectName("btn_add")
        self.gridLayout.addWidget(self.btn_add, 3, 3, 1, 1)
        self.btn_sub = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_sub.sizePolicy().hasHeightForWidth())
        self.btn_sub.setSizePolicy(sizePolicy)
        self.btn_sub.setStyleSheet("    font-family: \"Helvetica Neue\", Arial, sans-serif;\n"
"    font-size: 20px;\n"
"    font-weight: 600;\n"
"    background-color: #4AC4F3;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 10px;")
        self.btn_sub.setObjectName("btn_sub")
        self.gridLayout.addWidget(self.btn_sub, 2, 3, 1, 1)
        self.btn_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy)
        self.btn_2.setStyleSheet("    font-family: \"Helvetica Neue\", Arial, sans-serif; \n"
"    font-size: 20px;  \n"
"    font-weight: 600;  \n"
"    color: black;\n"
"    background-color: white;\n"
"    border: 2px solid #D3D3D3;\n"
"    border-radius: 8px;\n"
"    padding: 10px;")
        self.btn_2.setObjectName("btn_2")
        self.gridLayout.addWidget(self.btn_2, 3, 1, 1, 1)
        self.btn_mult = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_mult.sizePolicy().hasHeightForWidth())
        self.btn_mult.setSizePolicy(sizePolicy)
        self.btn_mult.setStyleSheet("    font-family: \"Helvetica Neue\", Arial, sans-serif;\n"
"    font-size: 20px;\n"
"    font-weight: 600;\n"
"    background-color: #4AC4F3;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 10px;")
        self.btn_mult.setObjectName("btn_mult")
        self.gridLayout.addWidget(self.btn_mult, 0, 3, 1, 1)
        self.btn_9 = QtWidgets.QPushButton(parent=self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy)
        self.btn_9.setStyleSheet("    font-family: \"Helvetica Neue\", Arial, sans-serif; \n"
"    font-size: 20px;  \n"
"    font-weight: 600;  \n"
"    color: black;\n"
"    background-color: white;\n"
"    border: 2px solid #D3D3D3;\n"
"    border-radius: 8px;\n"
"    padding: 10px;")
        self.btn_9.setObjectName("btn_9")
        self.gridLayout.addWidget(self.btn_9, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.btn_equal.setText(_translate("MainWindow", "="))
        self.btn_equal.setShortcut(_translate("MainWindow", "="))
        self.btn_6.setText(_translate("MainWindow", "6"))
        self.btn_6.setShortcut(_translate("MainWindow", "6"))
        self.btn_0.setText(_translate("MainWindow", "0"))
        self.btn_0.setShortcut(_translate("MainWindow", "0"))
        self.btn_1.setText(_translate("MainWindow", "1"))
        self.btn_1.setShortcut(_translate("MainWindow", "1"))
        self.bt_4.setText(_translate("MainWindow", "4"))
        self.bt_4.setShortcut(_translate("MainWindow", "4"))
        self.btn_clear.setText(_translate("MainWindow", "AC"))
        self.btn_div.setText(_translate("MainWindow", "/"))
        self.btn_div.setShortcut(_translate("MainWindow", "/"))
        self.btn_pands.setText(_translate("MainWindow", "+/-"))
        self.btn_backspace.setText(_translate("MainWindow", "<-"))
        self.btn_backspace.setShortcut(_translate("MainWindow", "Backspace"))
        self.btn_5.setText(_translate("MainWindow", "5"))
        self.btn_5.setShortcut(_translate("MainWindow", "5"))
        self.btn_7.setText(_translate("MainWindow", "7"))
        self.btn_7.setShortcut(_translate("MainWindow", "7"))
        self.btn_8.setText(_translate("MainWindow", "8"))
        self.btn_8.setShortcut(_translate("MainWindow", "8"))
        self.btn_dot.setText(_translate("MainWindow", "."))
        self.btn_3.setText(_translate("MainWindow", "3"))
        self.btn_3.setShortcut(_translate("MainWindow", "3"))
        self.btn_add.setText(_translate("MainWindow", "+"))
        self.btn_add.setShortcut(_translate("MainWindow", "+"))
        self.btn_sub.setText(_translate("MainWindow", "-"))
        self.btn_sub.setShortcut(_translate("MainWindow", "-"))
        self.btn_2.setText(_translate("MainWindow", "2"))
        self.btn_2.setShortcut(_translate("MainWindow", "2"))
        self.btn_mult.setText(_translate("MainWindow", "x"))
        self.btn_mult.setShortcut(_translate("MainWindow", "*"))
        self.btn_9.setText(_translate("MainWindow", "9"))
        self.btn_9.setShortcut(_translate("MainWindow", "9"))
