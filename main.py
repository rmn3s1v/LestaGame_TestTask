from person import *
from enemy import *
import random

def create_new_class(choice):
    if choice == 1:
        return Robber(random.randint(0,3), random.randint(0,3), random.randint(0,3))
    elif choice == 2:
        return Warrior(random.randint(0,3), random.randint(0,3), random.randint(0,3))
    else:
        return Barbarian(random.randint(0,3), random.randint(0,3), random.randint(0,3))

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
    second_person_g = None
    third_person_g = None

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
            print(f"Your dexterity {person_g.dexterity}, enemy dexterity {enemy.dexterity}. Enemy better. He first attack")
            firts_damage = False
        else:
            print(f"Your dexterity {person_g.dexterity}, enemy dexterity {enemy.dexterity}. You better. You first attack")

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
                    if second_person_g == None:
                        damage = get_damage(person_g, enemy, firts_damage, round)
                        print(f"Your damage: {damage}")
                        enemy.health -= damage
                        print(f"Enemy health: {enemy.health}")
                    elif second_person_g != None and third_person_g == None:
                        damage = get_damage(person_g, enemy, firts_damage, round)
                        damage += get_damage(second_person_g, enemy, firts_damage, round)
                        print(f"Your damage: {damage}")
                        enemy.health -= damage
                        print(f"Enemy health: {enemy.health}")
                    else:
                        damage = get_damage(person_g, enemy, firts_damage, round)
                        damage += get_damage(second_person_g, enemy, firts_damage, round)
                        damage += get_damage(third_person_g, enemy, firts_damage, round)
                        print(f"Your damage: {damage}")
                        enemy.health -= damage
                        print(f"Enemy health: {enemy.health}")

                if enemy.health <= 0:
                    print(f"Round:{round}, Lvl:{lvl + 1} - Win! Next!")
                    person_g.return_health()
                    print(f"You health is restored: {person_g.health}")
                    print("Select person: \n1 - Robber\n2 - Warrior\n3 - Barbarian\nIf you choice your person, he are lvlup")
                    choice = int(input())
                    if choice == 1 and isinstance(person_g, Robber):
                        person_g.lvl += 1
                    elif choice == 2 and isinstance(person_g, Warrior):
                        person_g.lvl += 1
                    elif choice == 3 and isinstance(person_g, Barbarian):
                        person_g.lvl += 1
                    elif choice == 1 and isinstance(second_person_g, Robber):
                        second_person_g.lvl += 1
                    elif choice == 2 and isinstance(second_person_g, Warrior):
                        second_person_g.lvl += 1
                    elif choice == 3 and isinstance(second_person_g, Barbarian):
                        second_person_g.lvl += 1
                    elif choice == 1 and isinstance(third_person_g, Robber):
                        second_person_g.lvl += 1
                    elif choice == 2 and isinstance(third_person_g, Warrior):
                        second_person_g.lvl += 1
                    elif choice == 3 and isinstance(third_person_g, Barbarian):
                        second_person_g.lvl += 1
                    else:
                        if second_person_g == None:
                            second_person_g = create_new_class(choice)
                            person_g.health += second_person_g.health
                            person_g.dexterity += second_person_g.dexterity
                            person_g.stamina += second_person_g.stamina

                        elif third_person_g == None:
                            third_person_g = create_new_class(choice)
                            person_g.health += third_person_g.health
                            person_g.dexterity += third_person_g.dexterity
                            person_g.stamina += third_person_g.stamina

                    if second_person_g == None:
                        print(f"You level: {person_g.lvl}")
                    elif second_person_g != None and third_person_g == None:
                        print(f"You level: {person_g.lvl} and {second_person_g.lvl}")
                    else:
                        print(f"You level: {person_g.lvl} and {second_person_g.lvl} and {third_person_g.lvl}")

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
                    if second_person_g == None:
                        damage = get_damage(person_g, enemy, firts_damage, round)
                        print(f"Enemy damage: {damage}")
                        person_g.health -= damage
                        print(f"You health: {person_g.health}")
                    elif second_person_g != None and third_person_g == None:
                        damage = get_damage(person_g, enemy, firts_damage, round)
                        damage2 = get_damage(second_person_g, enemy, firts_damage, round)
                        damage = min(damage, damage2)
                        print(f"Enemy damage: {damage}")
                        person_g.health -= damage
                        print(f"You health: {person_g.health}")
                    else:
                        damage = get_damage(person_g, enemy, firts_damage, round)
                        damage2 = get_damage(second_person_g, enemy, firts_damage, round)
                        damage3 = get_damage(second_person_g, enemy, firts_damage, round)
                        damage = min(damage, damage2, damage3)
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
