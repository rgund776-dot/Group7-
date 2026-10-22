from abc import ABC, abstractmethod

class Weapon(ABC):
    """
    Abstract base class for all weapon types.
    """

    def __init__(self, name: str, damage: int):
        self.name = name
        self.damage = damage

    def save(self, filename: str) -> None:
        with open(filename, "a") as file:
            file.write(self.__repr__() + "\n")

    @abstractmethod
    def __repr__(self) -> str:
        """
        Return a string representation of the weapon.
        Subclasses must implement this method.
        """
        pass

    def __str__(self) -> str:
        return self.__repr__()


class MeleeWeapon(Weapon):
    """
    Represents a melee weapon.
    """
    def __repr__(self) -> str:
        return f"MeleeWeapon,{self.name},{self.damage}"

class RangedWeapon(Weapon):
    """
    Represents a ranged weapon.
    """

    def __init__(self, name: str, damage: int, range: int):
        super().__init__(name, damage)
        self.range = range

    def __repr__(self) -> str:
        return f"RangedWeapon,{self.name},{self.damage},{self.range}"


class MagicWeapon(Weapon):
    """
    Represents a magic weapon.
    """

    def __init__(self, name: str, damage: int, range: int, mana_cost: int):
        super().__init__(name, damage)
        self.range = range
        self.mana_cost = mana_cost

    def __repr__(self) -> str:
        return f"MagicWeapon,{self.name},{self.damage},{self.range},{self.mana_cost}"