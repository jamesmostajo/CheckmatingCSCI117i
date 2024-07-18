import csv

elofile = "EloInfo.csv"

elo = []
elo_db = [0 for i in range(2300, 4001)] # 0 - 2300, 1 - 2301, ..., 1696 - 3996


with open(elofile, 'r') as elof:
    eloreader = csv.reader(elof)

    for row in eloreader:
        elo.append(row)

# mn, mx = 100000, 0
# mnave, mxave = 100000, 0

for row in elo:
    r1, r2 = int(row[1]), int(row[2])
    # mn = min([mn, r1, r2])
    # mx = max([mx, r1, r2])
    
    ave = (r1+r2)//2
    # mnave = min(mnave, ave)
    # mxave = max(mxave, ave)

    elo_db[ave-2300] += 1

# print(mn, mx)
# print(mnave, mxave)

cumu_elo_db = [0 for i in range(2300, 4001)]
cumu_elo_db[0] = elo_db[0]

for i in range(1, len(elo_db)):
    cumu_elo_db[i] = elo_db[i] + cumu_elo_db[i-1]

print(2299, 0, sep=',')
for r in range(len(cumu_elo_db)):
    print(r + 2300, cumu_elo_db[r], sep=',')

# python3 SortElo.py > SortedElo.csv