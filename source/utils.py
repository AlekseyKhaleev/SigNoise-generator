from abc import ABC, abstractmethod
from scipy.signal import medfilt
from scipy.ndimage import gaussian_filter
import pandas as pd


class SmoothStrategy(ABC):
    @abstractmethod
    def get_y(self, y_noisy):
        pass


class Exponential(SmoothStrategy):
    def get_y(self, y_noisy):
        return pd.Series(y_noisy).ewm(span=5).mean().values


class Gaussian(SmoothStrategy):

    def get_y(self, y_noisy):
        return gaussian_filter(y_noisy, sigma=2)


class Median(SmoothStrategy):

    def get_y(self, y_noisy):
        return medfilt(y_noisy, kernel_size=5)


class MovingAverage(SmoothStrategy):
    def get_y(self, y_noisy):
        window_size = 5
        return pd.Series(y_noisy).rolling(window=window_size).mean().values
