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


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create the maptlotlib FigureCanvas object,
        sc = MplCanvas(self, width=5, height=4, dpi=100)

        # Generate the signal
        a1, b1, a2, b2, a3, b3 = 1, 2, 2, 4, 0.5, 6
        x0, xk, dx = 0, 10, 0.1
        x = np.arange(x0, xk, dx)
        y = a1 * np.sin(b1 * x) + a2 * np.sin(b2 * x) + a3 * np.sin(b3 * x)

        # Add noise to the signal
        noise_level = 0.5
        noise = np.random.normal(0, noise_level, len(y))
        y_noisy = y + noise

        # Smooth the signal using a rolling mean
        window_size = 10
        y_smooth = pd.Series(y_noisy).rolling(window=window_size).mean().values

        # Plot the original, noisy, and smoothed signals
        sc.axes.plot(x, y, label='Original Signal')
        sc.axes.plot(x, y_noisy, label='Noisy Signal')
        sc.axes.plot(x, y_smooth, label='Smoothed Signal')
        sc.axes.legend()

        # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
        toolbar = NavigationToolbar(sc, self)

        layout = QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(sc)

        # Create a placeholder widget to hold our toolbar and canvas.
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()


app = QApplication(sys.argv)
w = MainWindow()
app.exec()
