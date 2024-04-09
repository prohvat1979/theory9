import numpy as np

# Заданные данные
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

# Функция потерь (Mean Squared Error)
def mse_loss(b0, b1, x, y):
    return np.mean((y - (b0 * x + b1)) ** 2)

# Градиент функции потерь по коэффициенту наклона (slope) и intercept
def gradient(b0, b1, x, y):
    grad_b0 = -2 * np.mean(x * (y - (b0 * x + b1)))
    grad_b1 = -2 * np.mean(y - (b0 * x + b1))
    return grad_b0, grad_b1

# Градиентный спуск с обновлением коэффициентов на каждой итерации
def gradient_descent_with_intercept(x, y, learning_rate=0.0001, epochs=1000):
    b0 = 0  # Начальное значение коэффициента наклона
    b1 = 0  # Начальное значение intercept
    for _ in range(epochs):
        grad_b0, grad_b1 = gradient(b0, b1, x, y)
        b0 -= learning_rate * grad_b0  # Обновление коэффициента наклона
        b1 -= learning_rate * grad_b1  # Обновление intercept
    return b0, b1

# Вычисление коэффициентов линейной регрессии с использованием градиентного спуска с intercept
b0_gradient_descent, b1_gradient_descent = gradient_descent_with_intercept(zp, ks)

# Вывод результатов
print("Коэффициенты линейной регрессии (slope и intercept) с использованием градиентного спуска:")
print("Свободный член (intercept):", b1_gradient_descent)
print("Коэффициент наклона (slope):", b0_gradient_descent)
