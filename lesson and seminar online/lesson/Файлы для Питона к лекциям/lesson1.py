# - закомментировать одну строку
"""
макс - закомментировать много строк через три двойные кавычки до и после нужных строк
или выделить нужные строк и нажать: CTRL+k+C, снять коммент: CTRL+k+u.
"""
# qwerty
# ytrewq



print(5) # CTRL+F5 - запуск кода или ввод в терминал (python+имя файла): python main.py
print(5, 8, 6)
n = 7
print(n)
print(type(n)) # проверка типаint тип
m = None # присвоено переменной пустое значение типа
print(m)
print(type(m))
k = 1.89
print(k)
print(type(k)) # тип float - дробное значение

n = "qwerty"
print(n)
print(type(n)) # тип строка str

n = "qwe \' poi" # установка одной кавычки в строке - через слэш(\)
print(n)

# Интерполяция:
a = 8
b = 5.89
c = "hello"
print(a,b,c)
print(a,'-', b,'-', c)
# или
print(f"{a} - {b} - {c}")
# или
print("{} - {} - {}".format(a,b,c))

# Ввод данных пользователем:
# a = input('Введите число: ') # всегда на выходе выдаёт тип СТРОКА str
# print(a)

# print('Введите а')
# a = input() # 10
# print('Введите b')
# b = input() # 20
# c = 30
# print(a, ' + ', b, ' = ', c) # 10 + 20 = 30

# # Приведение к другому типу:
# print('Введите а')
# a = int(input()) # 10
# print('Введите b')
# b = int(input()) # 20
# c = 30
# print(a, ' + ', b, ' = ', a+b)
# print('{} + {} = {}'.format(a, b, c))

# print('Введите а')
# a = float(input())
# print('Введите b')
# b = float(input())
# c = a + b
# print(a, ' + ', b, ' = ', c)

# a = int(input('Введите \nа: '))
# b = int(input('Введите \nb: '))
# c = a + b
# print('{} + {} = {}'.format(a, b, c))

# a = 5.89789
# b = 7.12345
# print('a*b =', round(a*b,3)) # вывод только с тремя знаками после запятой

# Арифметические операции
# exp1 = 2**3 - 10 % 5 + 2*3
# exp2 = 2**3 - 10 / 5 + 2*3
# print(exp1) # 14.0 или 14
# print(exp2) # 12.0 или 12

# Сокращённые операции и операции присваивания
iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4 # iter = iter - 4
# iter *= 5 # iter = iter * 5
# iter /= 5 # iter = iter / 5
# iter //= 5 # iter = iter // 5
# iter %= 5 # iter = iter % 5
# iter **= 5 # iter = iter ** 5
# print(iter)

# a, b, c = 1, 2, 3
# # a: 1 b: 2 c: 3
# print('a: {} b: {} c: {}'.format(a, b, c))
# print(range(*(1,5,2)))

# Логические операции
# >, >=, <, <=, ==, !=
# not, and, or – не путать с &, |, ^
# Кое-что ещё: is, is not, in, not in

# Управляющие конструкции: if, if-else
# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)

# Управляющие конструкции: while
# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# Управляющие конструкции: while-else
# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит )')
#     print(inverted)
# Пожалуй
# хватит

# original = 23
# inverted = 0
# while original != 0:
#     if inverted == 3:
#         break
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(inverted)

# Управляющие конструкции: for
# for i in 1, -2, 3, 14, 5:
#     print(i)

# r = range(5) # range(0, 5)
# r = range(2, 5) # range(2, 5)
# r = range(-5, 0) # range(-5, 0)
# r = range(1, 10, 2) # range(1, 10, 2)
# r = range(100, 0, -20) # range(100, 0, -20)

# r = range(100, 0, -20) # range(100, 0, -20)
# for i in r:
# print(i)
# # 100 80 60 40 20
# for i in range(5):
# print(i)
# # 0 1 2 3 4

# Вложенные циклы
# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# Немного о строках
text = 'съешь ещё этих мягких французских булок'
print(len(text)) # 39
print('ещё' in text) # True
print(text.isdigit()) # False
print(text.islower()) # True
print(text.replace('ещё','ЕЩЁ')) #
for c in text:
    print(c)