from weapon import *

class Enemy:
    def __init__(self, power, dexterity, stamina):
        self.power = power
        self.dexterity = dexterity
        self.stamina = stamina

    def feature():
        pass

    def reward():
        pass


class Goblin(Enemy):
    def __init__(self, power=1, dexterity=1, stamina=1):
        super().__init__(power, dexterity, stamina)
        self.health = 5
        self.damage = 2

    def feature(self):
        pass

    def reward(self):
        return Dagger()


class Skeleton(Enemy):
    def __init__(self, power=2, dexterity=2, stamina=1):
        super().__init__(power, dexterity, stamina)
        self.health = 10
        self.damage = 2

    def feature(self, weapon_person):
        if weapon_person.type_damage == "Дробящий":
            return 1
        return 0

    def reward(self):
        return Cudgel()


class Slime(Enemy):
    def __init__(self, power=3, dexterity=1, stamina=2):
        super().__init__(power, dexterity, stamina)
        self.health = 8
        self.damage = 1

    def feature(self, weapon_person=None):
        if weapon_person.type_damage == "Рубящий":
            return 1
        return 0

    def reward(self):
        return Spear()


class Ghost(Enemy):
    def __init__(self, power=1, dexterity=3, stamina=1):
        super().__init__(power, dexterity, stamina)
        self.health = 6
        self.damage = 3

    def feature(self, weapon_person=None):
        return self.damage + 1

    def reward(self):
        return Sword()


class Golem(Enemy):
    def __init__(self, power=3, dexterity=1, stamina=3):
        super().__init__(power, dexterity, stamina)
        self.health = 10
        self.damage = 1

    def feature(self, weapon_person=None):
        return weapon_person - self.stamina

    def reward(self):
        return Axe()


class Dragon(Enemy):
    def __init__(self, power=3, dexterity=3, stamina=3):
        super().__init__(power, dexterity, stamina)
        self.health = 20
        self.damage = 4

    def feature(self, weapon_person=None):
        if weapon_person == 3:
            return self.damage + 3
        return 0

    def reward(self):
        return Legendary_sword()
