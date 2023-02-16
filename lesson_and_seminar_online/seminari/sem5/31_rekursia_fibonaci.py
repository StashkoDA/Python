# Задача №31.
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию

def fibo(a):
    if a == 0:
        return 0
    if a in [1, 2]:
        return 1
    return fibo(a-1) + fibo(a-2)

n = int(input('Введите искомое число: '))
list_f = []

# for i in range(n):
#     list_f.append(fibo(i))
# print(list_f)
# print(list_f[n-1])

# # или
i = 0
while i < n:
    list_f.append(fibo(i))
    if i == n-1:
        print(list_f)
        print(list_f[i])
        break
    i += 1