# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1411, 1024)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: rgb(45, 50, 56);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(94, 94, 94);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(15, -1, 15, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.relionButton = QtWidgets.QPushButton(self.frame)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 143, 142))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 215, 197))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 179, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 71, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 95, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 143, 142))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 143, 142))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(198, 199, 193))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 143, 142))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 215, 197))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 179, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 71, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 95, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 143, 142))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 143, 142))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(198, 199, 193))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 143, 142))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 215, 197))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(176, 179, 164))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(70, 71, 65))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(94, 95, 87))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 143, 142))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 143, 142))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 143, 131))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.relionButton.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.relionButton.setFont(font)
        self.relionButton.setAutoFillBackground(False)
        self.relionButton.setStyleSheet("background-color: rgb(141, 143, 142);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding-top: 30px;\n"
"padding-bottom: 30px;\n"
"")
        self.relionButton.setObjectName("relionButton")
        self.verticalLayout.addWidget(self.relionButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem1)
        self.csparcButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.csparcButton.setFont(font)
        self.csparcButton.setStyleSheet("background-color: rgb(141, 143, 142);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding-top: 30px;\n"
"padding-bottom: 30px;")
        self.csparcButton.setObjectName("csparcButton")
        self.verticalLayout.addWidget(self.csparcButton)
        spacerItem2 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem2)
        self.parserButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.parserButton.setFont(font)
        self.parserButton.setStyleSheet("background-color: rgb(141, 143, 142);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding-top: 30px;\n"
"padding-bottom: 30px;")
        self.parserButton.setObjectName("parserButton")
        self.verticalLayout.addWidget(self.parserButton)
        spacerItem3 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem3)
        self.nnButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.nnButton.setFont(font)
        self.nnButton.setStyleSheet("background-color: rgb(141, 143, 142);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding-top: 30px;\n"
"padding-bottom: 30px;")
        self.nnButton.setObjectName("nnButton")
        self.verticalLayout.addWidget(self.nnButton)
        spacerItem4 = QtWidgets.QSpacerItem(20, 50, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem4)
        self.pickButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.pickButton.setFont(font)
        self.pickButton.setStyleSheet("background-color: rgb(141, 143, 142);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"padding-top: 30px;\n"
"padding-bottom: 30px;")
        self.pickButton.setObjectName("pickButton")
        self.verticalLayout.addWidget(self.pickButton)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"text-align: center;\n"
"margin-bottom: 0px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Roboto Thin")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(69, 69, 69);\n"
"color: rgb(255, 255, 255);\n"
"padding-top: 20px;\n"
"padding-bottom: 20px;\n"
"margin-top: 0px;\n"
"margin-bottom: 0px;")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setStyleSheet("color: white;")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout.addWidget(self.frame)
        self.mainTab = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.mainTab.setFont(font)
        self.mainTab.setObjectName("mainTab")
        self.dbTab = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("Source Sans Pro")
        font.setPointSize(14)
        self.dbTab.setFont(font)
        self.dbTab.setStyleSheet("::tab {\n"
"    \n"
"    background-color: rgb(255, 85, 127);\n"
"}")
        self.dbTab.setObjectName("dbTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dbTab)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.treeView = QtWidgets.QTreeView(self.dbTab)
        self.treeView.setObjectName("treeView")
        self.verticalLayout_3.addWidget(self.treeView)
        self.mainTab.addTab(self.dbTab, "")
        self.nnTab = QtWidgets.QWidget()
        self.nnTab.setObjectName("nnTab")
        self.mainTab.addTab(self.nnTab, "")
        self.horizontalLayout.addWidget(self.mainTab)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.mainTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.relionButton.setText(_translate("MainWindow", "Import Relion Project"))
        self.csparcButton.setText(_translate("MainWindow", "Import CSparc Project"))
        self.parserButton.setText(_translate("MainWindow", "Auto Parser"))
        self.nnButton.setText(_translate("MainWindow", "Train Neural Network"))
        self.pickButton.setText(_translate("MainWindow", "Pick Particles"))
        self.label.setText(_translate("MainWindow", "ONN Database / Parser"))
        self.pushButton.setText(_translate("MainWindow", "Settings"))
        self.label_2.setText(_translate("MainWindow", "Purdue @ 2020"))
        self.mainTab.setTabText(self.mainTab.indexOf(self.dbTab), _translate("MainWindow", "Database"))
        self.mainTab.setTabText(self.mainTab.indexOf(self.nnTab), _translate("MainWindow", "Neural Networks"))
