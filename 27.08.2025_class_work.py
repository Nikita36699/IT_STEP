# # поліморфізм
#
# class Cat:
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#
#     def make_sound(self):
#         print('мяу')
#
#     def grow(self):
#         self.age += 1
#
#     def catch_mouse(self):
#         pass
#
# class Dog:
#     def __init__(self, name, age, speed):
#         self.name = name
#         self.age = age
#         self.speed = speed
#
#     def make_sound(self):
#         print('гав')
#
#     def grow(self):
#         self.age += 1
#
#
# class Hamster:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def make_sound(self):
#         print('пі-пі')
#
#     def grow(self):
#         self.age += 1
#
#
# cat = Cat('Murchil', 3, 'black')
# dog = Dog('Barsik', 2, 10)
# hamster = Hamster('Benny',4)
#
# pets = [cat, dog, hamster]
#
# #комжна тварина видає якісь звуки
#
# for pet in pets:
#     pet.make_sound()
#
#
# # model =NeuralNertwork()
# #
# # model.train(data)

#  Завдання 1
# Створіть наступні класи:
#  Rectangle – атрибути width, height
#  Circle – атрибути radius
#  Triangle – атрибути a, b, c
# Методи:
#  get_perimeter()
#  display_info()
# Напишіть функцію create_figure() яка запитує у користувача
# тип фігури та потрібні атрибути і повертає об’єкт.
# Створіть декілька фігур, добавте їх у список та для кожної
# викличте відповідні методи.
# import math
# from typing import list
#
# class Rectangle:
#     def __init__(self, width: float, height: float):
#         self.width = width
#         self.height = height
#
#     def get_perimeter(self):
#         return 2 * self.width + (2 * self.height)
#
#     def display_info(self):
#         print(f'Rectangle:')
#         print(f"\t\t{self.width = }")
#         print(f'\t\t{self.height = }')
#
#
# class Circle:
#     def __init__(self, radius: float):
#         self.radius = radius
#
#     def get_perimeter(self):
#         return math.pi * 2 * self.radius
#
#     def display_info(self):
#         print(f'Circle:')
#         print(f"\t\t{self.radius = }")
#
#
# class Triangle:
#     def __init__(self, a: float, b: float, c: float):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_perimeter(self):
#         return  self.a + self.b + self.c
#
#     def display_info(self):
#         print(f'Triangle:')
#         print(f"\t\t{self.a = }")
#         print(f"\t\t{self.b = }")
#         print(f"\t\t{self.c = }")
#
#
# def create_figure():
#     print('фігури які є:')
#     print('\t\tRectangle')
#     print('\t\tCircle')
#     print('\t\tTriangle')
#
#     user_figure = input('яку фігуру ви хочете?').strip()
#
#     if user_figure == 'Rectangle':
#         params = input('введіть (width, height) через кому' ).strip()
#
#         if params != '':
#             params_list = params.split(',')
#             return Rectangle(float(params_list[0]), float(params_list[1]))
#         else:
#             return None
#
#     elif user_figure == 'Circle':
#         params = input('введіть (radius) ').strip()
#
#         if params != '':
#             return Circle(float(params))
#
#         else:
#             return None
#
#     elif user_figure == 'Triangle':
#         params = input('введіть 3 cторони трикутника через кому - ) ').strip()
#
#         if params != '':
#             params_list = params.split(',')
#             return Triangle(float(params_list[0]), float(params_list[1]),float(params_list[2]))
#
#         else:
#             return None
#     else:
#         return None
#
#
# figures_list  = []
# for _ in range(3):
#
#     figura = create_figure()
#     if figura:
#         figures_list.append(figura)
#
# for  figur in figures_list:
#      print(figur.get_perimeter())
#      figur.display_info()

# Завдання 2
# Створіть наступні класи:
#  Manager – атрибути name, base_salary
#  Developer – атрибути name, base_salary, work_experience
#  Inter – атрибути name, base_salary
# Методи:
#  get_salary() – менеджер отримує базову ставку,
# розробник отримує на 20% більше якщо стаж більше 4
# років, інтерн отримує половину базової ставки
# Напишіть функцію create_worker() яка запитує у
# користувача тип працівника та потрібні атрибути і повертає
# об’єкт.
# Створіть декілька співробітників, добавте їх у список та для
# кожного викличте відповідні методи.

