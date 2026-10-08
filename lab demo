from classes import Driver, Team
import csv

#creates 10 teams from dataset

with open("data/f1_point.csv", "r") as file:
	reader = csv.reader(file)

	#skip header
	next(reader)

	for row in reader:
		driver_name = row[0]
		team_name = row[1]
		points = int(row[2])

		if team_name not on team:
			team[team_name] = Team(team_name)

		driver = Driver(driver_name, points)
		teams[team_name].add_driver(driver)
	
	print("Number of Teams:", len(teams))


#verify object

red_bull = teams["RED BULL RACING HONDA RBPT"]

print("Team:", red_bull.name)
print("Drivers:", red_bull.drivers)

#test case 2 - special case (three drivers)

special_team = Team("Test Racing")

special_team.add_driver(Driver("Driver A", 100))
special_team.add_driver(Driver("Driver B", 50))
special_team.add_driver(Driver("Driver C", 25))

print(special_team)
print("Number of drivers:", len(special_team.drivers))
print("Total points:", special_team.get_total_points())

#test sorting

team1 = Team("Team A")
team1.add_driver(Driver("Driver A", 100))


team2 = Team("Team B")
team2.add_driver(Driver("Driver B", 250))


team3 = Team("Team C")
team3.add_driver(Driver("Driver C", 50))

test_teams = [team1, team2, team3]

sorted_test_teams = sorted(test_teams)

for team in sorted_test_teams:
	print(team)

#test 3 error case

invalid_data = [
	["Driver A", "Test Team", "100"]
	["Driver B", "Test Team", "abc"]
]

with open("invalid_f1.csv", "w", newline="") as file:
	writer = csv.writer(file)
	writer.writerow(["Driver", "Team", "Points"])
	writer.writerows(invalid_data)

print("Invalid test file created.")

#test error

try:
	test_teams = {}

	with open("invalid_f1.csv", "r") as file:
	read = csv.reader(file)
	next(reader)
	
	for row in reader:
		driver_name = row[0]
		team_name = row[1]
		points = int(row[2])

		if team_name not on team:
			team[team_name] = Team(team_name)

		driver = Driver(driver_name, points)
		teams[team_name].add_driver(driver)
	
	print("Number of Teams:", len(teams))

except ValueError as e:
	print("Error dectected:", e)

