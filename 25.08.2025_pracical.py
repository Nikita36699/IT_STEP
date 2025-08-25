# Завдання 1
# Створіть клас Проект з атрибутами:
#  назва
#  виділений кошторис
#  загальні витрати
#  чи завершений(за замовчуванням False)
#  час виконання(за замовчуванням 0 місяців)
#  список необхідних задач
# Додайте методи:
#  вивід інформації: назва, час виконання, необхідні
# задачі
#  добавити нову задачу
#  розбити задачу на під-задачі: передається назва задачі
# та список під-задач
#  виконати задачу, передається назва, час та ціна
# виконання
#  поповнення кошторису
#
#
#опис классу(шаблон який описує всі проекти)
class Project:
    def __init__(self, name, budget, tasks: list):
        self.name  = name
        self.budget = budget
        self.tasks = tasks

        self.expenses = 0
        self.if_finished = False
        self.time = 0

    def show_info(self):
        print()
        print(f"інформація по проекту,{self.name}")
        print(f'\t Бюджет -- {self.budget}.грн')
        print(f"\t використано -- {self.expenses}/{self.budget}")
        print(f"\t час виконання -- {self.time} місяців")

        if self.if_finished:
            print("\t Статус -- Завершений")
        else:
            print("\t Статус -- Не завершений")

        print("\t список задач")
        for task in self.tasks:
            print(f'\t\t {task}')

    def add_task(self, new_task):
        self.tasks.append(new_task)
        print(f'додано нове завдання {new_task}')

    def created_subtasks(self,old_task, sub_tasks):
        #чи є стара задачу и списку
        if old_task not in self.tasks:
            print(f"Такої задачі немає у списку")
            return
        # old_task in list

        self.tasks.remove(old_task)
        self.tasks.extend(sub_tasks) #добавити всі елементи з subtasks в список self.tasks

    def do_task(self, task, price, time):
        if  task not in self.tasks:
            print(f'такої задачі немає в списку')
            return

        if price > self.budget - self.expenses:
            print(f"Не вистачає коштів")
            return

        #все добре робимо задачу
        self.tasks.remove(task)
        self.expenses += price
        self.time += time

        self.if_finished = len(self.tasks) == 0

    def deposit(self, price):
        self.budget += price



#створення конкретного проєкту
project1 = Project('Making Film',10000, ['write plot', 'find actors'])

# print(project1.tasks)
# print(project1.if_finished)

project1.show_info()
project1.add_task('find location')
project1.show_info()
print(project1.tasks)

project1.created_subtasks('talk with producer',sub_tasks= [])

project1.created_subtasks('find actors', ['talk with actor 1', 'talk with actor 2'])

project1.show_info()

project1.do_task('talk with actor 1',1000,0.5)
project1.show_info()


project1.deposit(50000)
project1.do_task('write plot',20000,3.5)
project1.show_info()