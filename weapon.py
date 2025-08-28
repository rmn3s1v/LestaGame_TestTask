class Weapon:
    def __init__(self, type_damage, damage):
        self.type_damage = type_damage
        self.damage = damage


class Sword(Weapon):
    def __init__(self, type_damage, damage):
        super().__init__(type_damage, damage)


class Cudgel(Weapon):
    def __init__(self, type_damage, damage):
        super().__init__(type_damage, damage)


class Dagger(Weapon):
    def __init__(self, type_damage, damage):
        super().__init__(type_damage, damage)


class Axe(Weapon):
    def __init__(self, type_damage, damage):
        super().__init__(type_damage, damage)


class Spear(Weapon):
    def __init__(self, type_damage, damage):
        super().__init__(type_damage, damage)


class Legendary_sword(Weapon):
    def __init__(self, type_damage, damage):
        super().__init__(type_damage, damage)
