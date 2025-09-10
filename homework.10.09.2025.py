
# Завдання 1
# Створіть клас Passenger з атрибутами
#  name – ім’я
#  destination – місце, куди прямує
class Passenger:
    def __init__(self, name: str, destination: str):
        self.name  = name
        self.destination = destination
# Завдання 2
# Створіть клас Transport з атрибутами
#  speed – швидкість
# Методи
#  move(destination, distance) – рухається до місця
# призначення, виводить інформацію як довго їхали
class Transport:
    def __init__(self, speed: float):
        self.speed = speed

    def move(self, destination, distance):
        if self.speed <= 0:
            print('Швидкість не може бути відємною')
            return

        if distance <= 0:
            print('Тоді можно було і пішки пройтись')
            return

        how_long_road = distance / self.speed


        print(f"ви доїхали до {destination} за такий час {how_long_road} годин ")

# Завдання 3
# Створіть клас Bus з атрибутами
#  passengers – список пасажирів(об’єкти класу Passenger)
#  capacity – максимальна можлива кількість пасажирів
# Методи
#  board_passenger(passenger) – якщо є місце, додає
# пасажира
#  move(destination, distance) – висаджує всіх пасажирів, які
# хочуть вийти в даному місці(виводить їхню загальну
# кількість) та викликає батьківський метод move()
class Bus(Transport):
    def __init__(self, speed, passengers, capacity):
        super().__init__(speed)

        self.capacity = capacity

        if  passengers is None:
            passengers = []
        self.passengers = passengers

    def board_passenger(self,passenger):
        if len(self.passengers) >= self.capacity:
            print(f'Більше немає місця для вас {passenger.name}')

        else:
            self.passengers.append(passenger)
            print(f'ви сіли на автобус {passenger.name}')

    def move(self, destination, distance):
        leaving_passengers = [p for p in self.passengers if p.destination == destination]
        print(f"Висаджено {len(leaving_passengers)} пасажирів у {destination}")


        self.passengers = [p for p in self.passengers if p.destination != destination]

        super().move(destination, distance)

p1 = Passenger("Іван", "Київ")
p2 = Passenger("Марія", "Львів")
p3 = Passenger("Олег", "Київ")

bus = Bus(speed=60, passengers=None, capacity=2)

bus.board_passenger(p1)
bus.board_passenger(p2)
bus.board_passenger(p3)
print(f"Зараз у автобусі {len(bus.passengers)} пасажирів")

bus.move("Київ", 300)
print(f"Зараз у автобусі {len(bus.passengers)} пасажирів")

bus.move("Львів", 500)
print(f"Зараз у автобусі {len(bus.passengers)} пасажирів")