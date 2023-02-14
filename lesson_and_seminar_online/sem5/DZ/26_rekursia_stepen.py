# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def getDegree(m, n):
    if n == 0:
        return 1
    return getDegree(m, n-1) * m

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))

for i in range(b+1):
    getDegree(a, i)
    if i == b:
        print(f'A = {a}, B = {b}, {a}^{b} -> {getDegree(a, i)}')
