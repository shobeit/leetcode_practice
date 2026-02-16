class Wizard:
    def __init__(self, name, stamina, intelligence):
        self.name = name
        self.__stamina = stamina
        self.__intelligence = intelligence
        self.mana = self.__intelligence * 10
        self.health = self.__stamina * 100

    # don't touch above this line

    def get_fireballed(self, fireball_damage):
        # Reduce the damage by the wizard's stamina
        damage_taken = fireball_damage - self.__stamina
        # Reduce the wizard's health by the remaining damage
        self.health -= damage_taken

    def drink_mana_potion(self, potion_mana):
        # Increase the potion's effectiveness by the wizard's intelligence
        mana_regained = potion_mana + self.__intelligence
        # Increase the wizard's mana pool
        self.mana += mana_regained