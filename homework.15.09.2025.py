# Завдання 1
# Використовуючи класи з практичної реалізуйте клас Shop з
# трьома чергами до кас. Кожна черга реалізується через
# двозв’язний список
# Атрибути
#  queue1, queue2, queue3 – черги до кас
# Методи
#  add_buyer(name, idx) – додає покупця в кінець черги
# номер idx
#  serve_buyer(idx) – обслуговує покупця з черги
# idx(вивести повідомлення та видалити покупця з черги)
# Якщо черга стала порожньою, то викликати _reorder(idx)
#  _reorder(idx) – з усіх черг останній покупець переходить
# в чергу з номером idx
#  display_info() – виводить на екран 3 черги
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return f"{self.data} -> {self.next}"


class DoubleLinkedList:
    """
    Клас двозв'язного списку.
    """

    def __init__(self):
        """
        Ініціалізація порожнього списку.
        """
        self.head = None
        self.tail = None

    def __str__(self):
        return str(self.head)

    def push_end(self, data):
        """
        Додає елемент у кінець списку.
        :param data: Дані для додавання
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def push_start(self, data):
        """
        Додає елемент на початок списку.
        :param data: Дані для додавання
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def pop_end(self):
        """
        Видаляє останній елемент зі списку.
        :return: Дані видаленого елемента або None, якщо список порожній
        """
        if not self.tail:
            return None

        data = self.tail.data

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        return data

    def pop_start(self):
        """
        Видаляє перший елемент зі списку.
        :return: Дані видаленого елемента або None, якщо список порожній
        """

        if not self.head:
            return None

        data = self.head.data

        if self.head.next is None:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return data


class Shop:
    def __init__(self):
        self.queue1 = DoubleLinkedList()
        self.queue2 = DoubleLinkedList()
        self.queue3 = DoubleLinkedList()

    def add_buyer(self, name, idx):
        """
        Добавляет покупателя в конец очереди с номером idx
        """
        queue = self._get_queue(idx)
        if queue is None:
            print(f"Черги {idx} не існує")
            return
        queue.push_end(name)
        print(f"{name} став у чергу {idx}")

    def serve_buyer(self, idx):
        """
        Обслуговує першого покупця з черги idx
        """
        queue = self._get_queue(idx)
        if queue is None:
            print(f"Черги {idx} не існує")
            return

        buyer = queue.pop_start()
        if buyer:
            print(f"{buyer} був обслужений на касі {idx}")
        else:
            print(f"Черга {idx} порожня")

        if queue.head is None:
            self._reorder(idx)

    def _reorder(self, idx):
        """
        З усіх черг останній покупець переходить в чергу idx
        """
        print(f"Черга {idx} порожня → перебудова...")
        for i in [1, 2, 3]:
            if i != idx:
                q = self._get_queue(i)
                if q and q.tail:  # беремо останнього покупця
                    buyer = q.pop_end()
                    self._get_queue(idx).push_end(buyer)
                    print(f"{buyer} перейшов у чергу {idx}")
                    return

    def display_info(self):
        """
        Виводить всі 3 черги
        """
        print("=== Стан черг ===")
        for i, q in enumerate([self.queue1, self.queue2, self.queue3], start=1):
            buyers = []
            node = q.head
            while node:
                buyers.append(node.data)
                node = node.next
            print(f"Черга {i}: {buyers if buyers else 'порожня'}")

    def _get_queue(self, idx):
        """
        Допоміжний метод — повертає потрібну чергу
        """
        if idx == 1:
            return self.queue1
        elif idx == 2:
            return self.queue2
        elif idx == 3:
            return self.queue3
        return None