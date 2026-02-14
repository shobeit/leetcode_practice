class Wizard:
    def __init__(self, name, stamina, intelligence):
        # Private properties
        self.__stamina = stamina
        self.__intelligence = intelligence
        
        # Public properties
        self.name = name
        self.health = stamina * 100
        self.mana = intelligence * 10