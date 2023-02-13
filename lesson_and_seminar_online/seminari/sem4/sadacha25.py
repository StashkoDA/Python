# Задача №25.
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()

qwe = 'a a a b c a a d c d d'
m_list = qwe.split()
res = []

# countA = 0
# countB = 0
# countC = 0
# countD = 0
# print(m_list)
# for i in range(len(m_list)):
#     if m_list[i] == 'a':
#         if countA == 0:
#             res.append(m_list[i])
#             countA += 1
#         if countA >= 1:
#             m_list[i] = f'{m_list[i]}_{countA}'
#             res.append(m_list[i])
#             countA += 1
#     if m_list[i] == 'b':
#         if countB == 0:
#             res.append(m_list[i])
#             countB += 1
#         if countA >= 1:
#             m_list[i] = f'{m_list[i]}_{countB}'
#             res.append(m_list[i])
#             countB += 1
#     if m_list[i] == 'c':
#         if countC == 0:
#             res.append(m_list[i])
#             countC += 1
#         if countC >= 1:
#             m_list[i] = f'{m_list[i]}_{countC}'
#             res.append(m_list[i])
#             countC += 1
#     if m_list[i] == 'd':
#         if countD == 0:
#             res.append(m_list[i])
#             countD += 1
#         if countD >= 1:
#             m_list[i] = f'{m_list[i]}_{countD}'
#             res.append(m_list[i])
#             countD += 1
# print(res)


# или

d = {'a': 0,'b': 0, 'c': 0, 'd': 0}
for i in m_list:
    if d[i] == 0:
        res.append(i)
        d[i] = d.get(i) + 1
    else:
        res.append(f'{i}_{d.get(i)}')
        d[i] = d.get(i) + 1
print(res)
