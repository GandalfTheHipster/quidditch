class Player:
    def __init__(self, team, name, position, skill_level):
        self.team = team
        self.name = name
        self.position = position  # E.g., 'Seeker', 'Keeper', 'Chaser', 'Beater'
        self.skill_level = skill_level  # Arbitrary scale, e.g., 1-10

    def __str__(self):
        return f"{self.name}, Position: {self.position}, Skill Level: {self.skill_level}"
        # return f"{self.name}, Position: {self.position}, Skill Level: {self.skill_level}, Team: {self.team}"
