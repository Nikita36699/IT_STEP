# # формат JSON(словники)
#
# # data = {
# #     "name": "Anton",
# #     "age": 23
# # }
# #
# # data['age']
#
# user1_name = 'Jhon'
# user1_data = {
#     'wins': 4,
#     'loses': 2
# }
#
# user2_name = 'Mary'
# user2_data = {
#     'wins': 6,
#     'loses': 0
# }
#
# user3_name = 'Mike'
# user3_data = {
#     'wins': 1,
#     'loses': 5
# }
#
# data = [
#     {
#         'name': 'Jhon',
#         'game_results': {
#             'wins': 4,
#             'loses': 2
#         }
#     },
#
#     {
#         'name': 'Mary',
#         'game_results': {
#             'wins': 6,
#             'loses': 0
#         }
#     }
# ]
#
# # отримати кількість перемог  для гравця з індексом 0
# print(data[0]['game_results']['wins'])
#
# data = {
#   "gt_parse": {
#     "menu": [
#       {
#         "nm": "Nasi Campur Bali",
#         "cnt": "1 x",
#         "price": "75,000"
#       },
#       {
#         "nm": "Bbk Bengil Nasi",
#         "cnt": "1 x",
#         "price": "125,000"
#       },
#       {
#         "nm": "MilkShake Starwb",
#         "cnt": "1 x",
#         "price": "37,000"
#       },
#       {
#         "nm": "Ice Lemon Tea",
#         "cnt": "1 x",
#         "price": "24,000"
#       },
#       {
#         "nm": "Nasi Ayam Dewata",
#         "cnt": "1 x",
#         "price": "70,000"
#       },
#       {
#         "nm": "Free Ice Tea",
#         "cnt": "3 x",
#         "price": "0"
#       },
#       {
#         "nm": "Organic Green Sa",
#         "cnt": "1 x",
#         "price": "65,000"
#       },
#       {
#         "nm": "Ice Tea",
#         "cnt": "1 x",
#         "price": "18,000"
#       },
#       {
#         "nm": "Ice Orange",
#         "cnt": "1 x",
#         "price": "29,000"
#       },
#       {
#         "nm": "Ayam Suir Bali",
#         "cnt": "1 x",
#         "price": "85,000"
#       },
#       {
#         "nm": "Tahu Goreng",
#         "cnt": "2 x",
#         "price": "36,000"
#       },
#       {
#         "nm": "Tempe Goreng",
#         "cnt": "2 x",
#         "price": "36,000"
#       },
#       {
#         "nm": "Tahu Telor Asin",
#         "cnt": "1 x",
#         "price": "40,000."
#       },
#       {
#         "nm": "Nasi Goreng Samb",
#         "cnt": "1 x",
#         "price": "70,000"
#       },
#       {
#         "nm": "Bbk Panggang Sam",
#         "cnt": "3 x",
#         "price": "366,000"
#       },
#       {
#         "nm": "Ayam Sambal Hija",
#         "cnt": "1 x",
#         "price": "92,000"
#       },
#       {
#         "nm": "Hot Tea",
#         "cnt": "2 x",
#         "price": "44,000"
#       },
#       {
#         "nm": "Ice Kopi",
#         "cnt": "1 x",
#         "price": "32,000"
#       },
#       {
#         "nm": "Tahu Telor Asin",
#         "cnt": "1 x",
#         "price": "40,000"
#       },
#       {
#         "nm": "Free Ice Tea",
#         "cnt": "1 x",
#         "price": "0"
#       },
#       {
#         "nm": "Bebek Street",
#         "cnt": "1 x",
#         "price": "44,000"
#       },
#       {
#         "nm": "Ice Tea Tawar",
#         "cnt": "1 x",
#         "price": "18,000"
#       }
#     ],
#     "sub_total": {
#       "subtotal_price": "1,346,000",
#       "service_price": "100,950",
#       "tax_price": "144,695",
#       "etc": "-45"
#     },
#     "total": {
#       "total_price": "1,591,600"
#     }
#   },
#   "meta": {
#     "version": "2.0.0",
#     "split": "train",
#     "image_id": 0,
#     "image_size": {
#       "width": 864,
#       "height": 1296
#     }
#   }
# }
#
# # отримати список ключів
# print(list(data.keys()))
#
# # отриати дані парсингу
# parse_data = data['gt_parse']
#
# print(list(parse_data.keys()))
#
# # дані про зігільну ціну
# sub_total_data = parse_data['sub_total']
#
# print(list(sub_total_data.keys()))
#
# # податки
# print(sub_total_data['tax_price'])
#
# # теж саме але одразу
# print(data['gt_parse']['sub_total']['tax_price'])
#
# # pydantic

