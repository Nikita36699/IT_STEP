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


