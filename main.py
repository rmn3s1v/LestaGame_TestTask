from person import *
from enemy import *
import random

def check_attack(person_g, enemy):
    if random.randint(1, person_g.dexterity + enemy.dexterity) <= enemy.dexterity:
        return 0
    return 1

def person_feature_defense(enemy, person_g, damage):
    if isinstance(person_g, Warrior):
        if enemy.power < person_g.power and person_g.lvl > 1:
            damage = person_g.bonus_second_lvl(damage)
        return damage
    elif isinstance(person_g, Barbarian):
        if person_g.lvl > 1:
            damage = person_g.bonus_second_lvl(damage)
            if damage < 0:
                damage = 0
        return damage
    else:
        return damage

def enemy_feature_defense(enemy, person_g, damage, round):
    if isinstance(enemy, Skeleton):
        if enemy.feature(person_g.my_weapon):
            return damage * 2
        return damage
    elif isinstance(enemy, Slime):
        if isinstance(person_g, Warrior) and round == 1:
            return damage
        elif enemy.feature(person_g.my_weapon):
            return person_g.power
        return damage
    elif isinstance(enemy, Golem):
        return enemy.feature(damage)
    else:
        return damage

def get_damage(person_g, enemy, attack, round):
    sum_damage = 0

    if attack:
        if isinstance(person_g, Robber):
            if person_g.lvl == 1:
                if person_g.dexterity > enemy.dexterity:
                    sum_damage += person_g.bonus_first_lvl()
                else:
                    sum_damage += person_g.my_weapon.damage
                sum_damage = enemy_feature_defense(enemy, person_g,sum_damage, round)
            elif person_g.lvl == 2:
                person_g.bonus_second_lvl()
                if person_g.dexterity > enemy.dexterity:
                    sum_damage += person_g.bonus_first_lvl()
                else:
                    sum_damage += person_g.my_weapon.damage
                sum_damage = enemy_feature_defense(enemy, person_g,sum_damage, round)
            else:
                if person_g.dexterity > enemy.dexterity:
                    sum_damage += person_g.bonus_first_lvl()
                sum_damage += person_g.bonus_third_lvl()
                sum_damage = enemy_feature_defense(enemy, person_g,sum_damage, round)

        elif isinstance(person_g, Warrior):
            if person_g.lvl == 1:
                if round == 1:
                    sum_damage += person_g.bonus_first_lvl()
                else:
                    sum_damage += person_g.my_weapon.damage
                sum_damage = enemy_feature_defense(enemy, person_g,sum_damage, round)
            else:
                if person_g.lvl == 3:
                    person_g.bonus_third_lvl()
                if round == 1:
                    sum_damage += person_g.bonus_first_lvl()
                else:
                    sum_damage += person_g.my_weapon.damage
                sum_damage = enemy_feature_defense(enemy, person_g,sum_damage, round)

        elif isinstance(person_g, Barbarian):
            if person_g.bonus_first_lvl(round) != -1:
                sum_damage += person_g.bonus_first_lvl(round)
                sum_damage = enemy_feature_defense(enemy, person_g,sum_damage, round)
            else:
                sum_damage = person_g.my_weapon.damage
                sum_damage = enemy_feature_defense(enemy, person_g, sum_damage, round)
    else:
        if isinstance(enemy, Ghost):
            if person_g.dexterity < enemy.dexterity:
                sum_damage += enemy.feature()
            else:
                sum_damage += enemy.damage
            sum_damage = person_feature_defense(enemy, person_g, sum_damage)
        elif isinstance(enemy, Dragon):
            if round % 3 == 0:
                sum_damage += enemy.feature()
            else:
                sum_damage += enemy.damage
            sum_damage = person_feature_defense(enemy, person_g, sum_damage)
        else:
            sum_damage = person_feature_defense(enemy, person_g, enemy.damage)
    return sum_damage

def main():
    person_g = None

    print("Insert you person: \n1 - Robber\n2 - Warrior\n3 - Barbarian")
    choice = int(input())

    if choice == 1:
        person_g = Robber(random.randint(0,3), random.randint(0,3), random.randint(0,3))

    elif choice == 2:
        person_g = Warrior(random.randint(0,3), random.randint(0,3), random.randint(0,3))

    elif choice == 3:
        person_g = Barbarian(random.randint(0,3), random.randint(0,3), random.randint(0,3))

    else:
        print("Incorrected insert. Exit game!")
        return 0

    for lvl in range(3):
        print("------")
        print(f"Lvl: {lvl+1}")
        round = 1
        enemy = None
        enemys = random.randint(0,5)
        if enemys == 0:
            enemy = Goblin()
        elif enemys == 1:
            enemy = Skeleton()
        elif enemys == 2:
            enemy = Slime()
        elif enemys == 3:
            enemy = Ghost()
        elif enemys == 4:
            enemy = Golem()
        else:
            enemy = Dragon()

        firts_damage = True

        if person_g.dexterity < enemy.dexterity:
            firts_damage = False

        print("-------------")
        print(f"Your details:\nHealth: {person_g.health}\nLvl: {person_g.lvl}\nDamage: {person_g.my_weapon.damage}\nPower: {person_g.power}\nDexterity: {person_g.dexterity}\nStamina: {person_g.stamina}")
        print("-------------")
        print(f"Enemy details:\nHealth: {enemy.health}\nDamage: {enemy.damage}\nPower:{enemy.power}\nDexterity: {enemy.dexterity}\nStamina: {enemy.stamina}")
        print("-------------")

        while round:
            if firts_damage:
                if not check_attack(person_g, enemy):
                    firts_damage = False
                    round += 1
                    print("You missing. Enemy attack")
                    continue
                else:
                    damage = get_damage(person_g, enemy, firts_damage, round)
                    print(f"Your damage: {damage}")
                    enemy.health -= damage
                    print(f"Enemy health: {enemy.health}")

                if enemy.health <= 0:
                    print(f"Round:{round} Win! Next!")
                    person_g.return_health()
                    print(f"You health is restored: {person_g.health}")
                    person_g.lvl += 1
                    print(f"You level is up: {person_g.lvl}")
                    round = 0
                    new_weapon = enemy.reward()
                    print(f"Do you want to take weapon from mob ({new_weapon.name})?\n1-yes\n2-no")
                    choice = int(input())
                    if choice == 1:
                        person_g.my_weapon = enemy.reward()

                    continue

                firts_damage = False

            else:
                if not check_attack(enemy, person_g):
                    firts_damage = True
                    round += 1
                    print("Enemy missing. Your attack")
                    continue
                else:
                    damage = get_damage(person_g, enemy, firts_damage, round)
                    print(f"Enemy damage: {damage}")
                    person_g.health -= damage
                    print(f"You health: {person_g.health}")

                if person_g.health <= 0:
                    print(f"Round:{round} Lose! Game over!")
                    print(f"Health enemy: {enemy.health}")
                    exit(0)

                firts_damage = True

            round += 1

    print("YOU WIN THIS GAME!")

if __name__ == "__main__":
    main()
