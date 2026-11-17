from part_2 import RaceSimulator, plot_tires, find_best_strategy

# soft_tire = race.Tire("soft", 0, 10, 0.5, 15)
# medium_tire = race.Tire("medium", 1, 20, 0.25, 25)
# hard_tire = race.Tire("hard", 2, 10, 0.0625, 55)

# pit_stop_time = 25

# pit_stop_time_1 = 11
# pit_stop_time_2 = 29

# total_laps = 60

sim = RaceSimulator()

# Simulate one strategy: stint lengths (laps) and the tire for each stint
total = sim.simulate([14, 8, 38], ["Soft", "Medium", "Hard"])