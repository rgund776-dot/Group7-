import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations, combinations_with_replacement

RACE_LAPS = 60
PIT_TIME = 25

class RaceSimulator:
    """
    Simulates an F1 race strategy by calculating the time added
    from tire degradation and pit stops.
    """

    def __init__(self):
        """
        Initialize the simulator and store tire data.
        """
        self.tires = pd.DataFrame({
            "Tmin": [0, 1, 2], 
            "Tmax": [10, 10, 10],
            "alpha": [1/2, 1/4, 1/16], 
            "beta": [15, 25, 55]
            }, index=["soft", "medium", "hard"])

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
        cleaned_tires = [s.strip().lower() for s in tire_types]

        if len(stint_lengths) != 3 or len(tire_types) != 3:
            raise ValueError("Need exactly 3 stints and 3 tire types")
        if any(s < 1 for s in stint_lengths):
            raise ValueError("Every stint must be at least 1 lap")
        if sum(stint_lengths) != RACE_LAPS:
            raise ValueError(f"Stints must total {RACE_LAPS} laps")
        if any(t not in self.tires.index for t in cleaned_tires):
            raise ValueError("Unknown tire type")
        if len(set(tire_types)) < 2:
            raise ValueError("Must use at least 2 different tire types")
        
        laps = []
        for i, (length, tire) in enumerate(zip(stint_lengths, cleaned_tires)):
            # print(length, tire, i)
            tire_stats = self.tires.loc[tire]
            age = np.arange(length)
            # print("🚀 ~ RaceSimulator ~ simulate ~ age:", age)
            tire_time = self.tire_time(age, tire_stats["Tmin"], tire_stats["Tmax"], tire_stats["alpha"], tire_stats["beta"])
            # print("🚀 ~ RaceSimulator ~ simulate ~ tire_time:", tire_time)
            pit = np.where((age == 0) & (i > 0), PIT_TIME, 0)
            # print("🚀 ~ RaceSimulator ~ simulate ~ pit:", pit)
            lap = pd.DataFrame({
                "age": age,
                "tire_time":tire_time,
                "pit":pit
                })
            laps.append(lap)
        # print(laps)
        race = pd.concat(laps, ignore_index=True)
        # print(race)
        return (race["tire_time"] + race["pit"]).sum()


def plot_tires(simulator: RaceSimulator):
    """
    Plot tire degradation curves for all tire compounds.

    Parameters:
        simulator: A RaceSimulator object containing tire data.

    Returns:
        None.
    """
    ages = np.arange(RACE_LAPS)
    # print(simulator)
    for name, p in simulator.tires.iterrows():
        plt.plot(ages, simulator.tire_time(ages, p["Tmin"], p["Tmax"], p["alpha"], p["beta"]), label=name)
    plt.xlabel("tire age (laps)")
    plt.ylabel("s/lap added")
    plt.legend()
    plt.show()


def find_best_strategy(simulator: RaceSimulator):
    """
    Test all valid race strategies and find the one
    with the minimum total time added.

    Parameters:
        simulator: A RaceSimulator object.

    Returns:
        The strategy with the lowest total tire and pit time.
    """
    best = None
    tire_names = list(simulator.tires.index)
    tire_orders = []
    for a in tire_names:
        for b in tire_names:
            for c in tire_names:
                if not (a == b == c):
                    tire_orders.append((a,b,c))
    
    pit_stop_combos = combinations(range(2, RACE_LAPS + 1), 2)
    for p1, p2 in pit_stop_combos:
        stints = (p1 - 1, p2 - p1, RACE_LAPS + 1 - p2)
        for tires in tire_orders:
            time = simulator.simulate(stints, tires)
            if best is None or time < best[0]:
                best = (float(time), stints, tires)

    return best