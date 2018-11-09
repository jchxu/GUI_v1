# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'trend_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_trend_dialog(object):
    def setupUi(self, trend_dialog):
        trend_dialog.setObjectName("trend_dialog")
        trend_dialog.resize(800, 600)
        self.comboBox_3 = QtWidgets.QComboBox(trend_dialog)
        self.comboBox_3.setGeometry(QtCore.QRect(100, 10, 81, 30))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_4 = QtWidgets.QLabel(trend_dialog)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 101, 31))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.comboBox_4 = QtWidgets.QComboBox(trend_dialog)
        self.comboBox_4.setGeometry(QtCore.QRect(190, 10, 81, 30))
        font = QtGui.QFont()
        font.setFamily("新宋体")
        font.setPointSize(12)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")

        self.retranslateUi(trend_dialog)
        QtCore.QMetaObject.connectSlotsByName(trend_dialog)

    def retranslateUi(self, trend_dialog):
        _translate = QtCore.QCoreApplication.translate
        trend_dialog.setWindowTitle(_translate("trend_dialog", "质量变化趋势分析"))
        self.comboBox_3.setItemText(0, _translate("trend_dialog", "焦煤"))
        self.comboBox_3.setItemText(1, _translate("trend_dialog", "肥煤"))
        self.comboBox_3.setItemText(2, _translate("trend_dialog", "1/3焦煤"))
        self.comboBox_3.setItemText(3, _translate("trend_dialog", "气煤"))
        self.comboBox_3.setItemText(4, _translate("trend_dialog", "瘦煤"))
        self.label_4.setText(_translate("trend_dialog", "基础煤种"))
        self.comboBox_4.setItemText(0, _translate("trend_dialog", "1"))
        self.comboBox_4.setItemText(1, _translate("trend_dialog", "2"))
        self.comboBox_4.setItemText(2, _translate("trend_dialog", "3"))
        self.comboBox_4.setItemText(3, _translate("trend_dialog", "4"))
        self.comboBox_4.setItemText(4, _translate("trend_dialog", "5"))
        self.comboBox_4.setItemText(5, _translate("trend_dialog", "6"))
        self.comboBox_4.setItemText(6, _translate("trend_dialog", "7"))