# pickle
# import json
#
#
# data = {
#     'name': 'Sophie',
#     'age': 42
# }
#
# with open('data.json', 'w') as file:
#     json.dump(data, file)
#
#
# with open('data.json', 'r') as file:
#     new_data = json.load(file)
#
#
# print(new_data)
#
#
# # дані зберігаються як str рядки
# encoded = json.dumps(data)
# print(encoded)
# print(type(encoded))


#pickle зберігання даних як байти

import pickle


# data = {
#     'name': 'Sophie',
#     'age': 42
# }
#
# encoded = pickle.dumps(data)
# print(data)
# print(encoded)
# print(type(encoded))
#
#
# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# person = Person('Jhon', 35)
# encoded = pickle.dumps(person)
# print(person)
# print(encoded)
# print(type(encoded))

# робота з файлами
import json
#
#
# data = {
#     'name': 'Sophie',
#     'age': 42
# }
#
# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def info(self):
#         print(f"Person: {self.name}, {self.age} yr")
#
# person = Person('Mike', 16)
#
#
#
# with open('data.pkl', 'wb') as file:
#     pickle.dump(person, file)
#
#
# with open('data.pkl', 'rb') as file:
#     new_data = pickle.load(file)
#
#
# print(new_data.info())

# Завдання 1
# Напишіть програму для заповнення списку товарів. Назви товарів вводить користувач. Реалізуйте функціонал:
#  додати новий товар
#  вивести список товарів
#  зберегти дані через json
#  зберегти дані через pickle
#  завантажити дані через json
#  завантажити дані через pickle
# Завдання 1
#===================================================================================================
# Напишіть програму для заповнення списку товарів.
# Назви товарів вводить користувач.
# Реалізуйте функціонал:
# додати новий товар
# вивести список товарів
# зберегти дані через json
# зберегти дані через pickle
# завантажити дані через json
# завантажити дані через pickle
import json
import pickle
import os


class Cart:
    def __init__(self, user_name):
        self.user_name = user_name
        self.items = []

    def add_item(self):
        item_name = input("Enter product name: ")
        item_price = float(input("Enter product price: "))
        item_brand = input("Enter product brand: ")

        item_data = {
            "name": item_name,
            "price": item_price,
            "brand": item_brand,
        }

        self.items.append(item_data)

    def show_cart(self):
        print(f"{self.user_name}'s products")

        for item in self.items:
            print(f"\tProduct data")
            print(f"\t Name: {item["name"]}")
            print(f"\t Price: {item["price"]}")
            print(f"\t Brand: {item["brand"]}")

    def save_data_json(self):
        # read exist data
        if os.path.exists("products.json"):
            with open("products.json", "r", encoding="utf-8") as file:
                users_data = json.load(file)

        # File products.json doesn't exist (first saving)
        else:
            users_data = {}

        users_data[self.user_name] = self.items

        with open("products.json", "w", encoding="utf-8") as file:
            json.dump(users_data, file, indent=4)

    def save_data_pickle(self):
        # read exist data
        if os.path.exists("products.pkl"):
            with open("products.pkl", "rb") as file:
                users_data = pickle.load(file)

        # File products.json doesn't exist (first saving)
        else:
            users_data = {}

        users_data[self.user_name] = self.items

        with open("products.pkl", "wb") as file:
            pickle.dump(users_data, file)

    def load_data_json(self):
        with open("products.json", "r", encoding="utf-8") as file:
            users_data = json.load(file)

            if self.user_name in users_data:
                self.items = users_data[self.user_name]

            else:
                self.items = []

    def load_data_pickle(self):
        with open("products.pkl", "rb") as file:
            users_data = pickle.load(file)
            self.items = users_data[self.user_name]


