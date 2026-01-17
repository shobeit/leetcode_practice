def meditate(mana, max_mana, num_potions):
    while mana < max_mana and num_potions >= 1:
        num_potions -= 1
        mana += 1
    return mana, num_potions