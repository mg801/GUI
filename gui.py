# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(812, 456)
        self.gridLayout_3 = QtWidgets.QGridLayout(Form)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stackedWidget.sizePolicy().hasHeightForWidth())
        self.stackedWidget.setSizePolicy(sizePolicy)
        self.stackedWidget.setToolTip("")
        self.stackedWidget.setToolTipDuration(-1)
        self.stackedWidget.setStatusTip("")
        self.stackedWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.stackedWidget.setStyleSheet("\n"
"background-color: rgb(251, 255, 183);")
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.stackedWidget.setObjectName("stackedWidget")
        self.stackedWidgetPage1 = QtWidgets.QWidget()
        self.stackedWidgetPage1.setObjectName("stackedWidgetPage1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.stackedWidgetPage1)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.stackedWidgetPage1)
        self.label.setMinimumSize(QtCore.QSize(144, 20))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setUnderline(False)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.stackedWidgetPage1)
        self.frame.setMinimumSize(QtCore.QSize(144, 336))
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius:10px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_2.addWidget(self.frame, 1, 0, 4, 1)
        self.frame_5 = QtWidgets.QFrame(self.stackedWidgetPage1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMinimumSize(QtCore.QSize(262, 118))
        self.frame_5.setAutoFillBackground(False)
        self.frame_5.setStyleSheet("\n"
"border-radius:10px;\n"
"background-color: rgb(255,255, 255);")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_2.addWidget(self.frame_5, 1, 1, 1, 2)
        self.frame_6 = QtWidgets.QFrame(self.stackedWidgetPage1)
        self.frame_6.setMinimumSize(QtCore.QSize(150, 118))
        self.frame_6.setAutoFillBackground(False)
        self.frame_6.setStyleSheet("\n"
"border-radius:10px;\n"
"background-color: rgb(255,255, 255);")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.gridLayout_2.addWidget(self.frame_6, 1, 3, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.stackedWidgetPage1)
        self.frame_3.setMinimumSize(QtCore.QSize(136, 160))
        self.frame_3.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius:10px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2.addWidget(self.frame_3, 1, 4, 2, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.stackedWidgetPage1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QtCore.QSize(149, 221))
        self.scrollArea.setStyleSheet("border-radius:10px;\n"
"background-color: rgb(230,230, 230);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_4 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_4.setGeometry(QtCore.QRect(0, 0, 162, 371))
        self.scrollAreaWidgetContents_4.setObjectName("scrollAreaWidgetContents_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_4)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_4)
        self.label_2.setMinimumSize(QtCore.QSize(144, 20))
        font = QtGui.QFont()
        font.setFamily("Century Schoolbook")
        font.setUnderline(False)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.line = QtWidgets.QFrame(self.scrollAreaWidgetContents_4)
        self.line.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.progressBar_2 = QtWidgets.QProgressBar(self.scrollAreaWidgetContents_4)
        self.progressBar_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_2.setObjectName("progressBar_2")
        self.verticalLayout.addWidget(self.progressBar_2)
        self.progressBar_3 = QtWidgets.QProgressBar(self.scrollAreaWidgetContents_4)
        self.progressBar_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.progressBar_3.setProperty("value", 24)
        self.progressBar_3.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_3.setObjectName("progressBar_3")
        self.verticalLayout.addWidget(self.progressBar_3)
        self.progressBar_4 = QtWidgets.QProgressBar(self.scrollAreaWidgetContents_4)
        self.progressBar_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.progressBar_4.setProperty("value", 24)
        self.progressBar_4.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_4.setObjectName("progressBar_4")
        self.verticalLayout.addWidget(self.progressBar_4)
        self.progressBar_5 = QtWidgets.QProgressBar(self.scrollAreaWidgetContents_4)
        self.progressBar_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.progressBar_5.setProperty("value", 24)
        self.progressBar_5.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_5.setObjectName("progressBar_5")
        self.verticalLayout.addWidget(self.progressBar_5)
        self.progressBar_6 = QtWidgets.QProgressBar(self.scrollAreaWidgetContents_4)
        self.progressBar_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.progressBar_6.setProperty("value", 24)
        self.progressBar_6.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_6.setObjectName("progressBar_6")
        self.verticalLayout.addWidget(self.progressBar_6)
        self.progressBar_7 = QtWidgets.QProgressBar(self.scrollAreaWidgetContents_4)
        self.progressBar_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.progressBar_7.setProperty("value", 24)
        self.progressBar_7.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_7.setObjectName("progressBar_7")
        self.verticalLayout.addWidget(self.progressBar_7)
        self.progressBar_8 = QtWidgets.QProgressBar(self.scrollAreaWidgetContents_4)
        self.progressBar_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.progressBar_8.setProperty("value", 24)
        self.progressBar_8.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_8.setObjectName("progressBar_8")
        self.verticalLayout.addWidget(self.progressBar_8)
        self.progressBar_9 = QtWidgets.QProgressBar(self.scrollAreaWidgetContents_4)
        self.progressBar_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.progressBar_9.setProperty("value", 24)
        self.progressBar_9.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_9.setObjectName("progressBar_9")
        self.verticalLayout.addWidget(self.progressBar_9)
        self.progressBar_13 = QtWidgets.QProgressBar(self.scrollAreaWidgetContents_4)
        self.progressBar_13.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.progressBar_13.setProperty("value", 24)
        self.progressBar_13.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_13.setObjectName("progressBar_13")
        self.verticalLayout.addWidget(self.progressBar_13)
        self.progressBar_10 = QtWidgets.QProgressBar(self.scrollAreaWidgetContents_4)
        self.progressBar_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.progressBar_10.setProperty("value", 24)
        self.progressBar_10.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_10.setObjectName("progressBar_10")
        self.verticalLayout.addWidget(self.progressBar_10)
        self.progressBar_12 = QtWidgets.QProgressBar(self.scrollAreaWidgetContents_4)
        self.progressBar_12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.progressBar_12.setProperty("value", 24)
        self.progressBar_12.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_12.setObjectName("progressBar_12")
        self.verticalLayout.addWidget(self.progressBar_12)
        self.progressBar_11 = QtWidgets.QProgressBar(self.scrollAreaWidgetContents_4)
        self.progressBar_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.progressBar_11.setProperty("value", 24)
        self.progressBar_11.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar_11.setObjectName("progressBar_11")
        self.verticalLayout.addWidget(self.progressBar_11)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_4)
        self.gridLayout_2.addWidget(self.scrollArea, 2, 1, 3, 1)
        self.frame_8 = QtWidgets.QFrame(self.stackedWidgetPage1)
        self.frame_8.setMinimumSize(QtCore.QSize(131, 91))
        self.frame_8.setAutoFillBackground(False)
        self.frame_8.setStyleSheet("\n"
"border-radius:10px;\n"
"background-color: rgb(230,230, 230);")
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_2.addWidget(self.frame_8, 2, 2, 2, 1)
        self.frame_10 = QtWidgets.QFrame(self.stackedWidgetPage1)
        self.frame_10.setMinimumSize(QtCore.QSize(151, 91))
        self.frame_10.setAutoFillBackground(False)
        self.frame_10.setStyleSheet("\n"
"border-radius:10px;\n"
"background-color: rgb(230,230, 230);")
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.gridLayout_2.addWidget(self.frame_10, 2, 3, 2, 1)
        self.frame_4 = QtWidgets.QFrame(self.stackedWidgetPage1)
        self.frame_4.setMinimumSize(QtCore.QSize(136, 160))
        self.frame_4.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"border-radius:10px;")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_2.addWidget(self.frame_4, 3, 4, 2, 1)
        self.frame_9 = QtWidgets.QFrame(self.stackedWidgetPage1)
        self.frame_9.setMinimumSize(QtCore.QSize(131, 91))
        self.frame_9.setAutoFillBackground(False)
        self.frame_9.setStyleSheet("\n"
"border-radius:10px;\n"
"background-color: rgb(230,230, 230);")
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.gridLayout_2.addWidget(self.frame_9, 4, 2, 1, 1)
        self.frame_11 = QtWidgets.QFrame(self.stackedWidgetPage1)
        self.frame_11.setMinimumSize(QtCore.QSize(151, 91))
        self.frame_11.setAutoFillBackground(False)
        self.frame_11.setStyleSheet("\n"
"border-radius:10px;\n"
"background-color: rgb(230,230, 230);")
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.gridLayout_2.addWidget(self.frame_11, 4, 3, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.stackedWidgetPage1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_2.setStyleSheet("\n"
"background-color: rgb(230, 230, 230);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2.addWidget(self.frame_2, 5, 0, 1, 5)
        self.pushButton = QtWidgets.QPushButton(self.stackedWidgetPage1)
        self.pushButton.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 4, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.stackedWidgetPage1)
        self.pushButton_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(229, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 0, 3, 1, 1)
        self.stackedWidget.addWidget(self.stackedWidgetPage1)
        self.stackedWidgetPage2 = QtWidgets.QWidget()
        self.stackedWidgetPage2.setObjectName("stackedWidgetPage2")
        self.gridLayout = QtWidgets.QGridLayout(self.stackedWidgetPage2)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_4 = QtWidgets.QPushButton(self.stackedWidgetPage2)
        self.pushButton_4.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(229, 0, 0);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 0, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.stackedWidgetPage2)
        self.pushButton_3.setStyleSheet("background-color: rgb(170, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.stackedWidget.addWidget(self.stackedWidgetPage2)
        self.gridLayout_3.addWidget(self.stackedWidget, 0, 0, 1, 1)

        self.pushButton.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(1))
        self.pushButton_2.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(0))
        self.pushButton_3.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(1))
        self.pushButton_4.clicked.connect(lambda : self.stackedWidget.setCurrentIndex(0))


        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "INVERTED"))
        self.label_2.setText(_translate("Form", "CELL VOLTAGES"))
        self.pushButton.setText(_translate("Form", "MASTER "))
        self.pushButton_2.setText(_translate("Form", "USER "))
        self.pushButton_4.setText(_translate("Form", "USER "))
        self.pushButton_3.setText(_translate("Form", "MASTER "))



