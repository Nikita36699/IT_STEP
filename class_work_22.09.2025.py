# # дерева
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None
#
#
# class BinaryTree:
#     def __init__(self):
#         self.root = None  # корінь дерева
#
#     def add(self, data):
#         node = Node(data)
#
#         # дерево порожнє
#         if self.root is None:
#             self.root = node
#             return
#
#         # вузол де робимо перевірку
#         current_node = self.root
#
#         while True:
#             # йдемо наліво
#             if data < current_node.data:
#                 # зліва вільне місце(вузла немає)
#                 if current_node.left is None:
#                     current_node.left = node
#                     break
#                 else:
#                     # зліва зайнято(повторити перевірку знову)
#                     current_node = current_node.left
#
#             elif data > current_node.data:  # йдемо направо
#                 # справа вільне місце(вузла немає)
#                 if current_node.right is None:
#                     current_node.right = node
#                     break
#                 else:
#                     current_node = current_node.right
#
#             else: # не можна добавляти дублікати
#                 break
#
#
#     def search(self, data):
#         current_node = self.root
#
#         while current_node is not None:
#             # вузол знайдено
#             if current_node.data == data:
#                 return True
#
#             elif data < current_node.data:
#                 current_node = current_node.left
#
#             elif data > current_node.data:
#                 current_node = current_node.right
#
#         # цикл зупинився -- значить даних в дереві немає
#         return False
#
#     def min(self):
#         current_node = self.root
#
#         while current_node.left is not None:
#             current_node = current_node.left
#
#         return current_node.data
#
#     def print_inorder(self):
#         self._inorder(self.root)
#         print()
#
#     def _inorder(self, node):  # _ -- приватний метод класу
#         if node.left:
#             self._inorder(node.left)
#
#         print(node.data, end=' ')
#
#         if node.right:
#             self._inorder(node.right)
#
#
#
# tree = BinaryTree()
#
# tree.add(5)
# tree.add(7)
# tree.add(3)
# tree.add(8)
# tree.add(4)
# tree.add(6)
#
# print(tree.search(8))
# print(tree.search(2))
#
# print(tree.min())
#
# tree.print_inorder()
import bintrees


# # AVL дерева
# import bintrees
#
# tree = bintrees.AVLTree()
#
# # сортує значення по параметру key
# tree.insert(key=8, value='John')
# tree.insert(key=10, value='Maria')
#
#
# tree.remove(8)
#
# # отримати значення(перевірка)
#
# if 10 in tree:
#     print(tree[10])



# Завдання:
#
# Створити бінарне дерево для каталогу книг у бібліотеці.
#
# Операції:
#
# Insert: Додавання нової книги в каталог з вказаною назвою та іншою інформацією (автор, рік видання, жанр тощо).
#
# Search: Пошук книги за назвою або іншими параметрами. Пошук повинен повертати усю інформацію, що стосується цієї книги.
#
# Delete: Видалення книги з каталогу за назвою або іншими параметрами.
#
# Display: Виведення всього каталогу книг за зростанням або спаданням алфавіту за назвою.
#
# Count: Підрахунок кількості книг у бібліотеці.
#
# Властивості:
#
# Зберігання: Книги зберігаються за алфавітом за назвою книги.
#
# Пошук: Користувач може шукати книгу за назвою або іншою інформацією про книгу.
#
# Видалення: Користувач може видаляти книгу з каталогу за назвою або іншими параметрами.
#
# Показ каталогу: Виведення всіх книг у вигляді списку, відсортованого за назвою книги.
#
# Статистика: Виведення загальної кількості книг у бібліотеці.
#
# Приклад використання:
#

