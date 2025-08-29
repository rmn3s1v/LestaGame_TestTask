class Weapon:
    def __init__(self, type_damage, damage):
        self.type_damage = type_damage
        self.damage = damage


class Sword(Weapon):
    def __init__(self, damage=0):
        super().__init__("Рубящий", 3 + damage)
        self.name = "Меч"


class Cudgel(Weapon):
    def __init__(self, damage=0):
        super().__init__("Дробящий", 3 + damage)
        self.name = "Дубина"


class Dagger(Weapon):
    def __init__(self, damage=0):
        super().__init__("Колющий", 2 + damage)
        self.name = "Кинжал"


class Axe(Weapon):
    def __init__(self, damage=0):
        super().__init__("Рубящий", 4 + damage)
        self.name = "Топор"


class Spear(Weapon):
    def __init__(self, damage=0):
        super().__init__("Колющий", 3 + damage)
        self.name = "Копье"


class Legendary_sword(Weapon):
    def __init__(self, damage=0):
        super().__init__("Рубящий", 5 + damage)
        self.name = "Легендарный меч"
