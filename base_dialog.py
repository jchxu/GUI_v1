# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'base_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_base_dialog(object):
    def setupUi(self, base_dialog):
        base_dialog.setObjectName("base_dialog")
        base_dialog.resize(800, 600)

        self.retranslateUi(base_dialog)
        QtCore.QMetaObject.connectSlotsByName(base_dialog)

    def retranslateUi(self, base_dialog):
        _translate = QtCore.QCoreApplication.translate
        base_dialog.setWindowTitle(_translate("base_dialog", "基础煤种库"))

