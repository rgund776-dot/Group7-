from classes1 import Team, Driver
import csv

def parse_file(file_path: str) -> list:
    teams = []
    with open(file_path, 'r') as file:
        data = csv.reader(file)
        next(data)  # Skip the header line
        for driver in data:
            name = driver[0]
            team_name = driver[1]
            driver_obj = Driver(name, int(driver[2]))
            
            for existing_team in teams:
                if existing_team.name == team_name:
                    existing_team.add_driver(driver_obj)
                    break
            else:
                team = Team(team_name)
                team.add_driver(driver_obj)
                teams.append(team)
    return teams

def main():
    teams = parse_file("f1_points.csv")
    sorted_teams = sorted(teams, reverse=True)
    return sorted_teams
    # for team in sorted_teams:
    #     print(team)
main()