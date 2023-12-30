import file_handler
import Note
import note_builder

# Минимальное кол-во символов заголовка заметки
min_size = 3

# Добавить заметку
def add():
    note = note_builder.create_note(min_size)
    array = file_handler.read_file()
    for notes in array:
        if Note.Note.get_id(note) == Note.Note.get_id(notes):
            Note.Note.set_id(note)
    array.append(note)
    file_handler.write_file(array, 'a')
    print('Заметка успешно добавлена. Присвоен ID: ' + Note.Note.get_id(note))

# Функция отображения заметок:
def show(text):
    logic = True
    array = file_handler.read_file()
    for notes in array:
        # вывод всех заметок из файла
        if text == 'all':
            logic = False
            print(Note.Note.info(notes))

        # показать заметку по id
        elif text == 'id':
            logic = False
            print('ID: ' + Note.Note.get_id(notes) + '; Название: ' + Note.Note.get_name(notes) + '.')

        # открыть заметку по дате
        elif text == 'date':
            logic = False
            print('Дата создания: ' + Note.Note.get_date(notes) + '; Название: ' + Note.Note.get_name(notes) + '.')

    if logic == True:
        print('Сохраните новую заметку!')

# Редактирование заметки по id:
def id_rewrite():
    id = input(
        'Выберете ID  заметки, которую Вы хотите перезаписать'
        '(ВНИМАНИЕ! прежняя информация в этой заметке сохранена не будет!): ')
    array = file_handler.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            note = note_builder.create_note(min_size, Note.Note.get_name(notes), Note.Note.get_content(notes))
            Note.Note.set_name(notes, note.get_name())
            Note.Note.set_content(notes, note.get_content())
            Note.Note.set_date(notes)
            print('Изменения в заметке c ID:' + id + '  успешно сохранены')
    if logic == True:
        print('Заметка c ID:' + id + ' не найдена. Проверьте правильность внесенного ID!')
    file_handler.write_file(array, 'a')

# Функция удаления заметки по id:
def id_delete():
    id = input('Введите ID заметки, которую хотите удалить (заметка не подлежит восстановлению): ')
    array = file_handler.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            prov = input('Подтвердите удаление заметки (y или n): ').strip().lower()
            if prov == 'y':
                array.remove(notes)
                print('Заметка c ID:' + id + ' успешно удалена')
            elif prov == 'n':
                print('Операция удаления заметки' + 'c ID:' + id + '  отменена')
    if logic == True:
        print('Заметка c ID:' + id + ' не найдена. Проверьте правильность внесенного ID!')
    file_handler.write_file(array, 'a')

# Функция показа заметки по id:
def id_show():
    id = input('Введите ID необходимой заметки: ')
    array = file_handler.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            print(Note.Note.info(notes))
    if logic == True:
        print('Заметка c ID:' + id + ' не найдена. Проверьте правильность внесенного ID!')
    file_handler.write_file(array, 'a')

# Функция показа заметки по дате:
def date_show():
    date = input('Введите дату и время последнего редактирования: ')
    array = file_handler.read_file()
    logic = True
    for notes in array:
        if date == Note.Note.get_date(notes):
            logic = False
            print(Note.Note.info(notes))
    if logic == True:
        print('Заметка c ID:' + id + ' не найдена. Проверьте правильность внесенного ID!')
    file_handler.write_file(array, 'a')