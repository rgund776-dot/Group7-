from abc import ABC, abstractmethod


class Weapon(ABC):
    def __init__(self,name: str, damage: int):
        self.name = name
        self.damage = damage 
        
    
    @abstractmethod
    def save(self, filename: str) -> None:
        pass
    
    
    @abstractmethod
    def __repr__(self) -> str:
        pass 
    
    def __str__(self):
        return self.__repr__()
    
    
    
class MeleeWeapon(Weapon):
    def __init__(self,name:str, damage: int):
        super().__init__(name, damage)
        
    def save(self, filename:str) -> None:
        with open(filename, "a") as file:
            file.write(self.__repr__() + "\n")
            
    def __repr__(self) -> str:
        return f"MeleeWeapon, {self.name},{self.damage}"
    
    
class RangedWeapon(Weapon):
    def __init__(self, name: str, damage: int, range: int):
        super().__init__(name, damage)
        self.range = range 
    
    def save(self, filename: str) -> None:
        with open(filename, "a") as file:
            file.write(self.__repr__() + "\n")
    
    def __repr__(self) -> str:
        return f"RangedWeapon,{self.name},{self.damage},{self.range}"
    
    
    
class MagicWeapon(Weapon):
    def __init__(self, name: str, damage: int, range: int, mana_cost: int):
        super().__init__(name, damage)
        self.range = range
        self.mana_cost = mana_cost
        
    def save(self, filename: str) -> None:
        with open(filename, "a") as file:
            file.write(self.__repr__() + "\n")
            
    def __repr__(self) -> str:
        return f"MagicWeapon,{self.name},{self.damage},{self.range},{self.mana_cost}"
                  
    