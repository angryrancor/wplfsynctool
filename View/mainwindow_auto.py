# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(841, 682)
        MainWindow.setMinimumSize(QtCore.QSize(655, 213))
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralWidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 831, 681))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMinimumSize(QtCore.QSize(671, 371))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.groupBox.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 30, 781, 281))
        self.groupBox_2.setObjectName("groupBox_2")
        self.secretKeyEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.secretKeyEdit.setEnabled(False)
        self.secretKeyEdit.setGeometry(QtCore.QRect(340, 240, 350, 31))
        self.secretKeyEdit.setMinimumSize(QtCore.QSize(350, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.secretKeyEdit.setFont(font)
        self.secretKeyEdit.setAutoFillBackground(True)
        self.secretKeyEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.secretKeyEdit.setReadOnly(False)
        self.secretKeyEdit.setObjectName("secretKeyEdit")
        self.saveSettingsBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.saveSettingsBtn.setEnabled(False)
        self.saveSettingsBtn.setGeometry(QtCore.QRect(240, 40, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.saveSettingsBtn.setFont(font)
        self.saveSettingsBtn.setObjectName("saveSettingsBtn")
        self.wmPageEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.wmPageEdit.setEnabled(False)
        self.wmPageEdit.setGeometry(QtCore.QRect(340, 90, 350, 31))
        self.wmPageEdit.setMinimumSize(QtCore.QSize(350, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.wmPageEdit.setFont(font)
        self.wmPageEdit.setAutoFillBackground(True)
        self.wmPageEdit.setReadOnly(False)
        self.wmPageEdit.setObjectName("wmPageEdit")
        self.secretKeyLAbel = QtWidgets.QLabel(self.groupBox_2)
        self.secretKeyLAbel.setGeometry(QtCore.QRect(90, 230, 241, 41))
        self.secretKeyLAbel.setMinimumSize(QtCore.QSize(151, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(48, 48, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 48, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.secretKeyLAbel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.secretKeyLAbel.setFont(font)
        self.secretKeyLAbel.setObjectName("secretKeyLAbel")
        self.consKeyLabel = QtWidgets.QLabel(self.groupBox_2)
        self.consKeyLabel.setGeometry(QtCore.QRect(90, 180, 241, 41))
        self.consKeyLabel.setMinimumSize(QtCore.QSize(151, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(48, 48, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 48, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.consKeyLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.consKeyLabel.setFont(font)
        self.consKeyLabel.setObjectName("consKeyLabel")
        self.consKeyEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.consKeyEdit.setEnabled(False)
        self.consKeyEdit.setGeometry(QtCore.QRect(340, 190, 350, 31))
        self.consKeyEdit.setMinimumSize(QtCore.QSize(350, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.consKeyEdit.setFont(font)
        self.consKeyEdit.setAutoFillBackground(True)
        self.consKeyEdit.setEchoMode(QtWidgets.QLineEdit.PasswordEchoOnEdit)
        self.consKeyEdit.setReadOnly(False)
        self.consKeyEdit.setObjectName("consKeyEdit")
        self.pageUrlLabel = QtWidgets.QLabel(self.groupBox_2)
        self.pageUrlLabel.setGeometry(QtCore.QRect(90, 80, 241, 41))
        self.pageUrlLabel.setMinimumSize(QtCore.QSize(151, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(48, 48, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 48, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.pageUrlLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pageUrlLabel.setFont(font)
        self.pageUrlLabel.setObjectName("pageUrlLabel")
        self.editSettingsBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.editSettingsBtn.setGeometry(QtCore.QRect(70, 40, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.editSettingsBtn.setFont(font)
        self.editSettingsBtn.setObjectName("editSettingsBtn")
        self.wpApiUrlEdit = QtWidgets.QLineEdit(self.groupBox_2)
        self.wpApiUrlEdit.setEnabled(False)
        self.wpApiUrlEdit.setGeometry(QtCore.QRect(340, 140, 350, 31))
        self.wpApiUrlEdit.setMinimumSize(QtCore.QSize(350, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.wpApiUrlEdit.setFont(font)
        self.wpApiUrlEdit.setAutoFillBackground(True)
        self.wpApiUrlEdit.setText("")
        self.wpApiUrlEdit.setReadOnly(False)
        self.wpApiUrlEdit.setObjectName("wpApiUrlEdit")
        self.wpApiUrlLabel = QtWidgets.QLabel(self.groupBox_2)
        self.wpApiUrlLabel.setGeometry(QtCore.QRect(90, 130, 241, 41))
        self.wpApiUrlLabel.setMinimumSize(QtCore.QSize(151, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(48, 48, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(48, 48, 48))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.wpApiUrlLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.wpApiUrlLabel.setFont(font)
        self.wpApiUrlLabel.setObjectName("wpApiUrlLabel")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 320, 781, 351))
        self.groupBox_3.setObjectName("groupBox_3")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton.setGeometry(QtCore.QRect(20, 40, 741, 131))
        self.pushButton.setMinimumSize(QtCore.QSize(151, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 180, 751, 160))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.outputText = QtWidgets.QPlainTextEdit(self.groupBox_4)
        self.outputText.setGeometry(QtCore.QRect(10, 30, 731, 121))
        self.outputText.setObjectName("outputText")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Leafly WPAPI Sync"))
        self.groupBox.setTitle(_translate("MainWindow", "Leafly WPAPI Sync"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Settings"))
        self.saveSettingsBtn.setText(_translate("MainWindow", "Save Settings"))
        self.secretKeyLAbel.setText(_translate("MainWindow", "WPAPI Secret Key:"))
        self.consKeyLabel.setText(_translate("MainWindow", "WPAPI Consumer Key:"))
        self.pageUrlLabel.setText(_translate("MainWindow", "Leafly page URL:"))
        self.editSettingsBtn.setText(_translate("MainWindow", "Edit Settings"))
        self.wpApiUrlLabel.setText(_translate("MainWindow", "WPAPI URL:"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Execution"))
        self.pushButton.setText(_translate("MainWindow", "Sync current products and pricing"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Output"))

