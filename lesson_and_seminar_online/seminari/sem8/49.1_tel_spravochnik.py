# Задача №49. 
# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные,
# которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной
# записи (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных.

# Зададим главное меню
def main_menu(): 
    print("\nГлавное меню\n") 
    print("1. Показать все контакты") 
    print("2. Добавить новый контакт") 
    print("3. Поиск контакта") 
    print("4. Редактировать контакт") 
    print("5. Удалить контакт") 
    print("6. Выход") 
    numb = input("Введите номер функции: ") 
    if numb == "1": 
        myfile = open(filename, "r+") 
        filecontents = myfile.read() # чтение содержимого файла
        if len(filecontents) == 0: 
            print("В телефонном справочнике нет контактов.") 
        else: 
            print(filecontents) 
        myfile.close 
        enter = input("Нажмите Enter, чтобы продолжить ...") 
        main_menu() 
    elif numb == "2": 
        newcontact() 
        enter = input("Нажмите Enter, чтобы продолжить ...") 
        main_menu() 
    elif numb == "3": 
        searchcontact() 
        enter = input("Нажмите Enter, чтобы продолжить ...") 
        main_menu() 
    elif numb == "4":
        editing()
        enter = input("Нажмите Enter, чтобы продолжить ...") 
        main_menu()
    elif numb == "5":
        removal()
        enter = input("Нажмите Enter, чтобы продолжить ...") 
        main_menu()
    
    elif numb == "6": 
        print("~ Спасибо за использование телефонного справочника! ~") 
    else: 
        print( "Пожалуйста, укажите доступный ввод!\n") 
        enter = input( "Нажмите Enter, чтобы продолжить ...") 
        main_menu() 
 
# Зададим функцию поиска        
def searchcontact(): 
    searchname = input("Введите имя для поиска контакта: ") 
    remname = searchname[1:] 
    firstchar = searchname[0] 
    searchname = firstchar.upper() + remname # Приводим введённый запрос с заглавной буквы
    myfile = open(filename, "r+") 
    filecontents = myfile.readlines() # Читаем все строки файла.
      
    found = False 
    for line in filecontents: # Перебираем строки в файле и ищем совпадения в строках
        if searchname in line: 
            print("Ваш искомый контакт:", end = " ") 
            print(line) 
            found = True 
            break 
    if found == False: 
        print( "Контакт отсутствует в телефонном справочнике", searchname) 
 
# Ввод имени:
def input_firstname(): 
    first = input("Введите имя: ") 
    remfname = first[1:] 
    firstchar = first[0] 
    return firstchar.upper() + remfname 

# Ввод отчества:
def input_surname(): 
    surname = input("Введите отчество: ") 
    remsname = surname[1:] 
    firstchar = surname[0] 
    return firstchar.upper() + remsname 

# Ввод фамилии
def input_lastname(): 
    last = input( "Введите фамилию: ") 
    remlname = last[1:] 
    firstchar = last[0] 
    return firstchar.upper() + remlname 
 
# Создание нового контакта
def newcontact(): 
    firstname = input_firstname()
    surname = input_surname()
    lastname = input_lastname() 
    phoneNum = input("Введите номер телефона: ") 
    contactDetails =("[" + firstname + " " + surname + " " + lastname + ", " + phoneNum +  "]\n") 
    myfile = open(filename, "a") 
    myfile.write(contactDetails) 
    print("Контактные данные:\n " + contactDetails + "\nуспешно сохранены!") 

# Редактирование
def editing(): 
    editingname = input("Введите контакт для редактирования: ")
    remname = editingname[1:] 
    firstchar = editingname[0] 
    editingname = firstchar.upper() + remname # Приводим введённый запрос с заглавной буквы
    myfile = open(filename, "r+") 
    filecontents = myfile.readlines() # Читаем все строки файла.
      
    found = False 
    for line in filecontents: # Перебираем строки в файле и ищем совпадения в строках
        if editingname in line: 
            print("Ваш искомый контакт:", end = " ") 
            print(line)
            print("Введите новое имя для редактирования контакта: "  + line)
            
            olddata = input('Введите изменяемый параметр: ')
            remname = olddata[1:] 
            firstchar = olddata[0] 
            olddata = firstchar.upper() + remname

            newdata = input('Введите новый параметр: ')
            remname = newdata[1:] 
            firstchar = newdata[0] 
            newdata = firstchar.upper() + remname

            with open(filename, 'r') as file:
                data = file.read()
                data = data.replace(olddata, newdata)
            with open(filename, 'w') as file:
                file.write(data)
            
            print("Изменения:\n " + newdata + "\n успешно изменены!")
            found = True 
            break 
    if found == False: 
        print( "Отсутствует в телефонном справочнике контакт: ", editingname) 

# удаление
def removal():
    # if searchcontact():
    searchname = input("Введите имя для поиска контакта: ") 
    remname = searchname[1:] 
    firstchar = searchname[0] 
    searchname = firstchar.upper() + remname # Приводим введённый запрос с заглавной буквы
    myfile = open(filename, "r+") 
    filecontents = myfile.readlines() # Читаем все строки файла.
      
    found = False 
    for line in filecontents: # Перебираем строки в файле и ищем совпадения в строках
        if searchname in line: 
            z = line
            print("Ваш искомый контакт:", end = " ") 
            print(line)
            print('Выберите действие: ')
            print('1 - удалить')
            print('2 - отмена')
            numb = input('Введите 1 или 2: ')
            if numb == "1":
                with open(filename, 'r') as fr:
                    text = fr.readlines()
 
                with open(filename, 'w') as fw:
                    for txt in text:
                        if txt != z:
                            fw.write(txt)
                    print("Контакт удалён")
            
            found = True 
            break 
    if found == False: 
        print( "Контакт отсутствует в телефонном справочнике", searchname)

# Вывод заголовка программы:
print("\n~ Добро пожаловать в телефонный справочник! ~") 
 
# Создадим файл для хранения контактов:
filename = "myphonebook.txt" 
myfile = open(filename, "a+") 
myfile.close 

main_menu()