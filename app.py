# Создать телефонный справочник с возможностью импорта и 
# экспорта данных в формате .txt. Фамилия, имя, отчество, номер телефона - данные, 
# которые должны находиться в файле.

# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных

file_name = 'data.txt'


def show_data() -> str:
    '''Функция показывает содержимое справочника'''
    with open(file_name, 'r', encoding='utf-8') as file:
        book = file.read()
    return book


def new_data(info: str) -> None:
    '''Эта функция добавляет новую информацию в справочник'''
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'\n{info}')


def remove_data(data: list, element):
    '''Эта функция удаляет элемент и перезаписывает файл'''
    el_index = data.index(element)
    del data[el_index]
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in data:
            file.write(f'\n{i}')


def edit_data(data, element):
    '''Эта функция переписывает элемент и перезаписывает файл'''
    el_index = data.index(element)
    data[el_index] = input('Исправьте элемент: ')
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in data:
            file.write(f'\n{i}')


def find_data(book) -> int:
    '''Эта функция ищет информацию в справочнике'''
    temp = input('Поиск: ')
    for i in book:
        if temp in i:
            temp = i
    return temp



print('У справочника есть следующие режимы: \n1 - прочитать, 2 - ввести данные, 3 - поиск, 4 - редактировать, 0 - закрыть программу')
while True:
    mode = input('Выберите режим работы справочника: ')
    if mode == '1':
        print(show_data())
    elif mode == '2':
        info = input('Введите данные: ')
        new_data(info)
    elif mode == '3':
        data = show_data().split('\n')
        element = find_data(data)
        print(element)
    elif mode == '4':
        print('5 - удалить элемент, 6 - редактировать элемент')
        mode = input('Выберите режим работы: ')
        if mode == '5':
            data = show_data().split('\n')
            element = find_data(data)
            print(element)
            mode = input('Удалить этот элемент (7 - да, 8 - нет): ')
            if mode == '7':
                remove_data(data, element)
            elif mode == '8':
                break
        elif mode == '6':
            data = show_data().split('\n')
            element = find_data(data)
            print(element)
            edit_data(data, element)
    elif mode == '0':
        break
    else:
        print('No mode')
