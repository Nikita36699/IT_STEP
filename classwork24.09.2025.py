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


def add_item(cart):
    name = input("Введіть назву товару: ")
    price = int(input("Введіть ціну товару: "))

    item_info = {
        'name': name,
        'price': price
    }

    cart.append(item_info)


def save_cart(cart, filename='cart.json'):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(cart, file, indent=4)


def load_cart(filename='cart.json'):
    with open(filename, 'r', encoding='utf-8') as file:
        cart = json.load(file)

    return cart


def display_cart(cart):
    print(json.dumps(cart, indent=2))


def main():
    print("Робота з кошиком")

    cart = [] # кошик з товарами

    while True:
        print()
        print('1 - додати товар')
        print('2 - зберегти кошик')
        print('3 - завантажити збережений кошик')
        print('4 - показати кошик')
        print('5 - завершити програму')

        choice = input("Введіть номер команди: ")

        if choice == '1':
            add_item(cart)

        elif choice == '2':
            save_cart(cart)

        elif choice == '3':
            cart = load_cart()

        elif choice == '4':
            display_cart(cart)

        elif choice == '5':
            break

        else:
            print("Невірна команда")


if __name__ == '__main__':
    main()