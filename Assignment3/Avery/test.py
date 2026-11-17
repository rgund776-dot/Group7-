import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations, combinations_with_replacement

RACE_LAPS = 60
PIT_TIME = 25  # seconds added on a pit stop lap


class RaceSimulator:
    """
    Simulates an F1 race strategy by calculating the time added
    from tire degradation and pit stops.
    """

    def __init__(self):
        """Initialize the simulator and store tire data in a DataFrame."""
        self.tires = pd.DataFrame(
            {
                "Tmin": [0, 1, 2],
                "Tmax": [10, 10, 10],
                "alpha": [1 / 2, 1 / 4, 1 / 16],
                "beta": [15, 25, 55],
            },
            index=["Soft", "Medium", "Hard"],
        )

    def tire_time(self, age, Tmin, Tmax, alpha, beta):
        """
        Calculate the time added due to tire degradation.

        Works on scalars, numpy arrays, or pandas Series (vectorized).
        """
        return Tmin + (Tmax - Tmin) / (1 + np.exp(-alpha * (age - beta)))

    def simulate(self, stint_lengths, tire_types):
        """
        Simulate a complete race strategy.

        Parameters:
            stint_lengths: Length (laps) of each stint, e.g. [14, 8, 38].
            tire_types: Tire name for each stint, e.g. ["Soft", "Medium", "Hard"].

        Returns:
            Total time added from tire degradation and pit stops.

        Raises:
            ValueError: if the strategy breaks the race rules.
        """
        self._validate(stint_lengths, tire_types)

        stints = []
        for i, (length, tire) in enumerate(zip(stint_lengths, tire_types)):
            params = self.tires.loc[tire]
            stint = pd.DataFrame({"age": np.arange(length)})  # new tires -> age 0
            stint["tire_time"] = self.tire_time(
                stint["age"], params["Tmin"], params["Tmax"],
                params["alpha"], params["beta"],
            )
            # Pit stop happens on the first lap of every stint except the first
            stint["pit_time"] = 0
            if i > 0:
                stint.loc[0, "pit_time"] = PIT_TIME
            stints.append(stint)

        race = pd.concat(stints, ignore_index=True)
        return (race["tire_time"] + race["pit_time"]).sum()

    def _validate(self, stint_lengths, tire_types):
        """Raise ValueError if the strategy is not allowed."""
        if len(stint_lengths) != 3 or len(tire_types) != 3:
            raise ValueError("A strategy needs exactly 3 stints and 3 tire types.")
        if any(l < 1 for l in stint_lengths):
            raise ValueError("Every stint must be at least 1 lap long.")
        if sum(stint_lengths) != RACE_LAPS:
            raise ValueError(f"Stint lengths must add up to {RACE_LAPS} laps.")
        if any(t not in self.tires.index for t in tire_types):
            raise ValueError(f"Tire types must be in {list(self.tires.index)}.")
        if len(set(tire_types)) < 2:
            raise ValueError("At least 2 different tire types must be used.")


def plot_tires(simulator):
    """Plot tire degradation curves for all tire compounds."""
    ages = np.arange(0, RACE_LAPS + 1)
    for name, p in simulator.tires.iterrows():
        plt.plot(ages, simulator.tire_time(ages, p["Tmin"], p["Tmax"],
                                           p["alpha"], p["beta"]), label=name)
    plt.xlabel("Tire age (laps)")
    plt.ylabel("Time added (s)")
    plt.title("Tire degradation")
    plt.legend()
    plt.show()


def find_best_strategy(simulator):
    """
    Test all valid race strategies and find the one
    with the minimum total time added.

    Returns:
        (best_time, pit_laps, tire_types) for the best strategy.
    """
    best = (np.inf, None, None)
    names = simulator.tires.index
    # pit laps: lap 1 can't be a pit lap (stint 1 needs >= 1 lap), so 2..60
    for p1, p2 in combinations(range(2, RACE_LAPS + 1), 2):
        lengths = [p1 - 1, p2 - p1, RACE_LAPS - p2 + 1]
        # every ordered choice of tires, using at least 2 different types
        for combo in combinations_with_replacement(names, 3):
            if len(set(combo)) < 2:
                continue
            for tires in set(_orderings(combo)):
                t = simulator.simulate(lengths, list(tires))
                if t < best[0]:
                    best = (t, (p1, p2), list(tires))
    return best


def _orderings(combo):
    """All orderings of a 3-item tuple (no itertools.permutations allowed)."""
    a, b, c = combo
    return [(a, b, c), (a, c, b), (b, a, c), (b, c, a), (c, a, b), (c, b, a)]