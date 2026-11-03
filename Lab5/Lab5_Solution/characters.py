from abc import ABC, abstractmethod


class Character(ABC):
    """
    Abstract base class for all character types.
    """

    def __init__(self, name: str, health: int):
        self.name = name
        self.health = health

    @abstractmethod
    def save(self, filename: str) -> None:
        """
        Save character information to a file.
        Subclasses must implement this method.
        """
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """
        Return a string representation of the character.
        Subclasses must implement this method.
        """
        pass

    def __str__(self) -> str:
        return self.__repr__()


class Fighter(Character):
    """
    Represents a fighter character.
    """

    def __init__(self, name: str, health: int, speed: int):
        super().__init__(name, health)
        self.speed = speed

    def save(self, filename: str) -> None:
        with open(filename, "a") as file:
            file.write(self.__repr__() + "\n")

    def __repr__(self) -> str:
        return f"Fighter,{self.name},{self.health},{self.speed}"


class Mage(Character):
    """
    Represents a mage character.
    """

    def __init__(self, name: str, health: int, mana: int):
        super().__init__(name, health)
        self.mana = mana

    def save(self, filename: str) -> None:
        with open(filename, "a") as file:
            file.write(self.__repr__() + "\n")

    def __repr__(self) -> str:
        return f"Mage,{self.name},{self.health},{self.mana}"