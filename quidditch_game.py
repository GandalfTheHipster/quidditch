# simulate_quidditch_game.py

import random

def simulate_quidditch_game(team1, team2):
    team1_quaffle_points = random.randint(0, 20) * 10
    team2_quaffle_points = random.randint(0, 20) * 10

    # Assuming initial points are reset at the start of each game in main.py
    team1.points = team1_quaffle_points
    team2.points = team2_quaffle_points

    snitch_catch = random.randint(0, 1)
    if snitch_catch == 0:
        team1.points += 150
        team1.snitch_catch = True
        snitch_catcher = team1.name
    else:
        team2.points += 150
        team2.snitch_catch = True
        snitch_catcher = team2.name

    # Determine game outcome for league standings
    if team1.points > team2.points:
        team1.wins += 1
        team2.losses += 1
    elif team2.points > team1.points:
        team2.wins += 1
        team1.losses += 1
    else:
        team1.draws += 1
        team2.draws += 1

    # Return game details for CSV
    return {
        'team1_name': team1.name,
        'team2_name': team2.name,
        'team1_points': team1.points,
        'team2_points': team2.points,
        'snitch_catch': snitch_catcher
    }
