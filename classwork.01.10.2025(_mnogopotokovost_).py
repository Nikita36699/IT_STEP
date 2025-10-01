# # дз
#
# def add_album(bands: dict, band: str, album: str) -> None:
#     """Додати новий альбом до гурту."""
#     if band not in bands:
#         print(f"Гурт '{band}' не знайдено!")
#         return
#
#     if album in bands[band]:
#         print(f"Альбом '{album}' вже є у гурта '{band}'!")
#         return
#
#     bands[band].append(album)
#
#
# text = '   \n  '
# # text.strip() == ''
# import threading
# import time


# # багато потоковість
# import time
#
#
# def func1():
#     print("Початок функції 1")
#     time.sleep(0.5)
#     total = 0
#     for num  in range(1, 1000):
#         total += num
#
#     print(total)
#     print("Кінець функції 1")
#
#
# def func2():
#     print("Початок функції 2")
#     time.sleep(0.5)
#     count15 = 0
#     for num in range(1, 1000):
#         if num % 15:
#             count15 += 1
#
#     print(count15)
#     print("Кінець функції 2")
#
#
# # без потоків
# start = time.time()
# func1()
# func2()
# end = time.time()
#
# print(f"Час без потоків -- {end - start} сек")
# print()
#
#
# # з потоками
#
# import threading
#
# # потік для функції 1
# thread1 = threading.Thread(target=func1)
#
# # потік для функції 2
# thread2 = threading.Thread(target=func2)
#
# # запуск потоків
# start = time.time()
# thread1.start()
# thread2.start()
#
# # дочекатись  закінчення потоків
# thread1.join()
# thread2.join()
#
# end = time.time()
#
# print(f"Час з потоками -- {end - start} сек")


# # функції з параметрами
# def func1(text, num):
#     for _ in range(num):
#         print(text + '\n', end='')
#
#
# def func2(nums):
#     print(f"{sorted(nums)}\n", end='')
#
#
# nums = [1, 4, 3, 2, 5, 3, 5, 3, 4, 6, 4, 7, 8, 9, 0, 0]
#
# # потік для функції 1 з параметрами "hello" 20
# thread1 = threading.Thread(target=func1, args=("hello", 20))
#
# # потік для функції 2 з параметрами nums
# thread2 = threading.Thread(target=func2, args=(nums, ))
#
# # потік для функції 1 у форматі func1('long text', num=10)
# thread3 = threading.Thread(target=func1,
#                            args=("long text",),
#                            kwargs={"num": 10}
#                            )
#
# thread1.start()
# thread2.start()
# thread3.start()


# є список задач, які виконують декілька потоків
# результати треба записати у спільний файл
# from threading import Lock
#
# locker = Lock()
#
#
# def do_task(tasks, thread_num, locker):
#     while True:
#         # кажемо іншим потокам зупинитися
#         locker.acquire()
#
#         if not tasks:
#             print(f"Потік{thread_num} закінчив роботу")
#             return
#
#         task = tasks.pop()
#
#         with open("logging.txt", 'a', encoding='utf-8') as file:
#             print(f"Потік{thread_num} виконав задачу {task}", file=file)
#
#         # інші потоки можуть продовжувати
#         locker.release()
#
#
# tasks = list(range(1, 10))
#
# threads = []
# for i in range(20):
#     thread = threading.Thread(target=do_task, args=(tasks, i, locker))
#     threads.append(thread)
#
# for thread in threads:
#     thread.start()
# Завдання 1
# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік знахо-
# дить максимум у списку. Другий потік знаходить мінімум
# у списку. Результати обчислень виведіть на екран.
# import  threading
#
#
# def maximum(nums: list, results: dict):
#     print('Function maximum started working')
#     result = max(nums)
#     results['maximum'] = result
#     print('function maximum ended work')
#     return  result
#
#
# def minimum(nums: list, results: dict):
#     print('Function minimum started working')
#     result = min(nums)
#     results['minimum'] = result
#     print('function minimum ended work')
#     return result
#

