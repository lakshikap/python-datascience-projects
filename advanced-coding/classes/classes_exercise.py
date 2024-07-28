class Avengers:
    def __init__(self, aname, aage, agen, apower, aweapon):
        self.name = aname
        self.age = aage
        self.gender = agen
        self.super_power = apower
        self.weapon = aweapon


captain = Avengers("Captain America", 100, "Male", "Strength, Speed, Reflexes", "The Shield")
iron_man = Avengers("Iron Man", 48, "Male", "Tech Savvy", "Powered Armour")
black_widow = Avengers("Black Widow", 34, "Female", "Resistance to ageing and disease", "Captain America Shield")
hulk = Avengers("Hulk", 49, "Male", "Unlimited Strength", "")
thor = Avengers("Thor", 1500, "Male", "God of Thunder, Electricity Generation", "Mjolnir")
hawkeye = Avengers("Hawk Eye", 41, "Male", "Clear Aim", "Bow and Arrows")


def get_info(self):
    return f' Avenger Profile - Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Super Power: {self.super_power}, Weapon: {self.weapon}'


def get_leader(self):
    return self.name == 'Captain America'


print(get_info(captain))
print(get_info(black_widow))
print(get_info(iron_man))
print(get_info(hulk))
print(get_info(thor))
print(get_info(hawkeye))

print(get_leader(thor))
