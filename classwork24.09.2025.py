# # пакування даних
#
# # файлів
#
# filename = 'file.txt'
#
# # записати інформацію у файл
# with open(filename, 'w', encoding='utf-8') as file:
#     file.write('[1, 245, 3]')
#
# # читання даних з файлу
# with open(filename, 'r', encoding='utf-8') as file:
#     data = file.read()
#
# print(type(data))
# print(data)

# data = {
#     "name": "John",
#     "age": 25,
#     "items": [
#         "pen",
#         "apple"
#     ]
# }

# # JSON
# import json
#
#
# data = {
#     "name": "Антон",
#     "age": 25,
#     "items": [
#         "pen",
#         "apple"
#     ]
# }
#
# # запис dump
# with open('data.json', 'w', encoding='utf-8') as file:
#     json.dump(data, file, indent=4)
#
# # читання даних load
# with open('data.json', 'r', encoding='utf-8') as file:
#     data: dict = json.load(file)
#
# print(type(data))
# print(data)
# print(data['items'])


# нюанси
import json
from xml.etree.ElementTree import indent

# class Person:
#     def __init__(self, name, age, items):
#         self.name = name
#         self.age = age
#         self.items = items
#
#     def method(self):
#         pass
#
#     def save(self, filename):
#         data = {
#             'name': self.name,
#             'age': self.age,
#             'items': self.items
#         }
#
#         with open(filename, 'w', encoding='utf-8') as file:
#             json.dump(data, file, indent=4)
#
#
# person = Person('Mary', 34, ['baggage', 'hljh'])
#
# with open('data.json', 'w', encoding='utf-8') as file:
#     json.dump(person, file, indent=4)
#
# person.method()

# data = {1, 2, 3, 4, 5}
# data = list(data)
#
# # запис dump
# with open('data.json', 'w', encoding='utf-8') as file:
#     json.dump(data, file, indent=4)
#
# # читання даних load
# with open('data.json', 'r', encoding='utf-8') as file:
#     data: dict = json.load(file)
#
# print(type(data))
# print(data)

# # функції dumps loads
# data = {
#     "name": "John",
#     "age": 25,
#     "items": [
#         "pen",
#         "apple"
#     ]
# }
#
# data_encoded = json.dumps(data)
#
# print(type(data_encoded))
# print(repr(data_encoded))  # repr -- щоб побачити як у коді
#
# data_decoded = json.loads(data_encoded)
#
# print(type(data_decoded))
# print(repr(data_decoded))


# Користувач вводить назву та ціну продукту. Добавте їх у кошик
# Також збережіть дані у файл

#
# def add_item(cart):
#     name = input("Введіть назву товару: ")
#     price = int(input("Введіть ціну товару: "))
#
#     item_info = {
#         'name': name,
#         'price': price
#     }
#
#     cart.append(item_info)
#
#
# def save_cart(cart, filename='cart.json'):
#     with open(filename, 'w', encoding='utf-8') as file:
#         json.dump(cart, file, indent=4)
#
#
# def load_cart(filename='cart.json'):
#     with open(filename, 'r', encoding='utf-8') as file:
#         cart = json.load(file)
#
#     return cart
#
#
# def display_cart(cart):
#     print(json.dumps(cart, indent=2))
#
#
# def main():
#     print("Робота з кошиком")
#
#     cart = [] # кошик з товарами
#
#     while True:
#         print()
#         print('1 - додати товар')
#         print('2 - зберегти кошик')
#         print('3 - завантажити збережений кошик')
#         print('4 - показати кошик')
#         print('5 - завершити програму')
#
#         choice = input("Введіть номер команди: ")
#
#         if choice == '1':
#             add_item(cart)
#
#         elif choice == '2':
#             save_cart(cart)
#
#         elif choice == '3':
#             cart = load_cart()
#
#         elif choice == '4':
#             display_cart(cart)
#
#         elif choice == '5':
#             break
#
#         else:
#             print("Невірна команда")
#
#
# if __name__ == '__main__':
#     main()

