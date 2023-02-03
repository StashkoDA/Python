# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2^k), не превосходящие числа N.
# 10 -> 1 2 4 8

def getdegree(n, k, res):
    while res <= n:
        res = 2**k
        if res <= n:
            print(res)
        k += 1
    return res

n = int(input('Введите целое число больше 0: '))
k = 0
res = 0
result = getdegree (n, k, res)
