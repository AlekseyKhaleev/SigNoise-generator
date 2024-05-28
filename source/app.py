import os
from enum import IntEnum
from fnmatch import fnmatch

from PySide6.QtCore import Signal
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QInputDialog, QMainWindow, QStackedLayout, QTextEdit

from functools import partial
from designed_ui.designed_interface import Ui_MainWindow
from source.plot import PlotLayout

# from designed_interface import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    temp_saved = Signal()
    temp_loaded = Signal()
    temp_generated = Signal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.current_dir = os.path.dirname(os.path.abspath(__file__))

        self.plot_lay = PlotLayout(self.a1_spin.value(), self.a2_spin.value(), self.a3_spin.value(),
                                   self.b1_spin.value(), self.b2_spin.value(), self.b3_spin.value(),
                                   self.x0_spin.value(), self.xk_spin.value(), self.dx_spin.value())
        self.plot_area.setLayout(self.plot_lay)
        self.average_checked()

        # ---------------------------- connections----------------------------------------
        self.noise_slider.valueChanged.connect(self.show_noise)
        self.noise_slider.valueChanged.connect(self.plot_lay.change_noise_lvl)
        self.average_radio.toggled.connect(self.average_checked)
        self.exp_radio.toggled.connect(self.exp_checked)
        self.gausse_radio.toggled.connect(self.gausse_checked)
        self.median_radio.toggled.connect(self.median_checked)

        self.a1_spin.valueChanged.connect(self.change_params)
        self.a2_spin.valueChanged.connect(self.change_params)
        self.a3_spin.valueChanged.connect(self.change_params)
        self.b1_spin.valueChanged.connect(self.change_params)
        self.b2_spin.valueChanged.connect(self.change_params)
        self.b3_spin.valueChanged.connect(self.change_params)
        self.x0_spin.valueChanged.connect(self.change_params)
        self.xk_spin.valueChanged.connect(self.change_params)
        self.dx_spin.valueChanged.connect(self.change_params)
        self.scale_inc_button.clicked.connect(self.plot_lay.y_scale_inc)
        self.scale_dec_button.clicked.connect(self.plot_lay.y_scale_dec)

        # ---------------------------------------------------------------------------------

    def show_noise(self, value: int):
        self.noise_line.setText(f'{value / 100} ')

    def average_checked(self):
        self.plot_lay.change_strategy("Moving Average")

    def exp_checked(self):
        self.plot_lay.change_strategy("Exponential")

    def gausse_checked(self):
        self.plot_lay.change_strategy("Gaussian")

    def median_checked(self):
        self.plot_lay.change_strategy("Median")

    def change_params(self):
        self.plot_lay.change_params({'a1': self.a1_spin.value(), 'a2': self.a2_spin.value(), 'a3': self.a3_spin.value(),
                                     'b1': self.b1_spin.value(), 'b2': self.b2_spin.value(), 'b3': self.b3_spin.value(),
                                     'x0': self.x0_spin.value(), 'xk': self.xk_spin.value(),
                                     'dx': self.dx_spin.value()})


