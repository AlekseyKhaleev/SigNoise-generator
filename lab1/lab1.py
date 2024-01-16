import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure


class Graphic(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100,*args):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(Graphic, self).__init__(fig)
        # Заданные пользователем значения
        # self.a1, self.b1 = 1, 2
        # self.a2, self.b2 = 3, 4
        # self.a3, self.b3 = 5, 6
        # self.x0, self.xk, self.dx = 0, 10, 0.1
        self.a1, self.b1, self.a2, self.b2, self.a3, self.b3, self.x0, self.xk, self.dx = args
        self.x, self.y, self.y_noisy, self.y_smooth = None, None, None, None

    def __get_xy(self):
        # Расчет y(x)
        self.x = np.arange(self.x0, self.xk, self.dx)
        self.y = self.a1 * np.sin(self.b1 * self.x) + self.a2 * np.sin(self.b2 * self.x) + self.a3 * np.sin(
            self.b3 * self.x)

        # Добавление шума
        noise = np.random.normal(0, 1, len(self.x))  # шум с нулевым средним и стандартным отклонением 1
        self.y_noisy = self.y + noise

        # Восстановление исходной функции с помощью скользящего среднего
        window_size = 5  # размер окна для скользящего среднего
        self.y_smooth = pd.Series(self.y_noisy).rolling(window_size, min_periods=1).mean().values

    def plot_lines(self):
        self.__get_xy()
        plt.clf()
        # Построение графика
        plt.plot(self.x, self.y, label='Исходная функция')
        plt.plot(self.x, self.y_noisy, label='Зашумленная функция')
        plt.plot(self.x, self.y_smooth, label='Восстановленная функция')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
