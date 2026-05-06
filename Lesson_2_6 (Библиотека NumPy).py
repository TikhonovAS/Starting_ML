import numpy as np

# 1. Создание одномерного массива
arr1 = np.array([1, 2, 3, 4, 5,])
print(arr1)

# 2. Создание двухмерного массива
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
print(arr2.shape)

# 3. Создание массива с нулями
zeros = np.zeros((3, 3))
print(zeros)

# 4. Создание массива с единицами
ones = np.ones((3, 3))
print(ones)
print(np.ones_like(arr2))

# Создание массива со случайными числами
random_arr = np.random.rand(3, 3)
print(random_arr)

# Математические операции
arr3 = np.array([1, 2, 3])
arr4 = np.array([4, 5, 6])

result = arr3 + arr4
print(result)

result = arr3 - arr4
print(result)

result = arr3 * arr4
print(result)

result = arr3 / arr4
print(result)

# Индексация и срезы
element = arr1[1] # нахождение элемента по индексу
print(element)

subarray = arr2[1] # нахождение части матрицы
print(subarray)

slice = arr1[1:3] # нахождение части списка по срезу
print(slice)

# Индексация с условием
mask = arr1 > 2
print(mask)
masked_data = arr1[mask] # получение окончательных данных
print(masked_data)

# Математические функции
mean = np.mean(arr1) # получение среднеарифметического значение
print(mean)

std = np.std(arr1) # получение значения стандартного отклонения
print(std)

max_value = np.max(arr1) # получение максимального значения из списка
print(max_value)

min_value = np.min(arr1) # получение минимального значения из списка
print(min_value)

# Скалярное произведение
print(arr3)
print(arr4)

dot = arr3.dot(arr4) # скалярное произведение 2-х векторов
print(dot)

arr5 = np.array([[1, 2], [3, 4]])
arr6 = np.array([[3, 4], [5, 6]])
print(arr5.dot(arr6)) # скалярное произведение 2-х матриц

# Транспонирование матрицы
transposed = arr2.T
print(arr2)
print(transposed)