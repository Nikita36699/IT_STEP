import requests

while True:
    print('\n1 - получить фильм')
    print('2 - добавить фильм')
    print('3 - удалить фильм')
    print('4 - выход')

    choice = input('выбери пункт: ')

    if choice == '1':
        movie_id = input('введи id фильма: ')
        print(requests.get(f'http://localhost:8000/movies{movie_id}').json())

    elif choice == '2':
        film = {
            'id': int(input('id: ')),
            'title': input('название: '),
            'director': input('режиссер: '),
            'year': int(input('год: '))
        }
        print(requests.post('http://localhost:8000/movies', json=film).json())

    elif choice == '3':
        movie_id = input('введи id фильма для удаления: ')
        print(requests.delete(f'http://localhost:8000/movies{movie_id}').json())

    elif choice == '4':
        break

    else:
        print('нет такого варианта')