# Завдання 3
# Створіть наступні класи:
#  Car – атрибути speed
#  Bicycle – атрибути speed
#  Boat – атрибути speed
# Методи:
#  move() – виводить повідомлення про рух
# o Car – їде по шосе зі швидкістю
# o Bicycle – їде по дорозі зі швидкістю
# o Boat – пливе по воді зі швидкістю
#  check_speed(speed) – перевіряє чи правильна швидкість,
# якщо ні то в __init__ треба викикати ValueError з
# відповідним повідомленням
# o Car – від 20 до 200
# o Bicycle – від 10 до 30
# o Boat – від 0 до 50
# Напишіть функцію create_vehicle() яка запитує у
# користувача тип транспорту та потрібні атрибути і повертає
# об’єкт.
# Створіть декілька транспортних засобів, добавте їх у список
# та для кожної викличте відповідні методи.
# import typing
#
#
# class Car:
#     def __init__(self, speed):
#         self.speed = speed
#         self.check_speed()
#
#     def move(self):
#         print(f'їде по шосе зі швидкістю: {self.speed} км/год')
#
#     def check_speed(self):
#         if self.speed < 20 or self.speed > 200:
#             raise  ValueError('Car – від 20 до 200')
#
#
# class Bicycle:
#     def __init__(self, speed):
#         self.speed = speed
#         self.check_speed()
#
#     def move(self):
#         print(f'їде по дорозі зі швидкістю: {self.speed} км/год')
#
#     def check_speed(self):
#         if self.speed < 10 or self.speed > 30:
#             raise ValueError('Bicycle – від 10 до 30')
#
#
# class Boat:
#     def __init__(self, speed):
#         self.speed = speed
#         self.check_speed()
#
#     def move(self):
#         print(f'пливе по воді зі швидкістю: {self.speed} км/год')
#
#     def check_speed(self):
#         if self.speed < 0 or self.speed > 50:
#             raise ValueError('Boat – від 0 до 50')
#
#
# def create_vehicle():
#     user_choise = int(input('оберіть траспортний засіб де Car(1) Bicycle(2) Boat(3) '))
#
#     if user_choise == 1:
#         try:
#             speed = int(input('введіть швидкість - км/год'))
#
#             car = Car(speed)
#             return  car
#         except ValueError as err:
#             print(f'ви ввели не правильно шивдість {err}')
#             return None
#
#     elif user_choise == 2:
#         try:
#             speed = int(input('введіть швидкість - км/год'))
#
#             bicycle = Bicycle(speed)
#
#             return  bicycle
#         except ValueError as err:
#             print(f'ви ввели не правильно шивдість {err}')
#             return None
#
#     elif user_choise == 3:
#         try:
#             speed = int(input('введіть швидкість - км/год'))
#
#             boat = Boat(speed)
#
#             return boat
#         except ValueError as err:
#             print(f'ви ввели не правильно шивдість {err}')
#             return None
#
#     else:
#         print("Виберіть правильну команду")
#         return None
#
#
# vechiles: typing.List[Car | Bicycle | Boat ] = []
#
# for _ in range(3):
#     vechile = create_vehicle()
#     if vechile is not None:
#         vechiles.append(vechile)
#
# for vechile in vechiles:
#     print(type(vechile))
#     vechile.move()


import  typing



class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(f'product  {self.name} ціна - {self.price}')


class Customer:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, total):
        self.balance += total

    def withdraw(self, total):
        self.balance -= total


class Cart:
    def __init__(self,owner: Customer, items: typing.List[Product]):
        self.owner = owner
        self.items = items

    def add_product(self, product: Product):
          self.items.append(product)

    def checkout(self):
        for product in self.items:
            price = product.price
            self.owner.withdraw(price)

        self.items = []

    def show(self):
        total = 0
        for product in self.items:
            price = product.price
            total += price
            product.show()

        print(f'загальна вартість {total} грн')



# product = Product('milk', 70)

# product = {
#     "name": "milk",
#     "price": 70
# }

customer = Customer('Mary', 100)
product1 =  Product('milk', 70)
product2 = Product('bread', 30)

cart = Cart(customer, [product1, product2])

cart.checkout()

print(customer.balance)