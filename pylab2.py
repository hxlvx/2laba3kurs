import numpy as np
# 1файл для пул реквесту
# 1. Створення одновимірного масиву з 200 випадкових чисел від -100 до 100
array = np.random.randint(-100, 101, size=200)
print("Початковий масив (перших 10 елементів):", array[:10])

# 2. Використання маски для фільтрації всіх додатних чисел
positive_mask = array > 0
positive_numbers = array[positive_mask]
print("\nДодатні числа (перших 10 елементів):", positive_numbers[:10])
print("Кількість додатних чисел:", len(positive_numbers))

# 3. Заміна всіх від'ємних значень на нулі
modified_array = np.where(array < 0, 0, array)
print("\nМасив після заміни від'ємних значень на нулі (перших 10 елементів):", modified_array[:10])

# 4. Обчислення середнього значення отриманого масиву
mean_value = np.mean(modified_array)
print("\nСереднє значення отриманого масиву:", mean_value)