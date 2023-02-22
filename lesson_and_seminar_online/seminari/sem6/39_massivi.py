# Задача №39.
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод:                 Вывод:
# 7                     3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)

n = int(input('Введите кол-во эл-тов в первом массиве: '))
n_list = [int(input(f'Введите {i} элемент первого массива: ')) for i in range(1, n+1)]
m = int(input('Введите кол-во эл-тов во втором массиве: '))
m_list = [int(input(f'Введите {i} элемент второго массива: ')) for i in range(1, m+1)]

print(n_list)
print(m_list)

res =[]

for i in n_list:
    if i not in m_list:
        res.append(i)
print(res)

# или ////// с примером добавления условия else для информации

# list1 = [int(input(f'Введите {i + 1}-е число: ')) for i in range(int(input('Введите количество элементов первого массива: ')))]
# list2 = [int(input(f'Введите {j + 1}-е число: ')) for j in range(int(input('Введите количество элементов второго массива: ')))]
# new_list = [el if el not in list2 else 0 for el in list1 ]
# print(new_list)