# Завдання 1
# Є словник з логінами(ключ) та паролями(значення) користувачів. Реалізуйте програму яка дозволяє:
#  завантажити дані з файлу
#  зберегти дані у файл
#  додати нового користувача
#  видалити користувача
#  зміна паролю
#  вхід у систему(якщо логін і пароль правильні)
# Реалізуйте все через функції.
# import json
#
# def save(logins,file_name ='Login.json'):
#      with open(file_name, 'w', encoding='utf-8') as file:
#          json.dump(logins, file, indent= 4)
#
#
# def download(file_name ='Login.json'):
#     with open(file_name, 'r', encoding='utf-8') as file:
#         logins = json.load(file)
#
#     return  logins
#
#
# def add_user(logins):
#     login = input('введіть логін')
#     password = input('введіть пароль')
#
#     if login in logins:
#         print('цей користувач вже існує')
#     else:
#         logins[login] = password
#         save(logins)
#
#
#
# def delete_user(logins):
#     login = input('введіть логін')
#
#     if login in logins:
#         logins.pop(login)
#         save(logins)
#     else:
#         print('такого юзеру не існує')
#
#
# def сhange_password(logins):
#     login = input('введіть логін')
#
#
#     if login in logins:
#         new_password = input('введіть новий пароль')
#         logins[login] = new_password
#         save(logins)
#     else:
#         print('no such user')
#
#
# def invite_user(logins):
#     login = input('введіть логін')
#     password = input('введіть пароль')
#
#     if login in logins and logins[login] == [password]:
#        print('ви увійшли в систему')
#     else:
#         print('логін або пароль введенні не вірно')
#
#
# def main():
#     logins = {}
#
#     while True:
#         print('Menu')
#         print('\n\t1 -завантажити дані з файлу\n\t2-додати нового користувача\n\t3-видалити користувача\n\t4-change-password\n\t5-login in\n\t6-stop ')
#
#         choise = int(input('make a choice from 1 to 6'))
#
#         if choise == 1:
#             logins =download()
#
#         elif choise == 2:
#             add_user(logins)
#
#         elif choise == 3:
#             delete_user(logins)
#
#         elif choise == 4:
#             сhange_password(logins)
#
#         elif choise == 5:
#             invite_user(logins)
#
#         elif choise == 6:
#             break
#
#         else:
#             print("wrong command")
#
#
# main()

# Завдання 2
# Створіть клас Cart
# Атрибути:
#  user – ім’я користувача
#  items – список товарів
#  total – загальна ціна
# Методи:
#  add(item, price) – добавити товар у кошик
#  delete(item, price) – видалити товар з кошика
#  info() – вивести інформацію про кошик
# Практичне завдання
#  save(fiename) – зберегти дані у файл(за замовчуванням cart.json)
#  load(fiename) – завантажити дані з файла(за замовчуванням cart.json)
# Завдання 2
# Створіть клас Cart
# Атрибути:
#  user – ім’я користувача
#  items – список товарів
#  total – загальна ціна
# Методи:
#  add(item, price) – добавити товар у кошик
#  delete(item, price) – видалити товар з кошика
#  info() – вивести інформацію про кошик
# save(fiename) – зберегти дані у файл(за замовчуванням cart.json)
#  load(fiename) – завантажити дані з файла(за замовчуванням cart.json)

import json


class Cart:
    def __init__(self, user):
        self.user = user
        self.items = []
        self.total = 0

    def add(self):
        item = input("Введіть товар: ")
        price = float(input("Та вкажіть його ціну: "))

        self.items.append(item)
        self.total += price

    def delete(self, item, price):
        if item in self.items:
            self.items.remove(item)
            self.total -= price
        else:
            print(f"Товару \"{item}\" немає в кошику.")

    def info(self):
        print()
        print(f"У кошику клієнта {self.user} знаходяться такі товари:")
        for item in self.items:
            print(f"\t{item}")
        print(f"На загальну суму: {self.total:.2f} грн.")

    # save(fiename) – зберегти дані у файл(за замовчуванням cart.json)
    def save(self, filename="cart.json"):
        with open(filename, 'r', encoding='utf-8') as file:
            data_all = json.load(file)

        data_all[self.user] = {
            "items": self.items,
            "total": self.total,
        }

        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data_all, file, indent=4)

    #  load(fiename) – завантажити дані з файла(за замовчуванням cart.json)
    def load(self, filename="cart.json"):
        with open(filename, 'r', encoding='utf-8') as file:
            data_dict: dict = json.load(file)
        user_data = data_dict[self.user]
        print(user_data)
        self.items = user_data["items"]
        self.total = user_data["total"]



if __name__ == '__main__':
   my_cart = Cart("John")

   my_cart.add()
   my_cart.add()
   my_cart.info()

   my_cart.save()

   my_cart1 = Cart("Mary")
   my_cart1.add()
   my_cart1.save()
   my_cart1.info()



# Завдання 3
# Створіть файл settings.json з базовими налаштуваннями програми, наприклад графічного інтерфейсу:
#  розмір зображення – 500х600
#  колір фону – сірий
#  колір кнопок – світлосірий
#  розміщення кнопок – [100, 50]
#  інструкція користувачу
# Напишіть код, де завантажується налаштування і створюються відповідні змінні size, background_color, …