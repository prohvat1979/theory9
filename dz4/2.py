# Заданные значения
a = 0.5  # Левая граница
variance = 0.2  # Дисперсия

# Функция для вычисления дисперсии по заданной правой границе
def compute_variance(b):
    return ((b - a) ** 2) / 12

# Функция для проверки, является ли значение близким к решению
def is_close_to_solution(b):
    return abs(compute_variance(b) - variance) < 0.0001

# Метод бисекции для нахождения правой границы
def bisection_method(a, b):
    while b - a > 0.0001:
        mid = (a + b) / 2
        if is_close_to_solution(mid):
            return mid
        elif compute_variance(mid) < variance:
            a = mid
        else:
            b = mid
    return (a + b) / 2

# Начальные значения интервала для метода бисекции
left_bound = 0.5
right_bound = 1.0

# Находим правую границу с помощью метода бисекции
right_bound = bisection_method(left_bound, right_bound)

# Среднее значение величины B
mean = (a + right_bound) / 2

print("Правая граница величины B:", right_bound)
print("Среднее значение величины B:", mean)