# class Book:
#     def __init__(self, name, author, year, style):
#         self.name = name
#         self.year = year
#         self.author = author
#         self.style = style
#
#     def __str__(self):
#         return f"Book\n\tauthor\t{self.author}\n\tname\t{self.name}\n\tyear\t{self.year}\n\tstyle\t{self.style}"
#
#
# class BinaryTreeLibrary():
#     def __init__(self):
#         self.books_tree = bintrees.AVLTree()
#
#     # Insert: Додавання нової книги в каталог з вказаною назвою та іншою інформацією(автор, ріквидання, жанртощо).
#     def insert(self, name, author, year, style):
#         book = Book(name, author, year, style)
#         self.books_tree.insert(key=name, value=book)
#
#     # Search: Пошук книги за назвою або іншими параметрами. Пошук повинен повертати усю інформацію, що стосується цієї книги.
#     def search(self, name):
#         if name in self.books_tree:
#             book = self.books_tree[name]
#             print(book)
#
#     # Delete: Видалення книги з каталогу за назвою або іншими параметрами.
#     def delete(self, name):
#         if name in self.books_tree:
#             self.books_tree.remove(name)
#
#     # Display: Виведення всього каталогу книг за зростанням або спаданням алфавіту за назвою.
#     def display(self):
#         for name in self.books_tree:
#             print(self.books_tree[name])
#
#     # Count: Підрахунок кількості книг у бібліотеці.
#     def count(self):
#         return len(self.books_tree)
#
#
# library = BinaryTreeLibrary()
#
# library.insert("1984", "George Orwell", 1949, "Dystopian Fiction")
# library.insert("To Kill a Mockingbird", "Harper Lee", 1960, "Classic Fiction")
# library.insert("Pride and Prejudice", "Jane Austen", 1813, "Romance")
#
# print("Books in library:")
# library.display()
#
# print("\nSearching for '1984':")
# library.search("1984")
#
# library.delete("To Kill a Mockingbird")
# print("\nBooks in library after deletion:")
# library.display()
#
# print("\nTotal number of books:", library.count())



# Створіть програму роботи зі словником. Наприклад,
# англо-іспанський, французько-німецький або інша мовна пара.
# Програма має:
#  надавати початкове введення даних для словника
#  відображати слово та його переклади
#  дозволяти додавати, змінювати, видаляти переклади
# слова

import bintrees


class Translation:
    def __init__(self, word: str, usage_example=None):
        self.word = word
        if usage_example:
            self.usage_example = usage_example
        else:
            self.usage_example = ''

    def __str__(self):
        return f'Translation: {self.word}, usage example: {self.usage_example}'

class WordsCouples:
    def __init__(self, word: str):
        self.word = word
        self.translations = {}
        #self.usage_example =

    def add_translation(self, trans_word: str, usage_example=None):
        this_translation = Translation(trans_word, usage_example)

        self.translations[trans_word] = this_translation

    def delete_translation(self, trans_word: str):
        self.translations.pop(trans_word)

    def __str__(self):
        all_translations = ', '.join(self.translations)
        #all_usage_examples = ', '.join(self.translations.values())
        all_usage_examples = ''

        for t in self.translations.values():
            all_usage_examples += str(t) + ', \n'


        return f'Word: {self.word}, translations: {all_translations}, usage examples: {all_usage_examples}'

class Dictionary:
    def __init__(self):
        self.words = bintrees.AVLTree()

    def add_word(self, word: str):
        this_word = WordsCouples(word)
        self.words.insert(key=word, value=this_word)

    def delete_word(self, word: str):
        if word in self.words:
            self.words.remove(key=word)

    def add_translation(self, key_word: str, translation: str, usage_examples=None):
        if key_word in self.words:
            self.words[key_word].add_translation(translation)
            return

        print(f'No {key_word} in the dictionary found.')

    def delete_translation(self, key_word: str, translation: str):
        if key_word in self.words:
            self.words[key_word].delete_translation(translation)
            return

        print(f'No {key_word} in the dictionary found.')

    def display_word(self, key_word: str):
        if key_word in self.words:
            print(self.words[key_word])
            return

        print(f'No {key_word} in the dictionary found.')


dict1 = Dictionary()

dict1.add_word('Apple')
dict1.add_translation('Apple', 'Яблоко', 'Яблоко упало.')
dict1.add_translation('Apple', 'Яблочко')

dict1.add_word('Word')
dict1.add_translation('Word', 'Слово')

dict1.delete_word('Word')

dict1.display_word('Apple')
dict1.display_word('Word')

dict1.delete_translation('Apple', 'Яблочко')
dict1.display_word('Apple')