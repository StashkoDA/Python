# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

# def array(b1, dd, nn, arr):
#     i = 0
#     while i < nn:
#         bn = b1 + i*dd
#         arr.append(bn)
#         i += 1

# a1 = int(input('Введите первый элемент: '))
# d = int(input('Введите разность между элементами: '))
# n = int(input('Введите кол-во элементов: '))
# arr = []
# array(a1, d, n, arr)
# print(arr)

# или /////////////////
# a1 = int(input('Введите первый элемент: '))
# d = int(input('Введите разность между элементами: '))
# n = int(input('Введите кол-во элементов: '))
# arr = []
# for i in range(n):
#   an = a1 + i * d
#   arr.append(an)    
# print(arr)

# или /////////////////
a1 = int(input('Введите первый элемент: '))
d = int(input('Введите разность между элементами: '))
n = int(input('Введите кол-во элементов: '))
arr = [a1 + i * d for i in range(n)]   
print(arr)
