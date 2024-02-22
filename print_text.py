def print_standings(teams):
    teams_sorted = sorted(teams, key=lambda x: (x.points, x.wins), reverse=True)
    print("Final Standings:")
    for team in teams_sorted:
        print(f"{team.name}: Wins: {team.wins}, Losses: {team.losses}, Draws: {team.draws}, Total Points: {team.points}")