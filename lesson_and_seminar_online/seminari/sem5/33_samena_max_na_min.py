# Задача №33.
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

import random
n = int(input('Введите кол-во оценок: '))
l_estimates = [random.randint(1, 5) for i in range(n)]
print(*l_estimates)
min = 5
max = 1
l_new = []
for i in l_estimates:
    if i < min:
        min = i
    if i > max:
        max = i
for i in l_estimates:
    if i == max:
        i = min
        l_new.append(i)
    else:
        l_new.append(i)
print(*l_new)