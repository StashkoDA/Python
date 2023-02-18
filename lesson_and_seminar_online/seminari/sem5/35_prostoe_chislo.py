# Задача №35.
# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

# def prime_number(a):
#     if a != 0 and a % a == 0 and a / 1 == a and a % a**0.5 != 0:
#         i = 2
#         while i < 10:
#             if a % i != 0:
#                 i += 1
#             elif a == i:
#                 i += 1
#             else:
#                 return 'no'
#         return 'yes'
#     elif int(a) == 0:
#         return 'Вы ввели ноль'
#     else:
#         return 'no'

# n = float(input('Введите число: '))
# print(prime_number(n))


# или ///////////

def prime_number(a):
    num_list = list(range(2, int(a ** 0.5) + 1))
    for i in num_list:
        if a % i == 0:
            return 'no'
    return 'yes'

n = int(input('Введите число: '))
print(prime_number(n))