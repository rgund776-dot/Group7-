from characters import Character, Mage
from weapons import Weapon, MagicWeapon 



def attack(attacker: Character, weapon: Weapon, target: Character, distance: int) -> None: 
    
    if isinstance(weapon, MagicWeapon) and not isinstance(attacker, Mage):
        raise TypeError("Only mages use magic weapons")
        
    if not hasattr(weapon, "range") and distance > 0:
        raise ValueError("This weapon cannot be used at distance")
        
    if hasattr(weapon, "range") and distance > weapon.range:
        raise ValueError("Target is out of range")
        
        
    target.health = target.health - weapon.damage 
    
    
    