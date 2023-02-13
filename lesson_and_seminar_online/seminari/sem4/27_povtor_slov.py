# Задача №27.
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure. So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

text = input('Введите текст: ')
d = dict()
count = 0
text = text.replace(".","")
text = text.replace(",","")
print(text)
text = text.lower()
print(text)
text = text.split()
text = list(set(text))
print(len(text))
