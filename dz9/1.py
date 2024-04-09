import numpy as np

# Заданные данные
zp = np.array([35, 45, 190, 200, 40, 70, 54, 150, 120, 110])
ks = np.array([401, 574, 874, 919, 459, 739, 653, 902, 746, 832])

# Расчет с использованием intercept
x_mean = np.mean(zp)
y_mean = np.mean(ks)

b_with_intercept = np.sum((zp - x_mean) * (ks - y_mean)) / np.sum((zp - x_mean) ** 2)
a_with_intercept = y_mean - b_with_intercept * x_mean

# Расчет без использования intercept
b_without_intercept = np.sum(zp * ks) / np.sum(zp ** 2)

# Вывод результатов
print("Коэффициенты линейной регрессии с использованием intercept:")
print("Свободный член (intercept):", a_with_intercept)
print("Коэффициент наклона (slope):", b_with_intercept)

print("\nКоэффициент линейной регрессии без использования intercept:")
print("Коэффициент наклона (slope):", b_without_intercept)
