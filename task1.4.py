import random
from tabulate import tabulate

class ChessPlayer:
    def __init__(self, name, age, ELO, tenacity, isBoring):
        self.name = name
        self.age = age
        self.ELO = ELO
        self.tenacity = tenacity
        self.isBoring = isBoring
        self.score = 0

    def simulateMatch(self, obj):
        if abs(self.ELO-obj.ELO) > 100:
            if self.ELO > obj.ELO:
                self.score += 1
            else:
                obj.score += 1
        elif abs(self.ELO-obj.ELO) < 100 and abs(self.ELO-obj.ELO) > 50:
            if self.ELO > obj.ELO:
                ten = random.randint(1, 10) * obj.tenacity
                if ten > self.ELO:
                    obj.score += 1
                else:
                    self.score += 1
            else:
                ten = random.randint(1, 10) * self.tenacity
                if ten > obj.ELO:
                    self.score += 1
                else:
                    obj.score += 1
        elif abs(self.ELO-obj.ELO) < 50:
            if abs(self.tenacity-obj.tenacity) > 100:
                if self.tenacity > obj.tenacity:
                    self.score += 1
                else:
                    obj.score += 1
        elif (self.isBoring is True or obj.isBoring is True) and abs(self.ELO-obj.ELO) < 100:
            self.score += 0.5
            obj.score += 0.5


c = ChessPlayer('Courage the Cowardly Dog', 25, 1000.39, 1000, False)
p = ChessPlayer('Princess Peach', 23, 945.65, 50, True)
w = ChessPlayer('Walter White', 50, 1650.73, 750, False)
r = ChessPlayer('Rory Gilmore', 16, 1700.87, 500, False)
a = ChessPlayer('Anthony Fantano', 37, 1400.45, 400, True)
b = ChessPlayer('Beth Harmon', 20, 2500.34, 150, False)

players = [c, p, w, r, a, b]
#for first match between each player
for i in range(0,len(players)):
    for j in range(i+1,len(players)):
        players[i].simulateMatch(players[j])
#for second match between each player
for i in range(0,len(players)):
    for j in range(i+1,len(players)):
        players[i].simulateMatch(players[j])
Result=[]
for item in players:
    temp=[item.name,item.score]
    Result.append(temp)
head = ["Name","Score"]
print(tabulate(Result, headers=head, tablefmt="grid"))












