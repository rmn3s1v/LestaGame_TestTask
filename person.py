from weapon import *

class Person():
    def __init__(self, power, dexterity, stamina):
        self.power = power
        self.dexterity = dexterity
        self.stamina = stamina

    def bonus_first_lvl(self):
        pass

    def bonus_second_lvl(self):
        pass

    def bonus_third_lvl(self):
        pass

    def return_health(self):
        pass

class Robber(Person):
    def __init__(self, power, dexterity, stamina):
        super().__init__(power, dexterity, stamina)
        self.my_weapon = Dagger(self.power)
        self.health = 4 + self.stamina
        self.lvl = 1
        self.one_use = True

    def bonus_first_lvl(self):
        return self.my_weapon.damage + 1

    def bonus_second_lvl(self):
        if self.one_use:
            self.dexterity += 1
            self.one_use = False

    def poison(self, start=1, step=1):
        current = start
        while True:
            yield current
            current += step

    def bonus_third_lvl(self):
        return self.my_weapon.damage + self.poison()

    def return_health(self):
        self.health = 4 + self.stamina


class Warrior(Person):
    def __init__(self, power, dexterity, stamina):
        super().__init__(power, dexterity, stamina)
        self.my_weapon = Sword(self.power)
        self.health = 5 + self.stamina
        self.lvl = 1
        self.one_use = True

    def bonus_first_lvl(self):
        return self.my_weapon.damage * 2

    def bonus_second_lvl(self, damage_enemy):
        return damage_enemy - 3

    def bonus_third_lvl(self):
        if self.one_use:
            self.power += 1
            if isinstance(self.my_weapon, Sword):
                self.my_weapon = Sword((self.power))
            elif isinstance(self.my_weapon, Cudgel):
                self.my_weapon = Cudgel((self.power))
            elif isinstance(self.my_weapon, Dagger):
                self.my_weapon = Dagger((self.power))
            elif isinstance(self.my_weapon, Axe):
                self.my_weapon = Axe((self.power))
            elif isinstance(self.my_weapon, Spear):
                self.my_weapon = Spear((self.power))
            else:
                self.my_weapon = Legendary_sword((self.power))

            self.one_use = False

    def return_health(self):
        self.health = 5 + self.stamina

class Barbarian(Person):
    def __init__(self, power, dexterity, stamina):
        super().__init__(power, dexterity, stamina)
        self.my_weapon = Cudgel(self.power)
        self.health = 6 + self.stamina
        self.lvl = 1
        self.one_use = True

    def bonus_first_lvl(self, round):
        if round <= 3:
            return self.my_weapon.damage + 2
        else:
            if self.one_use:
                self.my_weapon.damage -= 1
                self.one_use = False
            return -1

    def bonus_second_lvl(self, damage_enemy):
        return damage_enemy - self.stamina

    def return_health(self):
        self.health = 6 + self.stamina
