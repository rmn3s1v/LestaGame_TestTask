from person import Robber
import random

def main():
    p = Robber(random.randint(0, 3), random.randint(0, 3), random.randint(0, 3))

    print(p.power)
    print(p.dexterity)
    print(p.stamina)
    print(p.health)
    print(p.my_weapon.damage)

if __name__ == "__main__":
    main()
