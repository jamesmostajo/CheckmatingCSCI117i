import csv

elofile = "EloInfo.csv"
matefile = "MatePieces.csv"

elo = []

with open(elofile, 'r') as elof:
    eloreader = csv.reader(elof)

    for row in eloreader:
        elo.append(row)

for i in range(5):
    print(elo[i])