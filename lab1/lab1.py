import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Заданные пользователем значения
a1, b1 = 1, 2
a2, b2 = 3, 4
a3, b3 = 5, 6
x0, xk, dx = 0, 10, 0.1

# Расчет y(x)
x = np.arange(x0, xk, dx)
y = a1 * np.sin(b1 * x) + a2 * np.sin(b2 * x) + a3 * np.sin(b3 * x)

# Добавление шума
noise = np.random.normal(0, 1, len(x))  # шум с нулевым средним и стандартным отклонением 1
y_noisy = y + noise

# Восстановление исходной функции с помощью скользящего среднего
window_size = 5  # размер окна для скользящего среднего
y_smooth = pd.Series(y_noisy).rolling(window_size, min_periods=1).mean().values

# Построение графика
plt.plot(x, y, label='Исходная функция')
plt.plot(x, y_noisy, label='Зашумленная функция')
plt.plot(x, y_smooth, label='Восстановленная функция')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()