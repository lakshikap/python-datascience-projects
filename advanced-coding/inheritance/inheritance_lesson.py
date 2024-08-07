import datetime


class Player:
    def __init__(self, fname, lname, byear):
        self.first_name = fname
        self.last_name = lname
        self.birth_year = byear

    def get_age(self):
        now = datetime.datetime.now()
        return now.year - self.birth_year


class CricketPlayer(Player):
    def __init__(self, fname, lname, byear, team):
        Player.__init__(self, fname, lname, byear)
        self.team = team
        self.scores = []

    def add_score(self, score):
        self.scores.append(score)

    def get_avg_score(self):
        return sum(self.scores)/len(self.scores)


class TennisPlayer(Player):
    def __init__(self, fname, lname, byear, gwinner):
        Player.__init__(self, fname, lname, byear)
        self.grand_slam = gwinner
        self.aces = []

    def get_avg_aces_per_match(self):
        return sum(self.aces)/len(self.aces)


virat = CricketPlayer('virat', 'kohli', 1988, 'india')
virat.add_score(80)
virat.add_score(100)
virat.add_score(0)
print("Age of virat kohli: ", virat.get_age())
print("Average score of virat kohli: ", virat.get_avg_score())

roger = TennisPlayer('roger', 'federer', 1981, 20)
print("Age of Roger Federer: ", roger.get_age())