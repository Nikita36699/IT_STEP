# # Завдання 1
# # Створіть клас Проект з атрибутами:
# #  назва
# #  виділений кошторис
# #  загальні витрати
# #  чи завершений(за замовчуванням False)
# #  час виконання(за замовчуванням 0 місяців)
# #  список необхідних задач
# # Додайте методи:
# #  вивід інформації: назва, час виконання, необхідні
# # задачі
# #  добавити нову задачу
# #  розбити задачу на під-задачі: передається назва задачі
# # та список під-задач
# #  виконати задачу, передається назва, час та ціна
# # виконання
# #  поповнення кошторису
# #
# #
# #опис классу(шаблон який описує всі проекти)
# class Project:
#     def __init__(self, name, budget, tasks: list):
#         self.name  = name
#         self.budget = budget
#         self.tasks = tasks
#
#         self.expenses = 0
#         self.if_finished = False
#         self.time = 0
#
#     def show_info(self):
#         print()
#         print(f"інформація по проекту,{self.name}")
#         print(f'\t Бюджет -- {self.budget}.грн')
#         print(f"\t використано -- {self.expenses}/{self.budget}")
#         print(f"\t час виконання -- {self.time} місяців")
#
#         if self.if_finished:
#             print("\t Статус -- Завершений")
#         else:
#             print("\t Статус -- Не завершений")
#
#         print("\t список задач")
#         for task in self.tasks:
#             print(f'\t\t {task}')
#
#     def add_task(self, new_task):
#         self.tasks.append(new_task)
#         print(f'додано нове завдання {new_task}')
#
#     def created_subtasks(self,old_task, sub_tasks):
#         #чи є стара задачу и списку
#         if old_task not in self.tasks:
#             print(f"Такої задачі немає у списку")
#             return
#         # old_task in list
#
#         self.tasks.remove(old_task)
#         self.tasks.extend(sub_tasks) #добавити всі елементи з subtasks в список self.tasks
#
#     def do_task(self, task, price, time):
#         if  task not in self.tasks:
#             print(f'такої задачі немає в списку')
#             return
#
#         if price > self.budget - self.expenses:
#             print(f"Не вистачає коштів")
#             return
#
#         #все добре робимо задачу
#         self.tasks.remove(task)
#         self.expenses += price
#         self.time += time
#
#         self.if_finished = len(self.tasks) == 0
#
#     def deposit(self, price):
#         self.budget += price
#
#
#
# #створення конкретного проєкту
# project1 = Project('Making Film',10000, ['write plot', 'find actors'])
#
# # print(project1.tasks)
# # print(project1.if_finished)
#
# project1.show_info()
# project1.add_task('find location')
# project1.show_info()
# print(project1.tasks)
#
# project1.created_subtasks('talk with producer',sub_tasks= [])
#
# project1.created_subtasks('find actors', ['talk with actor 1', 'talk with actor 2'])
#
# project1.show_info()
#
# project1.do_task('talk with actor 1',1000,0.5)
# project1.show_info()
#
#
# project1.deposit(50000)
# project1.do_task('write plot',20000,3.5)
# project1.show_info()
from pyclbr import Class

# Завдання 2
# Створіть клас Телефон з атрибутами:
#  максимальний обсяг пам’яті
#  зайнята пам’ять
#  чи включений(за замовчуванням False)
#  встановлені додатки у вигляді словника, де ключ –
# назва додатку, значення – обсяг пам’яті
# Додайте методи:
#  вивести інформацію про використання пам’яті
#  видалити додаток
#  встановити новий додаток, якщо пам’яті достатньо
#  оновити додаток(нова версія може займати іншу
# кількість пам’яті)
#  запустити додаток, якщо він є і якщо телефон
# вкючений
#  включити телефон
#  виключити телефон

class Phone:
    def __init__(self, max_memory):
        self.max_memory = max_memory
        self.is_poweron = False
        self.used_memory = 0
        self.apps = {'YouTube': 1000, 'Google': 1000}
        self.used_memory = sum(self.apps.values())

    def show_mem_usage(self):
        print(f"Використано пам’яті: {self.used_memory} MB")
        print(f"Максимальний обсяг пам’яті: {self.max_memory} MB")
        print("Додатки: ")
        for app, mem in self.apps.items():
            print(f"\t{app} - {mem} MB")

    def delete_app(self, old_app):
        if old_app not in self.apps:
            print("Такого додатку немає")
            return
        self.used_memory -= self.apps[old_app]
        self.apps.pop(old_app)
        print(f"Додаток {old_app} видалено")

    def add_app(self, name_app, app_memory):
        if name_app in self.apps:
            print("Така програма вже встановлена")
            return
        if app_memory > self.max_memory - self.used_memory:
            print("Не вистачає пам’яті")
            return
        self.apps[name_app] = app_memory
        self.used_memory += app_memory
        print(f"Додаток {name_app} встановлено ({app_memory} MB)")

    def update_app(self, update_app, memory):
        if update_app not in self.apps:
            print("Такого додатку немає")
            return
        old_mem = self.apps[update_app]
        if self.used_memory - old_mem + memory > self.max_memory:
            print("Не вистачає пам’яті для оновлення")
            return
        self.used_memory = self.used_memory - old_mem + memory
        self.apps[update_app] = memory
        print(f"Додаток {update_app} оновлено ({memory} MB)")

    def run_app(self, app):
        if not self.is_poweron:
            print("Телефон вимкнено")
            return
        if app not in self.apps:
            print("Такого додатку не встановлено")
            return
        print(f"Запуск додатку {app}...")

    def turn_on_phone(self):
        if not self.is_poweron:
            self.is_poweron = True
            print("Телефон увімкнено")
        else:
            print("Телефон вже увімкнений")

    def turn_off_phone(self):
        if self.is_poweron:
            self.is_poweron = False
            print("Телефон вимкнено")
        else:
            print("Телефон вже вимкнений")



phone1 = Phone(max_memory=10000)

phone1.show_mem_usage()
phone1.delete_app('YouTube')
phone1.show_mem_usage()
phone1.add_app('TikTok', 2000)
phone1.show_mem_usage()
phone1.update_app('Google', 1500)
phone1.show_mem_usage()
phone1.turn_on_phone()
phone1.run_app('TikTok')
phone1.turn_off_phone()

# Завдання 3
# Створіть клас Автомобіль з атрибутами:
#  марка
#  пробіг
#  рівень пального
#  витрата пального(л/км)
#  чи є справним(за замовчуванням True)
# Реалізуйте методи:
#  проїхати певну відстань, має змінитись пробіг та рівень
# пального, якщо автомобіль справний та достатньо
# пального
# З ймовірністю 40% автомобіль може зламатись
#  ремонт
#  поповнення пального

class Car:
    def __init__(self, mark, mileage, fuel_waste):
        self.mark = mark
        self.milege = mileage
        self.fuel_waste = fuel_waste

        self.lvl_fuel = 0
        self.in_order = True

    def take_a_ride(self,distance):
        if  self.lvl_fuel < self.fuel_waste * distance :
            print("спочатку заправте автомобіль")
            return

        if not  self.in_order:
            print("почініть автомобіль або візьміть новий")
            return





