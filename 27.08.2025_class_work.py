# поліморфізм

class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def make_sound(self):
        print('мяу')

    def grow(self):
        self.age += 1

    def catch_mouse(self):
        pass

class Dog:
    def __init__(self, name, age, speed):
        self.name = name
        self.age = age
        self.speed = speed

    def make_sound(self):
        print('гав')

    def grow(self):
        self.age += 1


class Hamster:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print('пі-пі')

    def grow(self):
        self.age += 1


cat = Cat('Murchil', 3, 'black')
dog = Dog('Barsik', 2, 10)
hamster = Hamster('Benny',4)

pets = [cat, dog, hamster]

#комжна тварина видає якісь звуки

for pet in pets:
    pet.make_sound()


# model =NeuralNertwork()
#
# model.train(data)
