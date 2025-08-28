class Enemy:
    def __init__(self, power, dexterity, stamina):
        self.power = power
        self.dexterity = dexterity
        self.stamina = stamina


class Goblin(Enemy):
    def __init__(self, power=1, dexterity=1, stamina=1):
        super().__init__(power, dexterity, stamina)
        self.healt = 5
        self.damage = 2


class Skeleton(Enemy):
    def __init__(self, power=2, dexterity=2, stamina=1):
        super().__init__(power, dexterity, stamina)
        self.healt = 10
        self.damage = 2


class Ghost(Enemy):
    def __init__(self, power=1, dexterity=3, stamina=1):
        super().__init__(power, dexterity, stamina)
        self.healt = 6
        self.damage = 3


class Golem(Enemy):
    def __init__(self, power=3, dexterity=1, stamina=3):
        super().__init__(power, dexterity, stamina)
        self.healt = 10
        self.damage = 1


class Dragon(Enemy):
    def __init__(self, power=3, dexterity=3, stamina=3):
        super().__init__(power, dexterity, stamina)
        self.healt = 20
        self.damage = 4
