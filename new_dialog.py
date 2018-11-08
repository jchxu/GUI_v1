# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_new_dialog(object):
    def setupUi(self, new_dialog):
        new_dialog.setObjectName("new_dialog")
        new_dialog.resize(800, 600)

        self.retranslateUi(new_dialog)
        QtCore.QMetaObject.connectSlotsByName(new_dialog)

    def retranslateUi(self, new_dialog):
        _translate = QtCore.QCoreApplication.translate
        new_dialog.setWindowTitle(_translate("new_dialog", "新煤种库"))

