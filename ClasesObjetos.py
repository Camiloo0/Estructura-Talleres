class Dog:
    def __init__(self, size="Medium", color="Blue", race="Husky", price=5000):
        self.size = size
        self.color = color
        self.race = race
        self.price = price


rufo = Dog()
print(f"{rufo.size}:{rufo.color}:{rufo.race}:{rufo.price}")

bolt = Dog("Small", "Gold", "Samoyed", "Free")
print(f"{bolt.size}:{bolt.color}:{bolt.race}:{bolt.price}")

bruce = Dog("Big", "White", "Pug", "Free")
print(f"{bruce.size}:{bruce.color}:{bruce.race}:{bruce.price}")

zeus = Dog("Big", "Brown", "German Shepherd", "Free")
print(f"{zeus.size}:{zeus.color}:{zeus.race}:{zeus.price}")

thanos = Dog("Big", "Gold", "Golden Retriever", "Free")
print(f"{thanos.size}:{thanos.color}:{thanos.race}:{thanos.price}")


class Cat:
    def __init__(self, size="Small", color="Black", race="Persian", price=1000):
        self.size = size
        self.color = color
        self.race = race
        self.price = price

michi = Cat()
print(f"{michi.size}:{michi.color}:{michi.race}:{michi.price}")

luna = Cat("Small", "White", "Siamese", "Free")
print(f"{luna.size}:{luna.color}:{luna.race}:{luna.price}")

tom = Cat("Medium", "Gray", "British Shorthair", 1500)
print(f"{tom.size}:{tom.color}:{tom.race}:{tom.price}")

garfield = Cat("Large", "Orange", "Exotic Shorthair", 2000)
print(f"{garfield.size}:{garfield.color}:{garfield.race}:{garfield.price}")

salem = Cat("Medium", "Black", "Bombay", "Free")
print(f"{salem.size}:{salem.color}:{salem.race}:{salem.price}")

class Bird:
    def __init__(self, size="Small", color="Green", species="Parrot", price=500):
        self.size = size
        self.color = color
        self.species = species
        self.price = price

piolin = Bird()
print(f"{piolin.size}:{piolin.color}:{piolin.species}:{piolin.price}")

kiwi = Bird("Tiny", "Yellow", "Canary", 300)
print(f"{kiwi.size}:{kiwi.color}:{kiwi.species}:{kiwi.price}")

sky = Bird("Small", "Blue", "Budgerigar", "Free")
print(f"{sky.size}:{sky.color}:{sky.species}:{sky.price}")

zazu = Bird("Medium", "Multicolor", "Macaw", 2500)
print(f"{zazu.size}:{zazu.color}:{zazu.species}:{zazu.price}")

tweety = Bird("Tiny", "Yellow", "Finch", 100)
print(f"{tweety.size}:{tweety.color}:{tweety.species}:{tweety.price}")
