import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from itertools import combinations, combinations_with_replacement


class RaceSimulator:
    """
    Simulates an F1 race strategy by calculating the time added
    from tire degradation and pit stops.
    """
    def __init__(self):
        """
        Initialize the simulator and store tire data.
        """
        self.tire_data = pd.DataFrame({
        'Tmin': [0, 1, 2],
        'Tmax': [10, 10, 10],
        'alpha': [0.5, 0.25, 0.0625],
        'beta': [15, 25, 55]
       }, index=['Soft', 'Medium', 'Hard'])


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
        time = Tmin + (Tmax - Tmin) / (1 + np.exp(-alpha * (age - beta)))
        return time 


    def simulate(self, stint_lengths, tire_types):
        """
        Simulate a complete race strategy.

        Parameters:
            stint_lengths: Length of each race stint.
            tire_types: Tire compound used for each stint.

        Returns:
            Total time added from tire degradation and pit stops.
        """
        if len(stint_lengths) != 3 or len(tire_types) != 3:
            raise ValueError("A race must have 3 stints")
        
        if sum(stint_lengths) != 60:
            raise ValueError("Total number of laps must be 60") 
        
        if any(length <= 0 for length in stint_lengths):
            raise ValueError("Stint legnths must be postiive")
        
        if len(set(tire_types)) < 2:
            raise ValueError("At least 2 different tire types must be used")
        
        for tire in tire_types:
            if tire not in self.tire_data.index:
                raise ValueError("Invalid Tire Type")
            
        stint_frames = [] 
    
        lap_number = 1 
    
        for i in range(3): 
        
            length = stint_lengths[i]
            tire = tire_types[i]
        
            Tmin = self.tire_data.loc[tire, 'Tmin']
            Tmax = self.tire_data.loc[tire, 'Tmax']
            alpha = self.tire_data.loc[tire, 'alpha']
            beta = self.tire_data.loc[tire, 'beta'] 
        
            tire_age = np.arange(length) 
        
            tire_time_added = self.tire_time(tire_age, Tmin, Tmax, alpha, beta) 
        
            #pit stop 
        
            pit_stop_time = np.zeros(length) 
        
            if i > 0:
                pit_stop_time[0] = 25 
            
            stint_df = pd.DataFrame({
                'Lap': np.arange(lap_number, lap_number + length),
                'Tire': tire,
                'Tire Age': tire_age,
                'Tire Time Added': tire_time_added,
                'Pit Stop Time': pit_stop_time
            }) 

            stint_frames.append(stint_df)
        
            lap_number += length 
        
        self.race_data = pd.concat(stint_frames, ignore_index=True)
    
        total_time = (
            self.race_data['Tire Time Added'].sum()
            + self.race_data['Pit Stop Time'].sum()
        )
    
        return total_time

def plot_tires(simulator):
    """
    Plot tire degradation curves for all tire compounds.

    Parameters:
        simulator: A RaceSimulator object containing tire data.

    Returns:
        None.
    """
    ages = np.arange(0,61)
    
    for tire in simulator.tire_data.index: 
        
        Tmin = simulator.tire_data.loc[tire, 'Tmin']
        Tmax = simulator.tire_data.loc[tire, 'Tmax']
        alpha = simulator.tire_data.loc[tire, 'alpha']
        beta = simulator.tire_data.loc[tire, 'beta']
        
        times = simulator.tire_time(ages, Tmin, Tmax, alpha, beta)
        
        plt.plot(ages,times, label=tire)
        
    plt.xlabel("Tire Age (laps)")
    plt.ylabel("Additional Lap Time (seconds)")
    plt.title("Tire Breakdown")
    plt.legend()
    plt.grid()
    plt.show()


def find_best_strategy(simulator):
    """
    Test all valid race strategies and find the one
    with the minimum total time added.

    Parameters:
        simulator: A RaceSimulator object.

    Returns:
        The strategy with the lowest total tire and pit time.
    """
    best_time = float('inf')
    best_stint_lengths = None
    best_tire_types = None 
    
    tires = simulator.tire_data.index 
    
    for stop1, stop2 in combinations(range(2,61),2):
        
        stint_lengths = [
            stop1 - 1,
            stop2 - stop1,
            61 - stop2
        ]
        
        for tire1 in tires:
            for tire2 in tires:
                for tire3 in tires:
                    
                    tire_types = [tire1,tire2,tire3]
                    
                    if len(set(tire_types)) >= 2:
                        
                        total_time = simulator.simulate(
                            stint_lengths, tire_types
                        )
                        
                        if total_time < best_time:
                            best_time = total_time
                            best_stint_lengths = stint_lengths
                            best_tire_types = tire_types 
                            
    return best_time, best_stint_lengths, best_tire_types
        
  