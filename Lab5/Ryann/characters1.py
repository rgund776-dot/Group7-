from abc import ABC, abstractmethod

class Character(ABC):

    def __init__(self, name: str, health: int):
        # Common attributes shared by all characters
        self.name = name
        self.health = health

    @abstractmethod
    def save(self, filename: str) -> None:
        # Forces subclasses to implement file saving
        pass

    @abstractmethod
    def __repr__(self) -> str:
        # Forces subclasses to define how the object is represented as a string
        pass

    def __str__(self):
        # Ensures print() uses the same format as __repr__
        return self.__repr__()


class Fighter(Character):

    def __init__(self, name: str, health: int, speed: int):
        super().__init__(name, health)
        # Fighter-specific attribute: movement speed
        self.speed = speed

    def save(self, filename: str) -> None:
        # Saves fighter data in CSV format to file
        with open(filename, "a") as file:
            file.write(self.__repr__() + "\n")

    def __repr__(self) -> str:
        # String format used for saving and debugging
        return f"Fighter,{self.name},{self.health},{self.speed}"


class Mage(Character):

    def __init__(self, name: str, health: int, mana: int):
        super().__init__(name, health)
        # Mage-specific attribute: mana resource
        self.mana = mana

    def save(self, filename: str) -> None:
        # Saves mage data in CSV format to file
        with open(filename, "a") as file:
            file.write(self.__repr__() + "\n")

    def __repr__(self) -> str:
        # String format used for saving and debugging
        return f"Mage,{self.name},{self.health},{self.mana}"