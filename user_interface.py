from read_contact import read_contact
from save_contacts import save_to_csv
from export_to_txt import export_to_txt
from export_to_xml import export_to_xml
from export_to_json import export_to_json
import os
import time


def clear():
    return os.system('cls')


def start():
    clear()
    print('Выберите операцию:', '1 - Добавить новый контакт',
          '2 - Вывод данных в терминал', '3 - Экспорт данных в файл', '4 - Завершение работы',
          sep='\n')
    operation_select = int(input())
    clear()
    if operation_select == 1:
        soname = input('Введите фамилию: ')
        name = input('Введите имя: ')
        phone_number = input('Введите номер телефона: ')
        description = input('Введите описание: ')
        new_list = [soname, name, phone_number, description]
        save_to_csv(new_list)
        start()
        return new_list
    elif operation_select == 2:
        print('Как вывести информацию  каждого контакта?:',
              '1 - построчно', '2 - в одну строку', sep='\n')
        num = int(input())
        clear()
        if num == 1 or num == 2:
            read_contact(num)
        num = int(input('Введите "1", чтобы продолжить\n'))
        while num != 1:
            num = int(input('Введите "1", чтобы продолжить\n'))
        start()
    elif operation_select == 3:
        print('Выберите формат экспорта данных:',
              '1 - txt', '2 - xml', '3 - json', sep='\n')
        num = int(input())
        clear()
        if num == 1:
            export_to_txt()
            print('Данные экспортированы в txt')
            time.sleep(2)
        elif num == 2:
            export_to_xml()
            print('Данные экспортированы в xml')
            time.sleep(2)
        elif num == 3:
            export_to_json()
            print('Данные экспортированы в json')
            time.sleep(2)
        else:
            print('Неверный ввод')
            time.sleep(2)
            start()
        start()
    elif operation_select == 4:
        print('Пока!')
        exit(0)
    else:
        print('Неверный ввод')
        start()
