# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designed_interface.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QSizePolicy, QSlider, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1105, 628)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.plot_area = QWidget(self.centralwidget)
        self.plot_area.setObjectName(u"plot_area")
        self.plot_area.setGeometry(QRect(0, 0, 851, 601))
        self.noise_slider = QSlider(self.centralwidget)
        self.noise_slider.setObjectName(u"noise_slider")
        self.noise_slider.setGeometry(QRect(860, 60, 160, 22))
        self.noise_slider.setMaximum(100)
        self.noise_slider.setSingleStep(0)
        self.noise_slider.setOrientation(Qt.Horizontal)
        self.noise_label = QLabel(self.centralwidget)
        self.noise_label.setObjectName(u"noise_label")
        self.noise_label.setGeometry(QRect(910, 40, 71, 16))
        self.noise_line = QLineEdit(self.centralwidget)
        self.noise_line.setObjectName(u"noise_line")
        self.noise_line.setGeometry(QRect(1030, 60, 71, 22))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.noise_label.setText(QCoreApplication.translate("MainWindow", u"NoiseLevel", None))
    # retranslateUi

