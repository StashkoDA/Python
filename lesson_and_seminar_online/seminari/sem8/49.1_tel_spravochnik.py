# Задача №49. 
# Создать телефонный справочник с возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер телефона - данные,
# которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной


# Зададим главное меню
def main_menu(): 
    print("\nГлавное меню\n") 
    print("1. Показать все контакты") 
    print("2. Добавить новый контакт") 
    print("3. Поиск контакта") 
    print("4. Выход") 
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
        print("~ Спасибо за использование телефонного справочника! ~") 
    else: 
        print( "Пожалуйста, укажите доступный ввод!\n") 
        enter = input( "Нажмите Enter, чтобы продолжить ...") 
        main_menu() 
 
# Зададим функцию поиска        
def searchcontact(): 
    searchname = input( "Введите имя для поиска контакта: ") 
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

# Вывод заголовка программы:
print("\n~ Добро пожаловать в телефонный справочник! ~") 
 
# Создадим файл для хранения контактов:
filename = "myphonebook.txt" 
myfile = open(filename, "a+") 
myfile.close 

main_menu()