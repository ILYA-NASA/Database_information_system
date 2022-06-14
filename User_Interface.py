# 5. модуль User_Interface
# функция
# def user_choice
# Обращается к  пользователю для выбора режима
# 1) Вывод всей инф
# 2) Вывод всех ДР
# 3) Вывод успеваемости
# 4) Вывод пола
# Возвращает выбор пользователя

from os import system
system('cls')


def user_choice():
    while True:
        user_input = input('''
        1 - вывод дней рождения, 2 - вывод успеваемости 
        3 - вывод пола учеников, 4 - вывод списка целиком
        0 - выход\n
Выберите действие: ''')
        try:
            user_input = int(user_input)
        except:
            print('''
Введите номер цифрой!''')
            continue
        if user_input >= 0 and user_input <= 4:
            return user_input
        else:
            print('''
Выбрать нужно от 0 до 4!''')


if __name__ == '__main__':
    user_choice()
