import csv

elofile = "EloInfo.csv"
matefile = "MatePieces.csv"
outfile = "MateElo.csv"
elo = []
mate = {}

with open(elofile, 'r') as elof:
    eloreader = csv.reader(elof)

    for row in eloreader:
        elo.append(row)

with open(matefile, 'r') as matef:
    matereader = csv.reader(matef)

    for row in matereader:
        mate[row[0]] = row

out = []
for row in elo:
    if row[0] not in mate:
        continue
    out.append(mate[row[0]] + [row[1]] + [row[2]])

for row in out:
    print(*row, sep=',')

# python3 ExtractCheckmatesElo.py > MateElo.csv