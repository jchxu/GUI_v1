# coding=utf-8

import sys
from PyQt5 import QtGui,QtCore,QtWidgets
from PyQt5.QtWidgets import QDialog
from MainWindows import Ui_MainWindow
from major_dialog import Ui_major_dialog
from minor_dialog import Ui_minor_dialog
from base_dialog import Ui_base_dialog
from classic_dialog import Ui_classic_dialog
from new_dialog import Ui_new_dialog
from mine_dialog import Ui_mine_dialog
from trend_dialog import Ui_trend_dialog

#################### Templete ################################
class Main_Window(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(Main_Window, self).__init__()
        self.setupUi(self)

class Major_Window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_major_dialog()
        self.child.setupUi(self)

class Minor_Window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_minor_dialog()
        self.child.setupUi(self)

class Base_Window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_base_dialog()
        self.child.setupUi(self)

class Classic_Window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_classic_dialog()
        self.child.setupUi(self)

class New_Window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_new_dialog()
        self.child.setupUi(self)

class Mine_Window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_mine_dialog()
        self.child.setupUi(self)

class Trend_Window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.child = Ui_trend_dialog()
        self.child.setupUi(self)


    ######## Slot functions #############

    #def slot_major(self):
    #    print()
    #    price=self.price_box.toPlainText()
    #    self.results_window.setText("hi,PyQt5~")
    #    rate = self.tax_rate.value()
    #    self.results_window.setText(price*rate)
    #    self.label.text(price*rate)
    ######################################


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = Main_Window()
    MajorWindow = Major_Window()
    MinorWindow = Minor_Window()
    BaseWindow = Base_Window()
    ClassicWindow = Classic_Window()
    NewWindow = New_Window()
    MineWindow = Mine_Window()
    TrendWindow = Trend_Window()
    MainWindow.major_lib.clicked.connect(MajorWindow.show)
    MainWindow.minor_lib.clicked.connect(MinorWindow.show)
    MainWindow.base_coal.clicked.connect(BaseWindow.show)
    MainWindow.classic_coal.clicked.connect(ClassicWindow.show)
    MainWindow.new_coal.clicked.connect(NewWindow.show)
    MainWindow.mine_info.clicked.connect(MineWindow.show)
    MainWindow.trend.clicked.connect(TrendWindow.show)

    MainWindow.show()
    sys.exit(app.exec_())