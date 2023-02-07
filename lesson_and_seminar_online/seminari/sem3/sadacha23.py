# Задача №23. 
# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения списка или список задан изначально.

numb = [0, -1, 5, 2, 3]
count = 0
mlist = []
for i in range(len(numb) -1):
    if int(numb[i+1]) > int(numb[i]):
        count += 1
        a = str(f'{numb[i+1]} > {numb[i]}')
        mlist.append(a)
print(count, end=': ')
print(*tuple(mlist), sep=', ', end='\n')


# или
# from random import randint

# my_list = [randint(-10, 10) for _ in range(randint(1, 10))]
# print(my_list)

# counter = 0
# for i in range(1, len(my_list)):
#     if my_list[i] > my_list[i-1]:
#         counter += 1
# print(counter)


# или
# from random import randint

# my_list = [randint(-10, 10) for _ in range(randint(1, 10))]
# print(my_list)

# new_list = [f'{my_list[i]} > {my_list[i-1]}' for i in range(1, len(my_list)) if my_list[i] > my_list[i-1]]
# print(*new_list, sep='; ')
# print(len(new_list))