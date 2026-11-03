from characters import Character
from characters import Mage 
from characters import Fighter

from weapons2 import Weapon  
from weapons2 import Magic
from weapons2 import Melee
from weapons2 import Ranged

def attack(attacker: Character, weapon: Weapon, target: Character, distance: int) -> None:
    # only Mages can use a MagicWeapon
    if not isinstance(attacker, Mage) and isinstance(weapon, Magic):
        raise TypeError ("Only mages can use a magic weapon!")

    # only weapons that have a range attribute can be used at distances > 0
    # weapons that have a range cannot be used at distances above that range
    if hasattr(weapon, "range"):
        if distance > weapon.range:
            raise TypeError ("Target not within range!")
    if isinstance(weapon, Melee) and distance != 0:
        raise TypeError ("Target not within range!")    

    # if a mage doesn't have enough mana
    if isinstance(attacker, Mage):
        if weapon.mana > attacker.mana:
            raise ValueError ("Not enough mana to use this weapon!")
        attacker.mana = attacker.mana - weapon.mana  
        print(f"{attacker.name} has {attacker.mana} left!")

    # if target hp hits zero:
    if 0 >= (target.health - weapon.dmg):
        target.health = 0
        print(f"{attacker.name} hit {target.name} for {weapon.dmg}!")
        print(f"{target.name} has been defeated!")
    else:
        target.health = target.health - weapon.dmg
        print(f"{attacker.name} hit {target.name} for {weapon.dmg} hp!")
        print(f"{target.name} has {target.health} hp left!")

# sample characters
fighter = Fighter("Aragorn", 100, 20)
mage = Mage("Gandalf", 80, 50)
sword = Melee("Andúril", 25)
staff = Magic("Wizard Staff", 15, 20, 10)
bow = Ranged("Mirkwood Bow", 5, 50)

# test cases:
#normal case melee
attack(fighter, sword, mage, 0)

# normal case magic
attack(mage, staff, fighter, 10)

# normal case ranged
attack(fighter, bow, mage, 40)

# mage only weapon
attack(fighter, staff, mage, 5)

# out of range
attack(fighter, bow, mage, 100)

# not enough mana
mage.mana = 5
attack(mage, staff, fighter, 5)

# defeat
mage.health = 30
attack(fighter, sword, mage, 0)