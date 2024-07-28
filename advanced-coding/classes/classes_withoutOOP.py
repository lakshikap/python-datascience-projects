import datetime

virat = {
    'first_name': 'virat',
    'last_name': 'kohli',
    'birth_year': 1988,
    'scores': []
}

virat['scores'].append(80)
virat['scores'].append(100)
virat['scores'].append(0)


def get_age(player):
    now = datetime.datetime.now()
    return now.year - player['birth_year']


print(get_age(virat))


def get_avg_score(player):
    return sum(player['scores']) / len(player['scores'])


print(get_avg_score(virat))

david = {
    'first_name': 'david',
    'last_name': 'warner',
    'birth_year': 1986,
    'scores': [],
}

david['scores'].append(35)
david['scores'].append(120)
david['scores'].append(12)

print(get_age(david))
print(get_avg_score(david))