# Tests
cart1 = Cart("John")
cart1.add_item()
cart1.add_item()

cart1.show_cart()

cart1.save_data_json()
cart1.save_data_pickle()

cart1.load_data_json()
cart1.load_data_pickle()

cart1.show_cart()

cart2 = Cart("Maria")
cart2.add_item()
cart2.add_item()

cart2.show_cart()

cart2.save_data_json()
cart2.save_data_pickle()

cart2.load_data_json()
cart2.load_data_pickle()

cart2.show_cart()

# Завдання 2
#===================================================================================================
# Напишіть клас Student
# Атрибути:
# name – ім’я
# specialization – спеціалізація
# grades – список оцінок
# Методи:
# add_grade(grade) – додати нову оцінку
# show_info() – вивести ім’я, спеціалізацію та середню
# оцінку
# Практичне завдання
# Створіть список з трьох студентів. Збережіть цей список
# використовуючи pickle та json.
# Завантажте дані за допомогою pickle та json.

import json
import pickle
import os


class Student:
    def __init__(self, name: str, specialization: str):
        if name.isalpha() and specialization:
            self.name = name.capitalize().strip()
            self.specialization = specialization.capitalize().strip()
            self.grades = []
            print('New student added.\n')
        else:
            raise ValueError('Please enter student\'s name with letters.')

    def add_grade(self, grade: int):
        if isinstance(grade, int):
            self.grades.append(grade)
            print('New grade was added.\n')
        else:
            raise ValueError('Please enter digit as a grade\'s value.')

    def display_info(self):
        avg_grade = sum(self.grades) / len(self.grades)
        print(f'Name: {self.name}, specialization: {self.specialization}, average grade: {avg_grade:.1f}')

    def save_json(self):
        file_name = self._get_json_file_name()

        json_data = {
            'specialization': self.specialization,
            'grades': self.grades
        }

        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=4, ensure_ascii=False)

        print(f'Data saved to {file_name}')

    def _get_json_file_name(self):
        return f'student_data_{self.name}.json'

    def load_from_json(self):
        file_name = self._get_json_file_name()

        if os.path.exists(file_name):
            with open(file_name, 'r', encoding='utf-8') as f:
                data = json.load(f)
        else:
            print('No student was added to database.\n')
            return

        self.specialization = data['specialization']
        self.grades = data['grades']

        print('Student was upgraded.\n')


student = Student('Vlad', 'L4B')
student.add_grade(5)
student.add_grade(4)
student.add_grade(2)

student1 = Student('Liza', 'Cosmetology')
student1.add_grade(5)
student1.add_grade(4)
student1.add_grade(4)

student2 = Student('Ann', 'Economics')
student2.add_grade(5)
student2.add_grade(5)
student2.add_grade(5)

students = [student, student1, student2]

for student in students:
    student.load_from_json()
    student.display_info()

student1.display_info()
student2.display_info()

with open('students.pkl', 'wb') as f:
    pickle.dump(students, f)


with open('students.pkl', 'rb') as f:
    data = pickle.load(f)


for student in data:
    student.display_info()


with open('students.json', 'w', encoding='utf-8') as f:
    json.dump(students, f, indent=4, ensure_ascii=False)

