# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\BartendeerV2.7.1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(793, 658)
        MainWindow.setMinimumSize(QtCore.QSize(793, 658))
        MainWindow.setMaximumSize(QtCore.QSize(793, 658))
        font = QtGui.QFont()
        font.setFamily("SCG")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(500, 100, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.tableWidget_3 = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_3.setGeometry(QtCore.QRect(60, 280, 671, 241))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.tableWidget_3.setFont(font)
        self.tableWidget_3.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget_3.setIconSize(QtCore.QSize(0, 5))
        self.tableWidget_3.setRowCount(100)
        self.tableWidget_3.setObjectName("tableWidget_3")
        self.tableWidget_3.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)
        font = QtGui.QFont()
        font.setFamily("SCG")
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily("SCG")
        item.setFont(font)
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, item)
        self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(215)
        self.tableWidget_3.horizontalHeader().setHighlightSections(False)
        self.tableWidget_3.verticalHeader().setVisible(False)
        self.tableWidget_3.verticalHeader().setHighlightSections(True)
        self.tableWidget_3.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget_3.verticalHeader().setStretchLastSection(False)
        self.tableWidget_3.horizontalHeader().setCascadingSectionResizes(False)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(310, 100, 171, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(400, 222, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(470, 222, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.label_31 = QtWidgets.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(60, 60, 221, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setObjectName("label_31")
        self.label_44 = QtWidgets.QLabel(self.centralwidget)
        self.label_44.setGeometry(QtCore.QRect(630, 535, 101, 51))
        self.label_44.setObjectName("label_44")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(500, 170, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_32 = QtWidgets.QLabel(self.centralwidget)
        self.label_32.setGeometry(QtCore.QRect(310, 80, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setObjectName("label_32")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 100, 231, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_33 = QtWidgets.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(500, 70, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(500, 140, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setObjectName("label_34")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(240, 540, 161, 41))
        self.pushButton_7.setMaximumSize(QtCore.QSize(16777210, 16777215))
        font = QtGui.QFont()
        font.setFamily("SCG")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_7.setStyleSheet("background-color : orange ; color : white ;")
        self.pushButton_7.setIconSize(QtCore.QSize(13, 13))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(60, 540, 161, 41))
        self.pushButton_8.setMaximumSize(QtCore.QSize(16777210, 16777215))
        font = QtGui.QFont()
        font.setFamily("SCG")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.pushButton_8.setFont(font)
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_8.setStyleSheet("background-color : #4F7942 ; color : white ;")
        self.pushButton_8.setIconSize(QtCore.QSize(13, 13))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(60, 160, 161, 41))
        self.pushButton_9.setMaximumSize(QtCore.QSize(16777210, 16777215))
        font = QtGui.QFont()
        font.setFamily("SCG")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.pushButton_9.setFont(font)
        self.pushButton_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_9.setStyleSheet("background-color : #4F7942 ; color : white ;")
        self.pushButton_9.setIconSize(QtCore.QSize(13, 13))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(240, 160, 161, 41))
        self.pushButton_10.setMaximumSize(QtCore.QSize(16777210, 16777215))
        self.pushButton_10.setSizeIncrement(QtCore.QSize(0, 8))
        font = QtGui.QFont()
        font.setFamily("SCG")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.NoAntialias)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_10.setStyleSheet("background-color : orange ; color : white ;")
        self.pushButton_10.setIconSize(QtCore.QSize(13, 13))
        self.pushButton_10.setObjectName("pushButton_10")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 751, 221))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 230, 751, 351))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 250, 751, 351))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.raise_()
        self.groupBox.raise_()
        self.comboBox.raise_()
        self.tableWidget_3.raise_()
        self.lineEdit_2.raise_()
        self.label_31.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.label_44.raise_()
        self.comboBox_2.raise_()
        self.label_32.raise_()
        self.lineEdit.raise_()
        self.label_33.raise_()
        self.label_34.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.pushButton_9.raise_()
        self.pushButton_10.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 793, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)



        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bartendeer-2.8"))
        self.comboBox.setItemText(0, _translate("MainWindow", "None"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Floor : 2"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Floor : 3"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Floor : 2 & Display"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Floor : 3 & Display"))
        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Edge ID"))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Note"))
        item = self.tableWidget_3.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Component"))


        self.label.setText(_translate("MainWindow", "Status :"))
        self.label_31.setText(_translate("MainWindow", "Edge Barcode"))
        self.label_44.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/WODE/Split/WODE.jpg\"/></p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "None"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Edge Device"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Outdoor Sensor"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Indoor Floor 1"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Indoor Floor 2"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "Indoor Floor 3"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "Zigbee"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "Smart Display"))
        self.label_32.setText(_translate("MainWindow", "Note"))
        self.label_33.setText(_translate("MainWindow", "Select Component"))
        self.label_34.setText(_translate("MainWindow", "Single Component"))
        self.pushButton_7.setText(_translate("MainWindow", "Clear"))
        self.pushButton_8.setText(_translate("MainWindow", "Print"))
        self.pushButton_9.setText(_translate("MainWindow", "Add"))
        self.pushButton_10.setText(_translate("MainWindow", "Delete"))
        self.groupBox.setTitle(_translate("MainWindow", "Regist"))
        self.groupBox_2.setTitle(_translate("MainWindow", "GroupBox"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Data List"))
import WODE_New
