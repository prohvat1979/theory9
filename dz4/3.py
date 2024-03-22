import math

# Функция плотности вероятности
def f_x(x):
    return (1 / (4 * math.sqrt(2 * math.pi))) * math.exp(-(x + 2)**2 / 32)

# Вычисление математического ожидания M(X)
def compute_mean(f, a, b, n):
    integral = 0
    dx = (b - a) / n
    for i in range(n):
        x_i = a + i * dx
        integral += x_i * f(x_i) * dx
    return integral

mean = compute_mean(f_x, -100, 100, 1000)

print("Математическое ожидание M(X):", mean)

# Вычисление дисперсии D(X)
def compute_variance(f, mean, a, b, n):
    integral = 0
    dx = (b - a) / n
    for i in range(n):
        x_i = a + i * dx
        integral += (x_i - mean)**2 * f(x_i) * dx
    return integral

variance = compute_variance(f_x, mean, -100, 100, 1000)

print("Дисперсия D(X):", variance)

# Вычисление среднего квадратичного отклонения std(X)
std_dev = math.sqrt(variance)

print("Среднее квадратичное отклонение std(X):", std_dev)


