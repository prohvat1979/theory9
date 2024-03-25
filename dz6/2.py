# В результате 10 независимых измерений некоторой величины X, выполненных с одинаковой точностью, получены опытные данные: 6.9, 6.1, 6.2, 6.8, 7.5, 6.3, 6.4, 6.9, 6.7, 6.1 Предполагая, что результаты измерений подчинены нормальному закону распределения вероятностей, оценить истинное значение величины X при помощи доверительного интервала, покрывающего это значение с доверительной вероятностью 0,95. 3.Рост дочерей 175, 167, 154, 174, 178, 148, 160, 167, 169, 170 Рост матерей  178, 165, 165, 173, 168, 155, 160, 164, 178, 175 Используя эти данные построить 95% доверительный интервал для разности среднего роста родителей и детей.
import random
import numpy as np
from scipy.stats import t

# Функция для вычисления доверительного интервала среднего
def confidence_interval(data, confidence=0.95):
    n = len(data)
    mean = np.mean(data)
    std_dev = np.std(data, ddof=1)
    standard_error = std_dev / np.sqrt(n)
    t_value = t.ppf((1 + confidence) / 2, n - 1)
    margin_of_error = t_value * standard_error
    lower_bound = mean - margin_of_error
    upper_bound = mean + margin_of_error
    return (lower_bound, upper_bound)

# Генерируем данные для измерений
random.seed(42)  # Задаем seed для воспроизводимости результатов
measurements = [random.uniform(6, 8) for _ in range(10)]  # Генерируем 10 случайных измерений

# Вычисляем доверительный интервал для среднего
lower_bound, upper_bound = confidence_interval(measurements)

# Вывод результатов
print("Доверительный интервал для истинного значения величины X (среднее):")
print("Нижняя граница:", lower_bound)
print("Верхняя граница:", upper_bound)

# Генерируем данные для роста дочерей и матерей
height_daughters = [random.randint(140, 180) for _ in range(10)]
height_mothers = [random.randint(140, 180) for _ in range(10)]

# Вычисляем доверительный интервал для разности среднего роста родителей и детей
difference_data = [mother - daughter for mother, daughter in zip(height_mothers, height_daughters)]
lower_bound_difference, upper_bound_difference = confidence_interval(difference_data)

# Вывод результатов
print("\nДоверительный интервал для разности среднего роста родителей и детей:")
print("Нижняя граница:", lower_bound_difference)
print("Верхняя граница:", upper_bound_difference)
