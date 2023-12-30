import Note


def create_note(min_size, name, content):
    name = check_len_text(input('Введите изменения в название заметки ' + '"' + name + '": '), min_size)
    content = input('Введите изменения в содержание заметки ' + '"' + content + '": ')
    return Note.Note(name=name, content=content)


def check_len_text(text, min_size):
    while len(text) <= min_size:
        print(f'Текст не должен содержать меньше {min_size} символов!')
        text = input('\n Введите текст: \n')
    else:
        return text