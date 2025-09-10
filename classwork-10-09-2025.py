# nums = [1, 2, 3, 4, 5, 6, 7, 8]
#
# nums.append(4) # быстро
# 10 in nums # медленно
#
#
#
# nums = {1, 2, 3, 4, 5} # множество(set)
# nums.add(4) # быстро
# 10 in nums # быстро
#
#
#
# 2 + 4 * 5 - (10 + 7)
#
# нотация О
# используется для приблизительной оценки количества операций
#в залежность від розміру вхідних данних(N)
# приклади что такое N:
# -- кількість данних у базі(алгоритм пошуку\додавання елементів до списку)
# -- число(алгоритми переревырки на простоту числа або обрахунок певної величини числа )
#

#O(1) -- не залежить від N(не залежить від кількості данних
#O(log(N)) -- якшо данні збілшити в 2 разів то кількість операціі зросте на 1
#O(N) -- кількість операцій приблизно дорівнює кількість данних
#O(N^2) -- якшо данні збілшити в 10 разів то кількість операціі зросте в квадраті а собственно в 100 раз


#зв'язні списки
#
# # class for yzel
# class Node:
#     def __init__(self, value):
#         self.value = value #данні у вузлі
#         self.next = None  # посилання на наступний вузол
#
# nums = [3, 7, 2, 5]
#
# #перший вузол
# node1 =Node(3)
#
# #другий вузол
# node2 =Node(7)
# #зв'язок між першим та другим узлом
# node1.next = node2
#
# node3 = Node(2)
# node2.next = node3
#
# node4 = Node(5)
# node3.next = node4
#
# temp_node = node1
#
# while temp_node is not None:
#     print(temp_node.value)
#     temp_node = temp_node.next


#  Завдання 1
# Створіть клас однозв’язного списку SinglyLinkedList
# Методи
#  print() – виводить список на екран
#  push_end(data) – добавити в кінець
#  push_start(data) – добавити на початку
#  pop_start() – видалити перший елемент
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):#O(1)
        return self.head is None


    def print(self):# O(N)
        temp_node = self.head

        while temp_node is not None:
            print(temp_node.value, end= ' -> ')
            temp_node = temp_node.next

        print()

    def push_end(self, data):
        if not self.is_empty():#O(1)
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
        else:#O(1)
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node

    def push_start(self,data):
        if not self.is_empty():#O(1)
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:#O(1)
            new_node = Node(data)
            self.head = new_node
            self.tail = new_node

    def pop_start(self):#O(1)
        if self.head != self.tail:
            temp_node = self.head
            self.head = self.head.next
            temp_node.next = None
        else:
            self.head = None
            self.tail = None

    def get_item(self, pos):
        counter = 0
        temp_node = self.head

        while counter != pos - 1 :
            counter += 1
            temp_node = temp_node.next

        return  temp_node.value

new_list = SinglyLinkedList()
new_list.push_start(5)
new_list.push_start(4)
new_list.push_start(3)
new_list.push_start(2)
new_list.push_start(1)
res = new_list.get_item(4)
print(res)

new_list.print()

# Завдання 2
# Створіть клас двозв’язного списку DoubleLinkedList
# Методи
#  print(reversed=False) – виводить список на екран(з
# початку або з кінця залежно від reversed)
#  push_end(data) – добавити в кінець
#  push_start(data) – добавити на початку
#  pop_end() – видалити останній елемент
#  pop_start() – видалити перший елемент
# Завдання 3
# Є два однозв’язні списки, об’єднайте їх в один.
# Є два двозв’язні списки, об’єднайте їх в один.
# Виведіь результат на екран
# Завдання 4
# Є двозв’язний список. Отримайте елемент з індексом k з
# кінця.
# Є однозв’язний список. Отримайте елемент з індексом k з
# кінця.
# Завдання 5
# Є два відсортованих однозв’язних списка, об’єднайте їх в
# один відсортований список