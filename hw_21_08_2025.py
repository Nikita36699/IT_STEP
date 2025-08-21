# Завдання 1
# Створіть клас Cart(кошик клієнта магазину) з атрибутами
# client(ім’я клієнта) та items(список товарів).
# Додайте метод який додає новий товар до кошика
# Додайте метод який видаляє товар з кошика
# Додайте метод для виведення інформації про кошик
class Cart:
    def __init__(self,client,items):
         self.client = client
         self.items = items

    def add_item(self, item):
        self.items.append(item)

        return self.items


    def delete_item(self,item):
        if item in self.items:
            self.items.remove(item)
        else:
            print("Такого товару немає в кошику!")


    def show_items(self):
        print(f'ваш кошик на данний момент такий - {self.items}')


def get_user_choice():
    user_choise = input('оберіть дію від одного до 3 дє 1-додати,2-видалити,3-показати -кошик').strip()

    return user_choise


def get_user_item():
    user_item = input("введіть ваш товар - ")

    return  user_item


def main():
    cart = Cart("Нікіта", [])  # створюємо кошик для клієнта
    print('Введіть "4", щоб завершити роботу')

    while True:
        choice = get_user_choice()

        if choice == '1':
            item = get_user_item()
            cart.add_item(item)
            print("Товар додано!")

        elif choice == '2':
            item = get_user_item()
            cart.delete_item(item)
            print('Товар видалено')

        elif choice == '3':
            cart.show_items()

        elif choice == '4':
            print("Вихід з програми...")
            break

        else:
            print("Невірний вибір, спробуйте ще раз!")
main()

# Завдання 2
# Створіть клас Phone з атрибутами number та battery_level.
# Додайте метод який зменшує заряд телефона(на скільки
# зменшити відсотків передається як параметр), якщо він
# опуститься нижче 20%, вивести повідомлення
# Додайте метод для виведення інформації про телефон
class Phone:
    def __init__(self, number, battery_level):
        self.number = number
        self.battery_level = battery_level

    def battery_change(self,change=15):
        self.battery_level = self.battery_level - change

        if self.battery_level < 20:
            print('у вас низький заряд батареи')

        return self.battery_level

    def phone_info(self):

        print(f'номер телефону = {self.number}, заряд батареї - {self.battery_level} ')

phone1 = Phone(number = '+380996669966',battery_level=100)

phone1.phone_info()
phone1.battery_change(81)
phone1.phone_info()
