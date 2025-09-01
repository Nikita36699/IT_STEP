# # магічні методи
#
# nums = [1, 2, 3, 4]
#
# #явний метод(звичайний)
# nums.append(5)
#
# # магічний  метод(викликається не явно(без прямої назви))
# 10 in nums
# nums.__contains__(10)
#
# # num1 = 10
# #
# # num1 + 5
# # res = num1.__add__(5)
# # print(res)
#
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self): # заміняє операцію str(self)
#         return  f'{self.name}, {self.age} years'
#
#     def __eq__(self, other):#self == other
#         if isinstance(other, Person):
#             return  self.name  == other.name  and self.age == other.age
#
#         elif isinstance(other, str):
#             return  self.name == other
#
#         else:
#             return False
#
#
#     def __gt__(self, other): #self > other
#        if isinstance(other, Person):
#             return  self.age > other.age
#
#        else:
#            return  False
#
#     # def __lt__(self, other):# self < other
#     #     pass
#
#     def grow(self):
#         self.age += 1
#
#
# #метод __init__
# person1 = Person("Jhon",37)
# person2 = Person("Sophie", 40)
#
#
# #__str__
# print(person1)
#
# info = str(person2)
# print(info)
#
# #__eq__
# print(person1 == person2)
#
# # person3 = Person("Sophie", 40)
# # print(person3 == person2)
#
# print(person1 == "Jhon")
#
# # user = "Jhon"#(mistake other type of data)
# # user.name#(mistake)
#
# #__gt__
# if person1 > person2:
#     print(f'{person1} older then {person2} ')
# else:
#     print(f'{person2} older then {person1}')
#
# person3 = Person("Mike", 21)
#
# people = [person1, person2, person3]
#
# #отримати найстаршу люидну
# max_person = max(people)
#
# print(f"Найстарша людина: {max_person}")
#
# min_person = min(people)
#
# print(f'Наймолодша людина {min_person}')
#
#
#
# class Cart:
#     def __init__(self):
#         self.items = []
#
#     def add_item(self,item):
#         self.items.append(item)
#
#     def __str__(self):
#         return f"Cart with {self.items}"
#
#     def __contains__(self, item): # item in self
#         return item in self.items
#
#     def __getitem__(self, index): # self[index}
#         return  self.items[index]
#
#     def __len__(self): #len(self)
#         return  len(self.items)
#
#     def  generator(self):
#         for item in self.items:
#             yield  item
#
#     def __iter__(self):
#         return  iter(self.items)
#
#
#
#
# cart = Cart()
#
# cart.add_item("Milk")
# cart.add_item("Bread")
# cart.add_item("Butter")
#
# print(cart)
#
# # item in cart
# print('Milk' in cart)
# print('milk' in cart)
#
# # cart[2]
# print(cart[1])
#
#
# # len(cart)
#
# print(len(cart))
#
#
#
# # for item in cart:
# #usual fucntion
# # def func(param):
# #     res = param + 2
# #
# #     return  res
# #
# # # функція з багатьма резульаьами(генератор)
# # def power2(n):
# #     for k in range(n):
# #         yield 2**k # повертає результат для for i працюе далі
# #
# # #призив функціі у циклі и це виводить степені двійки
# # for num in power2(10):
# #     print(num)
#
#
# print(cart) #str(cart)
#
#
# # for item in cart:
# # for item in cart.generator(): #iter(cart)
# #     print(item)
#
# for item in cart:#iter(cart)(СДЕЛАНО БЛАГОДАРЯ МАГ МЕТОД __iter__)
#     print(item)

####PRACTICAL####
#  Завдання 1
# Створіть клас Message з атрибутами
#  user – ім’я автора повідомлення
#  text – текст повідомлення
#  time – час повідомлення(використайте модуль datetime)
# приклад datetime.strptime('10:23', '%H:%M')
# методи:
#  __str__(self) – повертає текст повідомлення та час
#  __len__(self)  – повертає довжину повідомлення
#  __gt__(self, other)  – перевіряє чи є повідомлення self
# старішим за other
# Створіть список з декількома повідомленнями та виведіть
# його. Відсортуйте список і знову виведіть
# import datetime
# import time
#
# class Message:
#     def __init__(self, user: str, text: str):
#         self.user = user
#         self.text = text
#         self.time = datetime.datetime.now()
#
#     def __str__(self):
#         return f'Time: {self.time.strftime('%H:%M:%S')}, user: {self.user}, message: "{self.text}"'
#
#     def __len__(self):
#         return len(self.text)
#
#     def __gt__(self, other):
#         if isinstance(other, Message):
#             return self.time > other.time
#         else:
#             raise TypeError(f'Нельзя сравнить > типа Message с типом {type(other)}')
#
#
# mess1 = Message('Vlad', "Hello")
# print(mess1)
# print(len(mess1))
#
# time.sleep(2)
#
# mess2 = Message('Liza', 'Poka')
# print(mess2)
#
# print(mess1 > mess2)
#
# time.sleep(2)
#
# mess3 = Message('Olena', 'Wassup')
#
# messes = [mess3, mess1, mess2]
#
# earliest_mess = min(messes)
#
# print(earliest_mess)
#
# sorted_messes = sorted(messes)
#
# for mess in sorted_messes:
#     print(mess)

# Завдання 2
# Створіть клас Song з атрибутами
#  name – назва пісні
#  author – ім’я автора
# методи:
#  __eq__(self, other) – перевіряє чи дві пісні однакові
#  __str__(self, other) – повертає рядок з назвою та автором
# Створіть клас Playlist з атрибутами
#  songs – список пісень(об’єкти класу Song)
# методи:
#   __len__(self)  – повертає кількість пісень
#  __contains__(self, item) – перевіряє чи є пісня в плейлисті
#  __iter__(self) – повертає літератор для циклу for
#  add_song(self, song) – додає пісню в плейлист
#  remove_song(self, song) – видаляє пісню з плейлиста
# Створіть порожній плейлист
# Створіть 3 пісні:
# "Imagine", "John Lennon"
# "Bohemian Rhapsody", "Queen"
# "Shape of You", "Ed Sheeran"
# Добавте їх в плейлист
# Пройдіться циклом for по плейлисту та виведіть кожну
# пісню на екран
class Song:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __eq__(self, other):
        return  self.name == other.name and self.author == other.author

    def __str__(self):
        return  f'{self.name} -- {self.author}'


class Playlist:
    def __init__(self):
        self.songs = []

    def __len__(self):
        return  len(self.songs)

    def __contains__(self, item):
        return  item in self.songs

    def __iter__(self):
        return  iter(self.songs)

    def add_song(self, song):
        if song not in self.songs:
            self.songs.append(song)

    def delete_song(self,song):
        if song in self.songs:
            self.songs.remove(song)


playlist = Playlist()

song1 = Song('Imagine', 'John Lennon')
song2 = Song('in the end ', 'Linkin Park' )
song3 = Song("billie eilish", 'chihiro')

playlist.add_song(song1)
playlist.add_song(song2)
playlist.add_song(song3)

for song in playlist:
    print(song)

if song1 in playlist:
    print(f"{song1} in Playlist")

