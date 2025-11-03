# Частина 1: Основи Python
# 1. Напишіть програму, яка приймає два цілих числа від
# користувача і виводить суму діапазону чисел між ними.
start = int(input('add first num'))
end = int(input('add second num'))

total = 0

for i in range(start, end +1):
    total += i

print(total)


# 2. Напишіть програму, для знаходження суми всіх парних
# чисел від 1 до 100.

total_pos = 0
for num in range(1, 100 +1):
    if num % 2 == 0:
        total_pos += num

print(total_pos)




# 3. Напишіть програму, яка приймає рядок від користувача і
# виводить кожну літеру рядка на окремому рядку.
user_string = input('add your text').strip()

for i in user_string:
    print(i)



# 4. Напишіть програму, яка створює список цілих чисел та
# виводить новий список, який містить лише парні числа з
# вихідного списку.
import random
nums = []
new_nums = []
for n in range(100):
    random_num = random.randint(-10, 199)
    nums.append(random_num)

for num in nums:
    if num % 2 == 0:
        new_nums.append(num)

print(new_nums)



# 5. Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, що починаються з великої літери.
def filter_capital_words(words):
    new_list = []
    for w in words:
        if w and w[0].isupper():
            new_list.append(w)

    return new_list


user_input = input('add your words with space')
words_list = user_input.split()

result = filter_capital_words(words_list)
print('Upper words:',  result)


# 6. Напишіть функцію, яка приймає список рядків від
# користувача і повертає новий список, що містить лише
# рядки, які містять слово "Python".
def python_filter(words):
    words_python =  []
    for w in words:
        if "Python" in w:
            words_python.append(w)

    return words_python

user_input = input('add your words with space')
words_list = user_input.split()

result = python_filter(words_list)
print('string which have "Python": ', result)


# 7. (додаткове на кристалики)Напишіть програму, яка
# створює словник, де ключами є слова, а значеннями - їхні
# визначення. Дозвольте користувачу додавати, видаляти
# та шукати слова у цьому словнику.
def add_value(user_dict: dict):
    user_key = input('add your word - ')
    user_value = input('add meaning to your word')

    user_dict[user_key] = user_value

    return  user_dict


def delete_value(user_dict: dict):
    user_key = input('enter a key which to delete')

    if user_key in user_dict:
        user_dict.pop(user_key)
    else:
        print('such key has not found')

    return  user_dict


def search(user_dict: dict):
    query = input('Enter a word or part of its meaning to search: ').lower()
    found = False

    for key, value  in user_dict.items():
        if query in key.lower() or query in value.lower():
            print(f'{key} :  {value} ')
            found = True

    if not found:
        print('no matches found.')

def main():
    user_dict = {}
    while True:
        print("Choose an option:")
        print("1. Add word")
        print("2. Delete word")
        print("3. Search word")
        print("4. Exit")


        choice = input("Your choice: ")
        print()

        if choice == "4":
            break
        elif choice == "1":
            add_value(user_dict)
        elif choice == "2":
            delete_value(user_dict)
        elif choice == "3":
            search(user_dict)
        else:
            print("Invalid choice. Try again.\n")

main()



# 8. (додаткове на кристалики)Використовуючи лямбдафункцію, напишіть вираз, який сортує список кортежів
# за другим елементом кожного кортежу (наприклад, [(1,
# 3), (3, 2), (2, 1)]).
tuples_list = [(1, 3), (3, 2), (2, 1)]
sorted_list = sorted(tuples_list, key=lambda x: x[1])

print(sorted_list)


# Симулятор роботи сайту
# WebSite: Основний клас, який представляє вебсайт.
# Атрибути: назва сайту, URL, список сторінок.
# Методи: додавання/видалення сторінок, відображення
# інформації про сайт.
# WebPage: Клас, який представляє окрему сторінку на сайті.
# Атрибути: заголовок сторінки, вміст, дата публікації.
# Методи: відображення деталей сторінки.
# Реалізація функціональності:
# Дозвольте користувачеві створювати новий сайт з
# певною назвою та URL. Додайте можливість створювати нові
# сторінки для сайту, вводячи заголовок та вміст. Реалізуйте
# функцію для видалення сторінок з сайту. Включіть функцію
# для відображення всієї інформації про сайт, включаючи
# список усіх сторінок.
# Розробіть простий текстовий інтерфейс для взаємодії з
# користувачем. Користувач повинен мати змогу вибирати дії,
# такі як створення сайту, додавання/видалення сторінок,
# перегляд інформації про сайт.
from datetime import datetime
class  WebPage:
    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def show_details(self):
        print(f"Title: {self.title}")
        print(f"Date: {self.date}")
        print(f"Content: {self.content}")



