import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations, combinations_with_replacement

# class Tire:
#     def __init__(self, name, Tmin, Tmax, alpha, beta ):
#         self.name = name
#         self.tMin = Tmin
#         self.tMax = Tmax
#         self.alpha = alpha
#         self.beta = beta

class RaceSimulator:
    """
    Simulates an F1 race strategy by calculating the time added
    from tire degradation and pit stops.
    """

    def __init__(self, soft_tire, medium_tire, hard_tire, pit_stop_time_1 , pit_stop_time_2 , total_laps, pit_stop_time = 25):
        """
        Initialize the simulator and store tire data.
        """
        # self.tires = [soft_tire, medium_tire, hard_tire]
        self.tires = pd.DataFrame({
            "Tmin": [0, 1, 2], 
            "Tmax": [10, 10, 10],
            "alpha": [1/2, 1/4, 1/16], 
            "beta": [15, 25, 55]},
            index=["soft", "medium", "hard"])
        self.pit_stop_time = pit_stop_time
        self.pit_stop_time_1 = pit_stop_time_1
        self.pit_stop_time_2 = pit_stop_time_2
        self.total_laps = total_laps


    def tire_time(self, age, Tmin, Tmax, alpha, beta):
        """
        Calculate the time added due to tire degradation.

        Parameters:
            age: Tire age in laps.
            Tmin: Minimum time added by the tire.
            Tmax: Maximum time added by the tire.
            alpha: Tire degradation rate parameter.
            beta: Tire degradation midpoint parameter.

        Returns:
            Tire time added for the given tire age.
        """
        return Tmin + (Tmax - Tmin) / (1 + np.exp(-alpha * (age - beta)))


    def simulate(self, stint_lengths, tire_types):
        """
        Simulate a complete race strategy.

        Parameters:
            stint_lengths: Length of each race stint.
            tire_types: Tire compound used for each stint.

        Returns:
            Total time added from tire degradation and pit stops.
        """
        pass


def plot_tires(simulator: RaceSimulator):
    """
    Plot tire degradation curves for all tire compounds.

    Parameters:
        simulator: A RaceSimulator object containing tire data.

    Returns:
        None.
    """
    pass


def find_best_strategy(simulator: RaceSimulator):
    """
    Test all valid race strategies and find the one
    with the minimum total time added.

    Parameters:
        simulator: A RaceSimulator object.

    Returns:
        The strategy with the lowest total tire and pit time.
    """
    pass