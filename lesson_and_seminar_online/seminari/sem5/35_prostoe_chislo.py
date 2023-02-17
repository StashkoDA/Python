# Задача №35.
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def prime_number(a):
    if a != 0 and a % a == 0 and a / 1 == a:
        return 'yes'
    elif int(a) == 0:
        return 'Вы ввели ноль'
    else:
        return 'no'

n = float(input('Введите число: '))
print(prime_number(n))