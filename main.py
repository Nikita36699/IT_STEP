class Dog:
    def __init__(self,name,age,breed = 'labrador'):
        #self -- це объебкт классу(конктретний песик)
        print('Hello from Dog.__innit__')
        #створення атрибуту name
        self.name = name

        self.age = age
        self.breed = breed

    def eat(self,food):
        print(f'{self.name} is eating {food}')

    def grow(self):
        """
        пес подорослішав на один рік 
        """
        self.age += 1

    def get_name(self):
        return  self.name

#створення кокретного пса

dog1 = Dog(name='tuzik',age=5)

print(dog1.name)
print(dog1.age)
print(dog1.breed)

#створення іншого пса

dog2 = Dog(name='barsik',age=2,breed='haski')
print(dog2.name)
print(dog2.age)
print(dog2.breed)

print()

dog1.eat('bone')
dog2.eat('meat')

print()

print(dog1.age )
dog1.grow()
print(dog1.age)

print()

name = dog1.get_name()
print(name)

#атрибути можна змінювати але не бажано
dog = Dog(name='tuzik', age = 5)
dog.age += 2
dog.color = 'brown'


