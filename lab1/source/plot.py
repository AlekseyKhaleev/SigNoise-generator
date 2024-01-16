import sys
import numpy as np

import matplotlib
from PySide6.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import pandas as pd

matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


class PlotLayout(QVBoxLayout, QWidget):

    def __init__(self, *args, **kwargs):
        super(PlotLayout, self).__init__(*args, **kwargs)

        # Create the maptlotlib FigureCanvas object,
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)


        # Generate the signal
        a1, b1, a2, b2, a3, b3 = 1, 2, 2, 4, 0.5, 6
        x0, xk, dx = 0, 10, 0.1
        self.x = np.arange(x0, xk, dx)
        self.y = a1 * np.sin(b1 * self.x) + a2 * np.sin(b2 * self.x) + a3 * np.sin(b3 * self.x)

        self.change_noise_lvl(0)

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(self.sc, self)

        self.addWidget(toolbar)
        self.addWidget(self.sc)

    def change_noise_lvl(self, lvl):
        # Сначала очистим предыдущий график
        self.sc.axes.clear()
        lvl /= 100
        # Генерация шума и добавление его к y
        noise = np.random.normal(0, lvl, len(self.y))
        y_noisy = self.y + noise
        window_size = 10
        y_smooth = pd.Series(y_noisy).rolling(window=window_size).mean().values

        self.sc.axes.plot(self.x, self.y, label='Original Signal')
        self.sc.axes.plot(self.x, y_noisy, label='Noisy Signal')
        self.sc.axes.plot(self.x, y_smooth, label='Smoothed Signal')

        # Восстановление легенды и других элементов графика, если они есть
        self.sc.axes.legend(loc='lower left')
        # Зафиксировать ось Y, например, от 0 до 10
        self.sc.axes.set_ylim([-5, 5])

        # Перерисовка графика
        self.sc.draw()