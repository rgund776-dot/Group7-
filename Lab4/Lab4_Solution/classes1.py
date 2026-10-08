
class Driver:

    def __init__(self, name: str, points: int):
        """
        :param name: the driver's name
        :param points: points scored by this driver
        """
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
        """
        :param name: the team's name
        """
        self.name = name
        self.drivers = []

    def add_driver(self, driver: Driver) -> None:
        """
        adds a Driver to this team (by appending it to self.drivers)
        :param driver: the Driver object to add to this Team
        """
        self.drivers.append(driver)

    def get_total_points(self) -> int:
        """
        :return: sum of points scored by this team's Drivers
        """
        result = 0
        for driver in self.drivers:
            if not isinstance(driver.points, int):
                raise ValueError(f"Driver points must be an integer. Issue with  {driver.name}")
            result += driver.points
        return result

    def __repr__(self) -> str:
        """
        This method defines what the human-readable string version of the Team object is.
        It should return a string that describes this Team, for example:
        "FERRARI with drivers Carlos Sainz, Charles Leclerc. Total pts: 406"
        """
        driver_names = ', '.join(driver.name for driver in self.drivers)
        return f"{self.name} with drivers {driver_names}. Total pts: {self.get_total_points()}"
    
    def __lt__(self, other) -> bool:
        """
        This method defines what "less than" means for the Team object
        It should return True if this Team (self) is "less than" another.
        In this case, it should return True if this team has less total points that the other.
        :param other: another Team object
        :return: True if this Team has less points than other
        """
        return self.get_total_points() < other.get_total_points()
