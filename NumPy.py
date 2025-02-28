import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0       # Среднее значение
std_dev = 1    # Стандартное отклонение
num_samples = 1000  # Количество образцов

# Генерация случайных чисел, распределенных по нормальному распределению
data = np.random.normal(mean, std_dev, num_samples)

# Создание гистограммы
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, alpha=0.7, color='blue', edgecolor='black')

# Добавление заголовка и меток
plt.title('Гистограмма нормального распределения')
plt.xlabel('Значение')
plt.ylabel('Частота')

# Показать график
plt.grid()
plt.show()

# Генерация двух массивов случайных чисел
x = np.random.rand(5)  # массив из 5 случайных чисел для оси X
y = np.random.rand(5)  # массив из 5 случайных чисел для оси Y

# Печать массивов
print("Массив X:", x)
print("Массив Y:", y)

# Построение диаграммы рассеивания
plt.scatter(x, y)
plt.title('Диаграмма рассеивания')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.grid(True)
plt.show()