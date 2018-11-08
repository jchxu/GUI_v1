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

        self.retranslateUi(trend_dialog)
        QtCore.QMetaObject.connectSlotsByName(trend_dialog)

    def retranslateUi(self, trend_dialog):
        _translate = QtCore.QCoreApplication.translate
        trend_dialog.setWindowTitle(_translate("trend_dialog", "质量变化趋势分析"))

