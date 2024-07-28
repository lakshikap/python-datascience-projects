import datetime


class CricketPlayer:
    def __init__(self, fname, lname, team, b_year):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = b_year
        self.team = team
        self.scores = []

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year

    def add_score(self, score):
        self.scores.append(score)

    def get_avg_score(self):
        return sum(self.scores)/len(self.scores)

    def __lt__(self, other):
        my_score = self.get_avg_score()
        other_score = other.get_avg_score()
        return my_score < other_score

    def __str__(self):
        return f'{self.first_name} {self.last_name}, cricket player from {self.team}'


virat = CricketPlayer('virat', 'kohli', 'india', 1988)
virat.add_score(80)
virat.add_score(100)
virat.add_score(0)

david = CricketPlayer('david', 'warner', 'australia', 1985)
david.add_score(39)
david.add_score(23)
david.add_score(85)


print(virat.team)
print(david.team)

print(virat.get_age())
print(david.get_age())

print(virat.get_avg_score())
print(david.get_avg_score())

print(virat < david)
print(virat)
print(david)
