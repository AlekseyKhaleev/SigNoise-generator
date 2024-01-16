import os
from enum import IntEnum
from fnmatch import fnmatch

from PySide6.QtCore import Signal
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import QInputDialog, QMainWindow, QStackedLayout, QTextEdit

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
        self.show_noise(0)
        self.plot_lay = PlotLayout()
        self.plot_area.setLayout(self.plot_lay)
        # ---------------------------- connections----------------------------------------
        self.noise_slider.valueChanged.connect(self.show_noise)
        self.noise_slider.valueChanged.connect(self.plot_lay.change_noise_lvl)
        # self.text_btn.clicked.connect(self.show_text)
        # self.render_btn.clicked.connect(self.show_html)
        # self.generate_btn.clicked.connect(self.generate)
        # self.clear_btn.clicked.connect(self.text_edit.clear)
        # self.clear_btn.clicked.connect(self.show_text)
        # self.save_btn.clicked.connect(self.save_modal)
        # self.load_btn.clicked.connect(self.load_template)
        # self.temp_saved.connect(self.update_templates)
        # self.temp_loaded.connect(self.show_text)
        # self.temp_generated.connect(self.show_text)
        # ---------------------------------------------------------------------------------

    def show_noise(self, value: int):
        self.noise_line.setText(f'{value/100} ')

