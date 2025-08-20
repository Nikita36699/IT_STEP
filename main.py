# class Dog:
#     def __init__(self,name,age,breed = 'labrador'):
#         #self -- це объебкт классу(конктретний песик)
#         print('Hello from Dog.__innit__')
#         #створення атрибуту name
#         self.name = name
#
#         self.age = age
#         self.breed = breed
#
#     def eat(self,food):
#         print(f'{self.name} is eating {food}')
#
#     def grow(self):
#         """
#         пес подорослішав на один рік
#         """
#         self.age += 1
#
#     def get_name(self):
#         return  self.name
#
# #створення кокретного пса
#
# dog1 = Dog(name='tuzik',age=5)
#
# print(dog1.name)
# print(dog1.age)
# print(dog1.breed)
#
# #створення іншого пса
#
# dog2 = Dog(name='barsik',age=2,breed='haski')
# print(dog2.name)
# print(dog2.age)
# print(dog2.breed)
#
# print()
#
# dog1.eat('bone')
# dog2.eat('meat')
#
# print()
#
# print(dog1.age )
# dog1.grow()
# print(dog1.age)
#
# print()
#
# name = dog1.get_name()
# print(name)
#
# #атрибути можна змінювати але не бажано
# dog = Dog(name='tuzik', age = 5)
# dog.age += 2
# dog.color = 'brown'

# #  Завдання 1
# # Створіть клас Student з атрибутами name та age. Додайте
# # метод для виводу інформації у форматі «Ім’я: {name}, вік:
# # {age}»
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def show_info(self):
#         print(f'hello {self.name},age: {self.age}')
#
#     def __str__(self):
#         return f"{self.name},{self.age}"
#
# # student1 = Student(name='Nikita', age=23)
# # student1.show_info()
# #
# # student2 = Student('John',20)
# # student2.show_info()
#
# # Завдання 2
# # Створіть список з 3-ма студентами, дані вводить
# # користувач. Після чого для кожного студента виведіть
# # інформацію про нього за допомогою метода.
# # student1_name = input('enter name: ')
# # student1_age = int(input('enter age: '))
# #
# # student1 = Student(student1_name, student1_age)
# #
# # student1.show_info()
#
# student_list = []
#
# for i in range(3):
#     student_name = input('enter name: ')
#     student_age = int(input('enter age: '))
#     student = Student(student_name, student_age)
#     student.show_info()
#     student_list.append(student)
#
#
# for student in student_list:
#     print(student)

# Завдання 3
# Створіть клас Circle з атрибутом radius. Додайте метод для
# отримання площі кола
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        pi = 3.14
        s = pi * (self.radius ** 2)

        return s

circle1 = Circle(radius=4)
circle2 = Circle(radius=5)

print(circle1.get_area())
print(circle2.get_area())


# Завдання 4
# Створіть клас BankAccount з атрибутами owner та balance.
# Додайте метод deposit для поповнення рахунку
# Додайте метод withdraw для зняття грошей з рахунку
# Додайте метод info для виведення інформації про баланс
class BankAccount:
    def __init__(self, balance,owner):
        self.balance = balance
        self.owner = owner


    def deposit(self,user_deposit):
        self.balance += user_deposit

        return self.balance


    def withdraw(self, user_withdraw):
        self.balance -= user_withdraw

        return self.balance


    def info(self):
        print(f'{self.owner} your balance {self.balance}')


user1 = input("введіть свое ім'я")
balance1 = int(input('введіть баланс:'))
account1 = BankAccount(balance=balance1,owner=user1)



account1.info()
account1.deposit(1000)
account1.info()


# Завдання 5
# Створіть клас Car з атрибутами brand(марка), year(рік
# випуску), is_ready(чи готовий до поїздки, за замовчування
# False).
# Додайте метод start_engine який заводить двигун, і змінює
# атрибут is_ready
# Додайте метод move який виводить повідомлення, що
# автомобіль їде, або ж ще не готовий в залежності від is_ready.
class Car:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
        self.is_ready = False

    def start_engine(self):
        self.is_ready = True
        print('двигун заведенно')

        return self.is_ready


    def move(self,distance):
        if not self.is_ready:
            print("цей автомобіль не заведенний і не можє їхати")
            return

        print(f"автомобіль проїхав - {distance} кілометрів ")

car = Car('BMW',2021)

car.move(10)

car.start_engine()

car.move(10)