class WebSite:
    def __init__(self, site_name, site_url):
        self.site_name = site_name
        self.site_url = site_url
        self.pages_list = []

    def __str__(self):
        return f'Site Name: {self.site_name},\nSite Url: {self.site_url}'


    def add_page(self, page):
        self.pages_list.append(page)

    def remove_page(self, title):
        for page in self.pages_list:
            if page.title == title:
                self.pages_list.remove(page)
                print(f"Page '{title}' removed.")
                return
        print(f"No page found with title '{title}'")

    def edit_page(self, title, new_title=None, new_content=None):
        for page in self.pages_list:
            if page.title == title:
                if new_title:
                    page.title = new_title
                if new_content:
                    page.content = new_content
                print(f"Page '{title}' updated.")
                return
        print(f"No page found with title '{title}'")

    def search_pages(self, keyword):
        results = []
        for page in self.pages_list:
            if keyword.lower() in page.title.lower() or keyword.lower() in page.content.lower():
                results.append(page)
        return results

    def show_info(self):
        print("\n--------Website info--------")
        print(f"Name: {self.site_name}")
        print(f"URL: {self.site_url}")
        print("------------------------------")

        if not self.pages_list:
            print("No pages on this site yet.")
        else:
            print(f"Total pages: {len(self.pages_list)}\n")
            for i, page in enumerate(self.pages_list, start=1):
                print(f"{i}.")
                page.show_details()
        print("--------------------------------")

my_site = WebSite("MyCoolSite", "www.coolsite.com")

# Создаём страницы
page1 = WebPage("Home", "Welcome to my website!")
page2 = WebPage("About", "This is an example site.")

# Добавляем страницы
my_site.add_page(page1)
my_site.add_page(page2)

# Показываем информацию о сайте
my_site.show_info()

# Удаляем страницу
my_site.remove_page("Home")

# Смотрим результат
my_site.show_info()

# Додаткові можливості (за бажанням на кристалики):
# Реалізуйте систему логіну/реєстрації для керування
# сайтом. Додайте можливість редагування існуючих сторінок.
# Створіть функціонал для пошуку сторінок за ключовими
# словами у заголовку або вмісті
users = {}

def register():
    login = input('Enter new login: ').strip()

    if login in users:
        print('login already exists')
        return  False

    password = input('Enter password: ').strip()
    users[login] = password
    print('Registration succesfull!')
    return  True


def login():
    login_name = input('login: ').strip()
    password = input('password: ').strip()

    if users.get(login_name) == password:
        print(f'Welcome,{login_name}!')
        return
    else:
        print('incorect log or pass')
        return

def main():
    site_name = input('enter site name: ').strip()
    site_url  = input('enter website URL: ').strip()
    site = WebSite(site_name, site_url)

    while True:
        print("\n--- Site Menu ---")
        print("1. Add Page")
        print("2. Remove Page")
        print("3. Edit Page")
        print("4. Show Website Info")
        print("5. Search Pages")
        print("6. Exit")
        action = input("Choose action: ").strip()

        if action == '1':
            title = input("Page title: ").strip()
            content = input("Page content: ").strip()
            page = WebPage(title, content)
            site.add_page(page)


        elif action == '2':
            title = input("Page title: ").strip()
            site.remove_page(title)

        elif action == "3":
            title = input("Enter title of page to edit: ").strip()
            new_title = input("New title (leave empty if no change): ").strip()
            new_content = input("New content (leave empty if no change): ").strip()
            site.edit_page(title, new_title if new_title else None, new_content if new_content else None)

        elif action == "4":
            site.show_info()

        elif action == "5":
            keyword = input("Enter keyword to search: ").strip()
            results = site.search_pages(keyword)
            if not results:
                print("No pages found with that keyword.")
            else:
                print(f"Found {len(results)} page(s):")
                for page in results:
                    page.show_details()


        elif action == "6":
            print("Exiting... Bye!")
            break

        else:
            print("Invalid action. Try again.")


main()

