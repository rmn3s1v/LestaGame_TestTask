class Weapon:
    def __init__(self, type_damage, damage):
        self.type_damage = type_damage
        self.damage = damage


class Sword(Weapon):
    def __init__(self, damage=0):
        super().__init__("Рубящий", 3 + damage)


class Cudgel(Weapon):
    def __init__(self, damage=0):
        super().__init__("Дробящий", 3 + damage)


class Dagger(Weapon):
    def __init__(self, damage=0):
        super().__init__("Колющий", 2 + damage)


class Axe(Weapon):
    def __init__(self, damage=0):
        super().__init__("Рубящий", 4 + damage)


class Spear(Weapon):
    def __init__(self, damage=0):
        super().__init__("Колющий", 3 + damage)


class Legendary_sword(Weapon):
    def __init__(self, damage=0):
        super().__init__("Рубящий", 5 + damage)
