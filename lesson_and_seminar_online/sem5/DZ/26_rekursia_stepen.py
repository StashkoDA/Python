# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def getDegree(m, n):
    if n == 0:
        return 1
    elif n == 1:
        return m
    return m

a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = 1
for i in range(b+1):
    c = c * getDegree(a, i)
    if i == b:
        print(f'A = {a}, B = {b}, {a}^{b} -> {c}')
