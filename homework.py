# Завдання 1
# Напишіть гру вгадати число: комп’ютер загадує число
# від 1 до 100. Користувач вводить свої відповіді на що
# отримує підказки більше\менше.
# Якщо число вгадане менш ніж за 5 спроб, то переміг
# користувач, інакше комп’ютер.
# Реалізуйте такий функціонал:
#  почати нову гру – користувач вводить числа до
# правильної відповіді
#  вивести результат – кількість перемог та програшів
#  зберегти дані – зберегти кількості перемог та
# програшів у файл
#  завантажити дані – завантажити кількості перемог
# та програшів
# Реалізуйте все функціями
import random
import json


def random_num():
    return random.randint(1, 100)


def user_guess():
    return int(input('Введіть яке число на вашу думку загадав комп’ютер(від 1 до 100): '))


def start_game(stat: dict):
    ran_num = random_num()
    tries = 0

    while True:
        us_guess = user_guess()
        tries += 1

        if ran_num > us_guess:
            print('Загадане число більше за ваше')
        elif ran_num < us_guess:
            print('Загадане число менше за ваше')
        else:
            print('Ви відгадали!')
            if tries < 5:
                print("Ви перемогли!")
                stat['wins'] += 1
            else:
                print("Комп’ютер переміг!")
                stat['loses'] += 1
            break


def save(stat: dict, filename='stat.json'):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(stat, file, ensure_ascii=False)
    print("Статистика збережена!")


def load(filename='stat.json'):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            stat = json.load(file)
        print("Статистика завантажена!")
        return stat
    except FileNotFoundError:
        print("Файл не знайдено, створено нову статистику.")
        return {'wins': 0, 'loses': 0}


def show_result(stat: dict):
    print(f"Перемоги: {stat['wins']} | Поразки: {stat['loses']}")



statistic = load()

while True:
    print("\nМеню:")
    print("1 - Почати нову гру")
    print("2 - Показати результат")
    print("3 - Зберегти статистику")
    print("4 - Завантажити статистику")
    print("5 - Вийти")

    choice = input("Ваш вибір: ")

    if choice == '1':
        start_game(statistic)
    elif choice == '2':
        show_result(statistic)
    elif choice == '3':
        save(statistic)
    elif choice == '4':
        statistic = load()
    elif choice == '5':
        print("До побачення!")
        break
    else:
        print("Невірний вибір, спробуйте ще раз.")