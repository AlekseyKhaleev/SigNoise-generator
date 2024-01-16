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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QMainWindow, QRadioButton, QSizePolicy, QSlider,
    QStatusBar, QWidget)

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
        self.noise_label.setGeometry(QRect(910, 40, 91, 16))
        self.noise_line = QLineEdit(self.centralwidget)
        self.noise_line.setObjectName(u"noise_line")
        self.noise_line.setGeometry(QRect(1030, 60, 71, 22))
        self.filter_box = QGroupBox(self.centralwidget)
        self.filter_box.setObjectName(u"filter_box")
        self.filter_box.setGeometry(QRect(860, 100, 171, 141))
        self.average_radio = QRadioButton(self.filter_box)
        self.average_radio.setObjectName(u"average_radio")
        self.average_radio.setGeometry(QRect(10, 30, 161, 20))
        self.average_radio.setChecked(True)
        self.median_radio = QRadioButton(self.filter_box)
        self.median_radio.setObjectName(u"median_radio")
        self.median_radio.setEnabled(True)
        self.median_radio.setGeometry(QRect(10, 60, 95, 20))
        self.median_radio.setChecked(False)
        self.gausse_radio = QRadioButton(self.filter_box)
        self.gausse_radio.setObjectName(u"gausse_radio")
        self.gausse_radio.setGeometry(QRect(10, 90, 95, 20))
        self.exp_radio = QRadioButton(self.filter_box)
        self.exp_radio.setObjectName(u"exp_radio")
        self.exp_radio.setGeometry(QRect(10, 120, 151, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.noise_label.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c \u0448\u0443\u043c\u0430", None))
        self.filter_box.setTitle(QCoreApplication.translate("MainWindow", u"\u0424\u0438\u043b\u044c\u0442\u0440", None))
        self.average_radio.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u043b\u044c\u0437\u044f\u0449\u0435\u0435 \u0441\u0440\u0435\u0434\u043d\u0435\u0435", None))
        self.median_radio.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0434\u0438\u0430\u043d\u043d\u044b\u0439", None))
        self.gausse_radio.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0430\u0443\u0441\u0441\u0430", None))
        self.exp_radio.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u043f\u043e\u043d\u0435\u043d\u0446\u0438\u0430\u043b\u044c\u043d\u044b\u0439", None))
    # retranslateUi

