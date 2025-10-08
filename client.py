# код для клієнета
# який спілкується з сервером
from http.client import responses

import requests

# # виклик функції message на сервері
# response = requests.post("http://localhost:8000/message")
# print(response.status_code)  # чи вдався запит(код 200)
#
# # виклик функції func на сервері
# requests.post("http://localhost:8000/function")

# # отримати дані від сервера
# num = 24
# response = requests.post(f"http://localhost:8000/mult2/{num}")
#
# # якщо запит успішний
# if response.ok:
#     # отримати відповідь від сервера у json форматі
#     data = response.json()
#     print(data)
# else:
#     #виникла помилка
#     print(response.text)

# передача параметрів як JSON

# user_data = {
#     'user_name': 'Jhon',
#     "login": "jhon45678",
#     'password': '123qwer',
#     'age': 45
# }
#
# response = requests.post("http://localhost:8000/register", json=user_data) #param dlya func on server
#
# import requests
#
#
# response = requests.post("http://localhost:8000/hello")
#
# if response.ok:
#     data = response.json()
#     print(data)
# else:
#     print(response.text)


# import requests
#
#
# response = requests.get("http://localhost:8000/greeting")
#
# if response.ok:
#     data = response.json()
#     print(data)
# else:
#     print(response.text)
#
# response = requests.get("http://localhost:8001/greeting")
#
# if response.ok:
#     data = response.json()
#     print(data)
# else:
#     print(response.text)

# name = 'Nikita'
# response = requests.post(f'http://localhost:8000/hello/{name}')
# print(response.json())
#
#
#
# name_data  ={
#     'name':'Nikita'
# }
# response1 = requests.post(f'http://localhost:8000/hello_json/',json=name_data)
# print(response1.json())


while True:
    user_choice = input('Choose options\n to get all books  press(1)\nTo add new book press(2)').strip()

    if user_choice == '1':
        response = requests.get('http://localhost:8000/books')

        if response.ok:
            data = response.json()

            print(data)
        else:
            print(response.text)

    elif user_choice == '2':
        book_id = int(input('please enter book id:'))
        book_title = input('Please enter book\'s title: ').strip()
        book_author = input('Please enter book\'s author: ').strip()
        book_year = int(input('Please enter book\'s year: ').strip())
        book_pages = int(input('Please enter book\'s pages quantity: ').strip())

        new_book ={
            'id': book_id,
            'title': book_title,
            "author": book_author,
            'year': book_year,
            'pages': book_pages
        }

        response = requests.get('http://localhost:8000/books')
        if response.ok:
            print("Book is added")
        else:
            print(response.text)