# def get_nums():
#     nums = []
#     while True:
#         num = (input("add nums to list or enter to finish"))
#         if  num == '':
#             return  nums
#
#         nums.append(int(num))
#
#
# results = {}
# my_nums = get_nums()
# thread1  = threading.Thread(target=maximum, args=(my_nums, results))
# thread2  = threading.Thread(target=minimum, args=(my_nums, results ))
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
#
# print(results)



#Завдання 2
# Користувач вводить з клавіатури значення у список.
# Після чого запускаються два потоки. Перший потік зна-
# ходить суму елементів у списку. Другий потік знаходить
# середнє арифметичне у списку. Результати обчислень
# виведіть на екран.
# import  threading
# import  time
#
# def sum_nums(nums: list, results: dict):
#     print('Function summ started working')
#
#     result = sum(nums)
#     results['summa'] = result
#
#     time.sleep(0.5)
#
#     print('function summ ended work')
#     return  result
#
#
# def avg_nums(nums: list, results: dict):
#     print('Function avg started working')
#
#     result = sum(nums) / len(nums)
#     results['average_num'] = result
#
#     time.sleep(0.5)
#
#     print('function avg ended work')
#     return result
#
#
# def get_nums():
#     nums = []
#     while True:
#         num = (input("add nums to list or  enter to finish"))
#         if  num == '':
#             return  nums
#
#         nums.append(int(num))
#
#
# results = {}
# my_nums = get_nums()
# thread1  = threading.Thread(target=sum_nums, args=(my_nums, results))
# thread2  = threading.Thread(target=avg_nums, args=(my_nums, results ))
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
#
# print(results)

# Завдання 3
# Користувач вводить з клавіатури шлях до файлу, що
# містить набір чисел. Після чого запускаються два потоки.
# Перший потік створює новий файл, в який запише лише
# парні елементи списку. Другий потік створює новий файл,
# в який запише лише непарні елементи списку. Кількість
# парних і непарних елементів виводиться на екран.
# import random
# import threading
# import json
#
# nums = []
# for _ in range(1_000_000):
#     random_num = random.randint(1, 100)
#     nums.append(random_num)
#
# with open(file='nums.json', mode='w') as file:
#     json.dump(nums, file)

import threading
import json
import  os
from fileinput import filename


def get_user_way():
    while True:
        filename = input('Дайте шлях до файлу')

        if not os.path.exists(filename):
            print('Такого файла не існує')
            continue

        if  not filename.endswith('.json'):
            print('Це не "JSON" файл')
            continue

        return  filename


def even_nums(filename):
    print('Start even')

    with open(filename, 'r') as f:
        nums = json.load(f)

    even = []
    for num in nums:
        if num % 2 == 0:
            even.append(num)

    new_file_name = filename[:-5]
    new_file_name += '_even.json'
    directory , filename1 = os.path.split(new_file_name)
    directory = os.path.join(directory, 'result')
    os.mkdir(directory)
    new_file_name = os.path.join(directory, filename1)
    print(new_file_name)
    print(filename)

    with open(new_file_name, 'w') as f:
        json.dump(even, f)

    print('End even')

def odd_nums(filename):
    print('Odd start')

    with open(filename, 'r') as f:
        nums = json.load(f)

    odd = []
    for num in nums:
        if num % 2 != 0:
            odd.append(num)

    new_file_name = filename.replace('.json', "_odd.json")
    directory, filename1 = os.path.split(new_file_name)
    directory = os.path.join(directory, 'result')
    os.mkdir(directory)
    new_file_name = os.path.join(directory, filename1)
    print(new_file_name)
    print(filename)

    with open(new_file_name, 'w') as f:
        json.dump(odd, f)

    print('Odd End ')

filename = get_user_way()
thread1 = threading.Thread(target=even_nums, args=(filename, ))
thread2 = threading.Thread(target=odd_nums, args=(filename, ))

thread1.start()
thread2.start()









# Завдання 4
# Користувач вводить з клавіатури шлях до файлу та
# слово для пошуку. Після чого запускається потік для
# пошуку цього слова у файлі. Результат пошуку виведіть
# на екран.