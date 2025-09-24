
#
# Завдання 1
# Використовуючи бінарні дерева, організуйте роботу
# автопарку, де зберігаються автомобілі, відсортовані за
# маркою
# Клас Car
# Атрибути:
#  brand – модель автомобіля
#  model – марка автомобіля
#  year – рік випуску
# Клас CarPark
# Атрибути:
#  cars – дерево з автомобілями
# Методи:
#  add(car) – добавити автомобіль
#  remove(model) – видалити автомобіль
#  search(model) – пошук автомобіля за маркою, якщо є
# то повертає книгу інакше None
#  __len__() – кількість автомобілів
#  sell_car(client, model) – продати автомобіль клієнту,
# якщо така марка присутня


import bintrees

class Car:
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand   # BMW
        self.model = model   # X5
        self.year = year     # 2019

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"


class CarPark:
    def __init__(self):
        self.cars = bintrees.AVLTree()

    def add(self, car: Car):
        if car.brand not in self.cars:
            self.cars.insert(car.brand, car)
        else:
            print("car already parked")

    def remove(self, brand):
        if brand in self.cars:
            self.cars.remove(brand)
        else:
            print("NO SUCH CAR!!!")

    def search(self, brand):
        if brand in self.cars:
            return self.cars.get(brand)
        return None

    def __len__(self):
        return len(self.cars)

    def sell_car(self, client, brand):
        if brand in self.cars:
            car = self.cars.get(brand)
            self.cars.remove(brand)
            print(f"{client} BOUGHT {car.brand} {car.model} {car.year}")
            return car
        else:
            print("CHOOSE OTHER CAR WE DO NOT HAVE THIS ONE ")
            return None


car1 = Car("BMW", "X5", 2019)
car2 = Car("Audi", "Q7", 2021)
car3 = Car("Mercedes", "GLE", 2020)


car_park = CarPark()


print("Добавляем машины:")
car_park.add(car1)  # Должно добавиться
car_park.add(car2)  # Должно добавиться
car_park.add(car1)  # Должно вывести "car already parked"


print("Количество машин в автопарке:", len(car_park))  # Ожидаем 2


print("Ищем BMW:", car_park.search("BMW"))
print("Ищем Audi:", car_park.search("Audi"))
print("Ищем Mercedes:", car_park.search("Mercedes"))


print("Удаляем Audi:")
car_park.remove("Audi")
car_park.remove("Audi")

print("Количество машин в автопарке после удаления:", len(car_park))


print("Продажа BMW клиенту John:")
sold_car = car_park.sell_car("John", "BMW")
print("Проданные машины:", sold_car)


print("Попытка продажи Audi клиенту Alice:")
car_park.sell_car("Alice", "Audi")


print("Количество машин в автопарке в конце:", len(car_park))