import numpy as np

# Заданные данные
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

# Функция потерь (Mean Squared Error)
def mse_loss(b, x, y):
    return np.mean((y - b * x) ** 2)

# Градиент функции потерь по коэффициенту наклона (slope)
def gradient(b, x, y):
    return -2 * np.mean(x * (y - b * x))

# Градиентный спуск
def gradient_descent(x, y, learning_rate=0.0001, epochs=1000):
    b = 0  # Начальное значение коэффициента наклона
    for _ in range(epochs):
        grad = gradient(b, x, y)
        b -= learning_rate * grad  # Обновление коэффициента наклона
    return b

# Вычисление коэффициента наклона с использованием градиентного спуска
b_gradient_descent = gradient_descent(zp, ks)

# Вывод результата
print("Коэффициент линейной регрессии (slope) с использованием градиентного спуска (без intercept):", b_gradient_descent)
