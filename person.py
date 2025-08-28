from weapon import *

class Person():
    def __init__(self, power, dexterity, stamina):
        self.power = power
        self.dexterity = dexterity
        self.stamina = stamina


class Robber(Person):
    def __init__(self, power, dexterity, stamina):
        super().__init__(power, dexterity, stamina)
        self.my_weapon = Dagger("Колющий", 2 + self.power)
        self.health = 4 + self.stamina


class Warrior(Person):
    def __init__(self, power, dexterity, stamina):
        super().__init__(power, dexterity, stamina)
        self.my_weapon = Sword("Рубящий", 3 + self.power)
        self.health = 5 + self.stamina


class Barbarian(Person):
    def __init__(self, power, dexterity, stamina):
        super().__init__(power, dexterity, stamina)
        self.my_weapon = Cudgel("Дробящий", 3 + self.power)
        self.health = 6 + self.stamina
