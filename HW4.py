# Реализуйте алгоритм перемешивания списка, без использования встроеных методов (особенно SHUFFLE, без него) можно (нужно) использовать библиотеку Random

import random

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f'Первичный список: {list}')

for i in range(len(list)-1):
    j = random.randint(0, len(list)-1)
    list[i], list[j] = list[j], list[i]
    
print(f'Случайный список: {list}')