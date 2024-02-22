# main.py
import csv
from loading_players import load_players, list_teams
from quidditch_game import simulate_quidditch_game
from schedule import generate_schedule
from team import Team
from print_text import print_standings  # Assuming this is a function that prints standings

# Setup team structures
team_names = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"]
teams = [Team(name) for name in team_names]

load_players("players.csv")
list_teams()

# Generate the game schedule
schedule = generate_schedule(teams)

# Initialize storage for game results
game_details = []

# Simulate the season
for game in schedule:
    team1, team2 = game
    # Reset the snitch_catch attribute before each game
    team1.snitch_catch = team2.snitch_catch = False
    # Simulate the game and store the result
    result = simulate_quidditch_game(team1, team2)
    game_details.append(result)

# Write the game results to a CSV file
with open('quidditch_results.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Team 1', 'Team 2', 'Team 1 Points', 'Team 2 Points', 'Snitch Catch'])
    for detail in game_details:
        writer.writerow([detail['team1_name'], detail['team2_name'], detail['team1_points'], detail['team2_points'], detail['snitch_catch']])

# Display the final standings
print_standings(teams)
