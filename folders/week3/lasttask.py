class Sportsman:
    def __init__(self, sport_id, sport_name):
        self.sport_id = sport_id
        self.sport_name = sport_name

    def printInfo(self):
        print('Id:', self.sport_id)
        print('Name:', self.sport_name)

    def setType(self, sport_type):
        self.sport_type = sport_type

    def getType(self):
        return self.sport_type


class TeamSport(Sportsman):
    def __init__(self, sport_id, sport_name, num_players):
        super().__init__(sport_id, sport_name)
        self.num_players = num_players

    def printInfo(self):
        super().printInfo()
        print('Num_players:', self.num_players)


RusTiger = TeamSport('007', 'RusTiger', '10')
print(RusTiger.printInfo())
