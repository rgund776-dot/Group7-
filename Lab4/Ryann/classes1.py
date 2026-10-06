
class Driver:

    def __init__(self, name: str, points: int):

        self.name = name
        self.points = points

    def __repr__(self) -> str:
        """
        This method defines what the human-readable string version of the Driver object is.
        It should return a string that describes this Driver. For example:
        "Carlos Sainz (200 pts)"
        """
        return f"{self.name} ({self.points} pts)"


class Team:

    def __init__(self, name: str):
        
        self.name = name
        self.drivers = []

    def add_driver(self, driver: Driver) -> None:
       
        self.drivers.append(driver)
        

    def get_total_points(self) -> int:
        """
        :return: sum of points scored by this team's Drivers
        """
        points = 0

        for driver in self.drivers:
            total += driver.points

        return total


    def __repr__(self) -> str:
        """
        This method defines what the human-readable string version of the Team object is.
        It should return a string that describes this Team, for example:
        "FERRARI with drivers Carlos Sainz, Charles Leclerc. Total pts: 406"
        """
        pass # your code here
    
    def __lt__(self, other) -> bool:
        """
        This method defines what "less than" means for the Team object
        It should return True if this Team (self) is "less than" another.
        In this case, it should return True if this team has less total points that the other.
        :param other: another Team object
        :return: True if this Team has less points than other
        """
        pass # your code here
