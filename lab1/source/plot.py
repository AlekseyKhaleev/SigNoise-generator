import numpy as np

import matplotlib
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

from source.utils import SmoothStrategy, Exponential, Gaussian, Median, MovingAverage

matplotlib.use('Qt5Agg')


class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, strategy: SmoothStrategy, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)
        self.sm_strategy = strategy


class PlotLayout(QVBoxLayout, QWidget):
    noise_lvl_changed = Signal()
    strategy_changed = Signal()
    params_changed = Signal()

    def __init__(self, /, a1, a2, a3, b1, b2, b3, x0, xk, dx, *args, **kwargs, ):
        super(PlotLayout, self).__init__(*args, **kwargs)
        # ---------------------------- connections----------------------------------------
        self.noise_lvl_changed.connect(self.draw_plot)
        self.strategy_changed.connect(self.draw_plot)
        self.params_changed.connect(self.draw_plot)

        # ---------------------------------------------------------------------------------

        self.params = {'a1': a1, 'a2': a2, 'a3': a3, 'b1': b1, 'b2': b2, 'b3': b3, 'x0': x0, 'xk': xk, 'dx': dx}
        # Create the maptlotlib FigureCanvas object,
        self.sc = MplCanvas(Exponential(), self, width=5, height=4, dpi=100)

        # Generate the signal
        self.noise_lvl = 0

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(self.sc, self)

        self.addWidget(toolbar)
        self.addWidget(self.sc)
        self.draw_plot()



    def change_noise_lvl(self, lvl):
        self.noise_lvl = lvl/100
        self.noise_lvl_changed.emit()

    def draw_plot(self):
        # Сначала очистим предыдущий график
        self.sc.axes.clear()

        x = np.arange(self.params['x0'], self.params['xk'], self.params['dx'])
        y = self.params['a1'] * np.sin(self.params['b1'] * x) + self.params['a2'] * np.sin(
            self.params['b2'] * x) + self.params['a3'] * np.sin(self.params['b3'] * x)
        # Генерация шума и добавление его к y
        noise = np.random.normal(0, self.noise_lvl, len(y))
        y_noisy = y + noise
        y_smooth = self.sc.sm_strategy.get_y(y_noisy)

        self.sc.axes.plot(x, y, label='Оригинальный сигнал')
        self.sc.axes.plot(x, y_noisy, label='Искаженный сигнал')
        self.sc.axes.plot(x, y_smooth, label='Восстановленный сигнал')

        # Восстановление легенды и других элементов графика, если они есть
        self.sc.axes.legend(loc='lower left')
        # Зафиксировать ось Y, например, от 0 до 10
        self.sc.axes.set_ylim([-5, 5])

        # Перерисовка графика
        self.sc.draw()

    def change_strategy(self, checkbox: str) -> None:
        match checkbox:
            case "Exponential":
                self.sc.sm_strategy = Exponential()
            case "Gaussian":
                self.sc.sm_strategy = Gaussian()
            case "Median":
                self.sc.sm_strategy = Median()
            case "Moving Average":
                self.sc.sm_strategy = MovingAverage()
        self.strategy_changed.emit()

    def change_params(self, new_params: dict) -> None:
        self.params = new_params
        self.params_changed.emit()
