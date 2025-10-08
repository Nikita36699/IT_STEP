# Завдання 1
# Напишіть сервер для збереження даних про фільми.
# Дані знаходяться у файлі films.json
# Напишіть модель на pydentic з такими даними:
# ● id
# ● title
# ● director
# ● year
# Функціонал:
# 1. Отримання даних за ID фільму
# ○ шлях – movies/{movie_id}
# ○ метод – GET
# 2. Додавання нового фільму
# ○ шлях – movies
# ○ метод – POST
# 3. Видалення фільму за ID
# ○ шлях – movies/{movie_id}
# ○ метод – DELETE
# Запустіть сервер
# Напишіть клієнта з таким фуннкціоналом для
# користувача:
# ● отримати дані про фільм
# ● додати новий фільм
# ● видалити фільм
from fastapi import FastAPI
from pydantic import BaseModel
import json
import os

app = FastAPI()
FILE = 'films.json'

class Film(BaseModel):
    id: int
    title: str
    director: str
    year: int

# если файла нет — создать пустой словарь
if not os.path.exists(FILE):
    with open(FILE, 'w', encoding='utf-8') as f:
        json.dump({}, f, ensure_ascii=False)

@app.get('/movies/{movie_id}')
def get_movie(movie_id: int):
    with open(FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data.get(str(movie_id), {'message': 'фильм не найден'})

@app.post('/movies')
def add_movie(film: Film):
    with open(FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    data[str(film.id)] = film.dict()
    with open(FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    return {"message": "Фильм добавлен", "film": film.dict()}

@app.delete('/movies/{movie_id}')
def delete_movie(movie_id: int):
    with open(FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if str(movie_id) in data:
        del data[str(movie_id)]
        with open(FILE, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        return {'message': 'фильм удалён'}
    return {'message': 'фильм не найден'}