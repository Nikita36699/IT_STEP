# серверне програмування

# https://www.google.com/search&q=java
#
#
# from fastapi import FastAPI
#
#
# # застосонук для сервера
# # допомагає позначити як отримати доступ до окремих функцій на сервері
#
# # коли робитиметься виклик до серверра
# # http:our_ip/шлях до функції
# app = FastAPI()
#
# # створення функцій
# @app.post('/message')
# def message():
#     print("виклик функції message")
#
#
# @app.post('/function')
# def func():
#     print("Виклик функції func")
#
#
# # функція яка повертає результат
# # формат Json
#
# # @app.post("/data")
# # def get_data():
# #     return {"result": "Привіт від сервера"}
#
#
# # передача параметрів
# # параметри як чатина шляху
# # як правило працює для одного параметра
#
# @app.post("/mult2/{num}")
# def mult2(num: int):
#     result = 2 * num
#     return {'result': result}
#
#
# # функція для реєстрації користувачів
# # отримує щось типу
# {
#     'user_name': 'Jhon',
#     "login": "jhon45678",
#     'password': '123qwer',
#     'age': 45
# }
#
# from pydantic import  BaseModel
#
# #pydanctic -- річ яка доаомогає в анотації json objects
#
# class UserData(BaseModel):
#     user_name: str
#     login: str
#     password: str
#     age: int
#
# @app.post("/register")
# def register_user(user: UserData):
#     print(user)
#     print(f'login: {user.login}')
#     results = {
#         'result': 'Дані отримано',
#         'user_data': user
#     }
#
#     return results

# # Тема: Мережеве програмування. Частина 2
# #===============================================================
# # Завдання 1
# # Напишіть сервер:
# # ● шлях – /hello
# # ● метод – POST
# # Функція має повертати JSON об’єкт {"message": "Привіт з сервера!"}
# # Запустіть сервер:
# # ● host – localhost
# # ● port – 8000
# # uvicorn main:app --port 8000 –host localhost --reload
# # Напишіть клієнта який робить запит на сервер
# # from fastapi import FastAPI
# #
# #
# # app = FastAPI()
#
# # @app.post("/hello")
# # def welcome():
# #     return {"message": "Привіт з сервера!"}
#
#
# # Завдання 2
# #===================================================
# # Напишіть сервер1:
# # ● шлях – /greeting
# # ● метод – GET
# # ● результат – {"respond": "Привіт з сервера1"}
# # ● порт – 8000
# # Напишіть сервер2:
# # ● шлях – /greeting
# # ● метод – GET
# # ● результат – {"respond": "Привіт з сервера2"}
# # ● порт – 8001
# # Запустіть обида сервери на localhost
# # Напишіть клієнта який робить запита на обидва сервери
# from fastapi import FastAPI
#
#
# app = FastAPI()
#
# @app.get("/greeting")
# def hi():
#     return {"respond": "Привіт з сервера1"}


#from fastapi import FastAPI
# from pydantic import BaseModel
#
# app = FastAPI()
#
# @app.post("/hello/{name}")
# def hello(name: str):
#     return {"message": f"Привіт, {name}!"}
#
# class NameData(BaseModel):
#     name: str
#
#
# @app.post('hello_json')
# def hello_json(name_data: NameData):
#     name = name_data.name
#     return {"message": f"Привіт, {name}!"}
#
# Завдання 4
# Напишіть сервер для симуляції роботи бібліотеки.
# Дані про книги знаходяться у файлі books.json
# Напишіть модель на pydentic для книги з такими даними:
# ● id
# ● title
# ● author
# ● year
# ● pages
# Функціонал:
# 1. Отримання всіх книг
# ○ шлях – books
# ○ метод – GET
# 2. Отримання даних за ID книги
# ○ шлях – books/{book_id}
# ○ метод – GET
# 3. Додавання нової книги
# ○ шлях – books
# ○ метод – POST
# 4. Видалення книги за ID
# ○ шлях – books/{book_id}
# ○ метод – DELETE
# from fastapi import FastAPI
# from pydantic import BaseModel
# import  json
#
# app = FastAPI()
#
# class Book(BaseModel):
#     id: int
#     title: str
#     author: str
#     year: int
#     pages: int
#
# @app.get('/books')
# def get_all_books(filename='books.json'):
#     with open(filename, 'r', encoding='utf-8') as f:
#         data = json.load(f)
#
#     return data
#
# @app.post('/books')
# def add_new(book_json: Book, filename='books.json'):
#     with open(filename, 'r', encoding='utf-8') as f:
#         data = json.load(f)
#
#     data[book_json] = book_json
#
#     with open(filename, 'w',) as f:
#         json.dump(data, f, indent=4)

