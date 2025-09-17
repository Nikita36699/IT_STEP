# Завдання 2
# Використовуючи черги з пріоритетом створіть програму для симуляції роботи аеропорту. Кожен пасажир має пройти через 3 етапи: реєстрація, контроль безпеки, посадка. Відповідно аеропорт складається з 3-ох зон, кожна з яких має свою чергу. Коли Пасажир пройшов одну зону, то переходить в наступну.
# Пасажири з вищим пріоритетом обслуговуються першими
# Клас Zone – зона
# Атрибути:
#  name – назва(реєстрація, контроль безпеки або посадка)
#  passengers – черга пасажирів
# Методи:
#  add(passenger) – додає пацієнта в чергу з пріоритетом
#  serve_passenger() – обслуговуємо наступного пасажира та повертає його
# Клас Airport – аеропорт
# Атрибути:
#  zones – словник із зонами, ключем є назва зони
#  passengers – список пасажирів, які успішно пройшли 3 зони
# Методи:
#  add(passenger) – додає пасажира в чергу на реєстрацію
#  serve_registration() – обслуговує клієнта з черги реєстрації та переводить на котроль безпеки
#  serve_security_control() – обслуговує клієнта з черги контролю безпеки та переводить на посадку
#  serve_boarding() – обслуговує клієнта з черги посадки та переводить в passengers
#  show_statistics() – вивести кількість пасажирів у кожній зоні та скільки успішно все пройшли
# Для цього скористайтесь класом Passenger
# Атрибути:
#  name – ім’я
#  priority – пріоритет
# TASK 2
# Завдання 3
# Створіть дочірні класи від Zone та перевизначте метод
# serve_passenger() щоб він повертав пару: пасажир та True/False
# в залежності від успішності перевірки.
# Перевірки:
#  реєстрація – наявність білету(у багажі)
#  безпека – відсутність небезпечних предметів у багажі:
# ніж, зброя, вибухівка
#  посадка – перевірка не потрібна
# Для цього скористайтесь класом Passenger
# Атрибути:
#  name – ім’я
#  priority – пріоритет
#  baggage – список з предметами в багажі
from queue import PriorityQueue

class Passenger:
    def __init__(self, name, priority, baggage: list):
        self.name = name
        self.priority = priority
        self.baggage = baggage


class Zone:
    def __init__(self, name):
        self.name = name
        self.passengers = PriorityQueue()

    def add(self, passenger: Passenger):
        self.passengers.put((passenger.priority, passenger))

    def serve_passenger(self):
        if self.passengers.empty():
            return None
        priority, passenger = self.passengers.get()
        print(f'{passenger.name} пройшов зону {self.name}')
        return passenger, True


class RegistrationZone(Zone):
    def __init__(self, name):
        super().__init__(name)

    def serve_passenger(self):
        if self.passengers.empty():
            return None
        priority, passenger = self.passengers.get()

        if "ticket" in passenger.baggage:
            print(f'{passenger.name} успішно зареєструвався')
            return passenger, True
        else:
            print(f'{passenger.name} НЕ має квитка ')
            return passenger, False


class SecurityZone(Zone):
    def __init__(self, name):
        super().__init__(name)

    def serve_passenger(self):
        if self.passengers.empty():
            return None
        priority, passenger = self.passengers.get()

        forbidden = {"knife", "weapon", "explosive"}
        if any(item in forbidden for item in passenger.baggage):
            print(f'{passenger.name} НЕ пройшов безпеку ')
            return passenger, False
        else:
            print(f'{passenger.name} пройшов безпеку')
            return passenger, True


class BoardingZone(Zone):
    def __init__(self, name):
        super().__init__(name)

    def serve_passenger(self):
        if self.passengers.empty():
            return None
        priority, passenger = self.passengers.get()
        print(f'{passenger.name} успішно сів у літак ')
        return passenger, True


class Airport:
    def __init__(self):
        self.zones = {
            "register": RegistrationZone("Реєстрація"),
            "security_control": SecurityZone("Контроль безпеки"),
            "boarding": BoardingZone("Посадка")
        }

    def add_passenger(self, passenger: Passenger):
        self.zones["register"].add(passenger)

    def serve_registration(self):
        result = self.zones['register'].serve_passenger()
        if result and result[1]:  # если успешно
            self.zones['security_control'].add(result[0])

    def serve_security_control(self):
        result = self.zones['security_control'].serve_passenger()
        if result and result[1]:
            self.zones['boarding'].add(result[0])

    def serve_boarding(self):
        self.zones['boarding'].serve_passenger()






airport = Airport()
p1 = Passenger("Іван", 2, ["ticket", "bag"])
p2 = Passenger("Марія", 1, ["ticket", "knife"])
p3 = Passenger("Андрій", 3, ["bag"])  # без квитка

airport.add_passenger(p1)
airport.add_passenger(p2)
airport.add_passenger(p3)


airport.serve_registration()
airport.serve_registration()
airport.serve_registration()

airport.serve_security_control()
airport.serve_security_control()

airport.serve_boarding()