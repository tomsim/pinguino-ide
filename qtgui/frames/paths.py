# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/yeison/.virtualenvs/pinguino_env/pinguino/pinguino-ide/qtgui/frames/paths.ui'
#
# Created: Wed Jan  8 21:17:47 2014
#      by: pyside-uic 0.2.14 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Paths(object):
    def setupUi(self, Paths):
        Paths.setObjectName("Paths")
        Paths.resize(737, 246)
        self.centralwidget = QtGui.QWidget(Paths)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtGui.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_sdcc_bin = QtGui.QPushButton(self.groupBox)
        self.pushButton_sdcc_bin.setObjectName("pushButton_sdcc_bin")
        self.gridLayout.addWidget(self.pushButton_sdcc_bin, 0, 2, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit_sdcc_bin = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_sdcc_bin.setObjectName("lineEdit_sdcc_bin")
        self.gridLayout.addWidget(self.lineEdit_sdcc_bin, 0, 1, 1, 1)
        self.lineEdit_pinguino_8_libs = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_pinguino_8_libs.setObjectName("lineEdit_pinguino_8_libs")
        self.gridLayout.addWidget(self.lineEdit_pinguino_8_libs, 1, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.pushButton_pinguino_8_libs = QtGui.QPushButton(self.groupBox)
        self.pushButton_pinguino_8_libs.setObjectName("pushButton_pinguino_8_libs")
        self.gridLayout.addWidget(self.pushButton_pinguino_8_libs, 1, 2, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton_gcc_bin = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_gcc_bin.setObjectName("pushButton_gcc_bin")
        self.gridLayout_2.addWidget(self.pushButton_gcc_bin, 0, 2, 1, 1)
        self.lineEdit_gcc_bin = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_gcc_bin.setObjectName("lineEdit_gcc_bin")
        self.gridLayout_2.addWidget(self.lineEdit_gcc_bin, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.lineEdit_pinguino_32_libs = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_pinguino_32_libs.setObjectName("lineEdit_pinguino_32_libs")
        self.gridLayout_2.addWidget(self.lineEdit_pinguino_32_libs, 1, 1, 1, 1)
        self.pushButton_pinguino_32_libs = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_pinguino_32_libs.setObjectName("pushButton_pinguino_32_libs")
        self.gridLayout_2.addWidget(self.pushButton_pinguino_32_libs, 1, 2, 1, 1)
        self.gridLayout_4.addWidget(self.groupBox_2, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(304, 23, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_close = QtGui.QPushButton(self.centralwidget)
        self.pushButton_close.setMinimumSize(QtCore.QSize(161, 0))
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout.addWidget(self.pushButton_close)
        self.gridLayout_4.addLayout(self.horizontalLayout, 2, 0, 1, 2)
        Paths.setCentralWidget(self.centralwidget)

        self.retranslateUi(Paths)
        QtCore.QMetaObject.connectSlotsByName(Paths)
        Paths.setTabOrder(self.pushButton_close, self.lineEdit_sdcc_bin)
        Paths.setTabOrder(self.lineEdit_sdcc_bin, self.pushButton_sdcc_bin)
        Paths.setTabOrder(self.pushButton_sdcc_bin, self.lineEdit_gcc_bin)
        Paths.setTabOrder(self.lineEdit_gcc_bin, self.pushButton_gcc_bin)

    def retranslateUi(self, Paths):
        Paths.setWindowTitle(QtGui.QApplication.translate("Paths", "Pinguino Paths", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("Paths", "8bit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_sdcc_bin.setText(QtGui.QApplication.translate("Paths", "Change...", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Paths", "SDCC compiler:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Paths", "Libraries:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_pinguino_8_libs.setText(QtGui.QApplication.translate("Paths", "Change...", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("Paths", "32bit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_gcc_bin.setText(QtGui.QApplication.translate("Paths", "Change...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Paths", "GCC compiler:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Paths", "Libraries:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_pinguino_32_libs.setText(QtGui.QApplication.translate("Paths", "Change...", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_close.setText(QtGui.QApplication.translate("Paths", "Close", None, QtGui.QApplication.UnicodeUTF8))

