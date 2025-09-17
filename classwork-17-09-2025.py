# стеки

# def func1():
#     func2()
#
#
# def func2():
#     func3()
#
# def func3():
#     print()
#
#     return
#
#
# func1()


from queue import LifoQueue
#
#
# stack = LifoQueue()  # стек
#
# stack.put(1)
# stack.put(2)
# stack.put(3)
# stack.put(4)
#
# print(stack.get())  # останній улемент який був доданий до стека
# print(stack.get())
# print(stack.get())
# print(stack.get())


# перевірка правильності дужок у виразі

# наївний
def naive(expr):
    counts = {
        '(': 0,
        '[': 0,
        '{': 0
    }

    reversed_brackets = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in expr:
        if char in "([{":
            counts[char] += 1
        elif char in ")]}":
            reversed_bracket = reversed_brackets[char]

            if counts[reversed_bracket] == 0:
                print('Дужки неправильні')
                return
            counts[reversed_bracket] -= 1

    # перевірка чи залишились відкриті дужки
    for bracket in counts:
        if counts[bracket] > 0:
            print('Забагато відкритих дужок')
            return

    print('Дужки правильні')


def correct_method(expr):
    RED = "\033[91m"  # червоний колір
    RESET = "\033[0m"

    stack = LifoQueue()

    for i, char in enumerate(expr):
        if char in "([{":
            stack.put((i, char))
        elif char in ")]}":
            if stack.empty():
                print(expr[:i] + f"{RED}{char}{RESET}" + expr[i+1:])
                print('Дужки неправильні')
                return

            j, last_bracket = stack.get()

            if last_bracket + char not in ['()', '{}', '[]']:
                print(expr[:j] + f"{RED}{last_bracket}{RESET}" + expr[j + 1:i] + f"{RED}{char}{RESET}" + expr[i+1:])
                print('Дужки неправильні')
                return

    if not stack.empty():
        i, char = stack.get()
        print(expr[:i] + f"{RED}{char}{RESET}" + expr[i + 1:])
        print('Забагато відкритих дужок')
        return

    print('Дужки правильні')


expr = "num = [func(1 * )(2 - 3)), func2({'John', 'Mike})]"
#expr = "([)]"
correct_method(expr)

# Завдання 1
# Використовуючи стек створіть клас WebHistory
# Атрибути:
#  history – стек з історією відвідування веб сторінок
#  forward_history – стек з веб сторінками, для повернення «вперед»
# Методи:
#  add(page) – перейти на нову сторінку
#  undo() – повернутись на попередню сторінку
#  redo() – перейти вперед
#  get_current_page() – повернути поточну сторінку
from queue import LifoQueue

class WebHistory:
    def __init__(self):
        self.history = LifoQueue()

        self.forward_history = LifoQueue()

    def add(self, page):
        self.history.put(page)
        self.forward_history = LifoQueue()
        print(f"Перешли на {page}\n")

    def undo(self):
        if self.history.empty():
            print('history empty')
            return

        page = self.history.get()
        self.forward_history.put(page)

        if self.history.empty():
            print('history empty')
            return

        page =  self.history.queue[-1]
        print(f'ви повернулися  на  {page}\n')

    def redo(self):
        if self.forward_history.empty():
            print('history empty redo ')
            return

        page = self.forward_history.get()
        self.history.put(page)

        if self.forward_history.empty():
            print('history empty redo ')
            return

        page = self.history.queue[-1]
        print(f'ви повернулися  на  {page}\n')


wh = WebHistory()
wh.add('Google')
wh.add('chatGPT')
wh.undo()
wh.add('Youtube')
wh.undo()
wh.undo()
wh.undo()
wh.undo()
wh.undo()



wh.redo()
wh.redo()