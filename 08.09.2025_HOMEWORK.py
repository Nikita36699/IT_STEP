# Завдання 1
# Створіть клас Pet з атрибутами
#  name – ім’я тварини
#  satiety – рівень ситості(від 0 до 100, за замовчуванням 50)
#  energy – рівень енергії (від 0 до 100, за замовчуванням 50)
# Методи:
#  sleep() – збільшує energy до 100
#  eat(food_amont) – їсть, збільшує satiety на food_amount
#  play(activity_level) – абстрактний метод
#  make_sound() – просто pass
# Створіть клас Cat
# Методи:
#  play(activity_level) – якщо satiety > 60, зменшує energy на
# 2*acticity_level та satiety на acticity_level
#  make_sound() – виводить ‘Мяу’
#  catch_mouse() – якщо energy > 30, ловить мишу. Якщо
# satiety > 40, то грається з мишею, інакше їсть
# Створіть клас Dog

import abc

class Pet(abc.ABC):
    def __init__(self, name: str, satiety: float = 50, energy: float = 50):
        self.name = name
        self.satiety = satiety
        self.energy = energy

    def sleep(self):
        self.energy = 100
        print(f"{self.name} виспався і повний енергії!")

    def eat(self, food_amount):
        self.satiety = min(100, self.satiety + food_amount)
        print(f"{self.name} поїв. Ситість тепер {self.satiety}")

    @abc.abstractmethod
    def play(self, activity_level):
        raise NotImplementedError("Цей метод треба реалізувати у підкласі")

    def make_sound(self):
        pass


class Cat(Pet):
    def play(self, activity_level):
        if self.satiety > 60:
            self.energy = max(0, self.energy - activity_level * 2)
            self.satiety = max(0, self.satiety - activity_level)
            print(f"Ви погралися з котом {self.name}")
        else:
            print(f"{self.name} занадто голодний, щоб гратися")

    def make_sound(self):
        print("Мяу")

    def catch_mouse(self):
        if self.energy > 30:
            print(f"Кіт {self.name} впіймав мишу")
            if self.satiety > 40:
                print(f"{self.name} грається з мишею")
            else:
                print(f"{self.name} з’їв мишу")
        else:
            print(f"{self.name} надто втомлений, щоб ловити мишей")


class Dog(Pet):
    def play(self, activity_level):
        if self.satiety > 15:
            self.energy = max(0, self.energy - activity_level // 2)
            self.satiety = max(0, self.satiety - activity_level // 2)
            print(f"Ви погралися з собакою {self.name}")
        else:
            print(f"{self.name} занадто голодний, щоб гратися")

    def make_sound(self):
        print("Гав")

    def fetch_ball(self):
        if self.satiety > 10:
            self.energy = max(0, self.energy - 5)
            print(f"Собака {self.name} приніс м’яч")
        else:
            print(f"{self.name} занадто голодний, щоб бігати за м’ячем")


cat = Cat("Мурчик")
dog = Dog("Барбос")

print("\n--- Початковий стан ---")
print(f"{cat.name}: satiety={cat.satiety}, energy={cat.energy}")
print(f"{dog.name}: satiety={dog.satiety}, energy={dog.energy}")
print("\n--- Кіт їсть ---")
cat.eat(30)  # +30 ситість
print(f"{cat.name}: satiety={cat.satiety}, energy={cat.energy}")
print("\n--- Кіт грається ---")
cat.play(15)
print(f"{cat.name}: satiety={cat.satiety}, energy={cat.energy}")
print("\n--- Кіт ловить мишу ---")
cat.catch_mouse()
print("\n--- Собака грається ---")
dog.play(20)
print(f"{dog.name}: satiety={dog.satiety}, energy={dog.energy}")
print("\n--- Собака ловить м’яч ---")
dog.fetch_ball()
print(f"{dog.name}: satiety={dog.satiety}, energy={dog.energy}")
print("\n--- Звуки ---")
cat.make_sound()
dog.make_sound()