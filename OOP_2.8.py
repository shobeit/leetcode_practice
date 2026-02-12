def main():
    attacker1 = Brawler("Aragorn", 4, 4)
    attacker2 = Brawler("Gimli", 2, 7)
    attacker3 = Brawler("Legolas", 7, 7)
    attacker4 = Brawler("Frodo", 3, 2)

    fight(attacker1, attacker2)
    fight(attacker3, attacker4)


# don't touch below this line


class Brawler:
    def __init__(self, name, speed, strength):
        self.name = name
        self.speed = speed
        self.strength = strength
        self.power = speed * strength


def fight(attacker, defender):
    print(f"{attacker.name}: {attacker.power} power")
    print(f"{defender.name}: {defender.power} power")
    if attacker.power > defender.power:
        print(f"{attacker.name} wins!")
    elif attacker.power < defender.power:
        print(f"{defender.name} wins!")
    else:
        print("It's a tie!")
    print("---------------------------------")


main()
