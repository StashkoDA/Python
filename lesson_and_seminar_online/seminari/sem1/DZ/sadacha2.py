# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# numb = int(input('Введите трёхзначное число: '))
# a = numb // 100 % 10
# b = numb // 10 % 10
# c= numb % 10
# sum = a + b + c
# print(f'{numb} -> {sum} ({a} + {b} + {c})')

# или:
n = int(input('Введите трёхзначное число: '))
numb = n
sum = 0
while numb > 0:
    ost = numb % 10
    sum += ost
    numb //= 10
print(f'{n} -> {sum}')