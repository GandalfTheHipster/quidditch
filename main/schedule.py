import random

def generate_schedule(teams):
    schedule = []
    for i in range(len(teams)):
        for j in range(i + 1, len(teams)):
            schedule.append((teams[i], teams[j]))
    random.shuffle(schedule)
    return schedule