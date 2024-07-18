import csv, json

filenames = []
for i in range(1, 12+1):
    if i < 10: 
        filenames.append("Games/0"+str(i)+"GamesChessMoves.csv")
    else:
        filenames.append("Games/"+str(i)+"GamesChessMoves.csv")

elofile = "EloInfo.csv"
game_elo = [] # gameid - elo

with open(elofile, 'r') as elof:
    filereader = csv.reader(elof)

    for row in filereader:
        r1, r2 = int(row[1]), int(row[2])
        elo = (r1+r2)//2
        game_elo.append(elo)

elo_res = {elo : {res:0 for res in ["Draw", "Checkmate", "Others"]} for elo in range(2299, 4001)}

for i in range(12):
    with open(filenames[i], 'r') as file:
        filereader = csv.reader(file)

        for row in filereader:
            game_id = int(row[0])
            score = row[-1].split('-')
            last_move = row[-2]
            cur_elo = game_elo[game_id]

            if "1/2" in score:
                elo_res[cur_elo]["Draw"] += 1
            elif '#' in last_move:
                elo_res[cur_elo]["Checkmate"] += 1
            else:
                elo_res[cur_elo]["Others"] += 1
    
    print(f"Done with File {i}.")
    

cumu_elo_res = {elo : {res:0 for res in ["Draw", "Checkmate", "Others"]} for elo in range(2299, 4001)}

for elo in range(2300, 4001):
    for res in ["Draw", "Checkmate", "Others"]:
        cumu_elo_res[elo][res] = cumu_elo_res[elo-1][res] + elo_res[elo][res]

json_file = "EloGameResults.json"
with open(json_file, 'w') as json_file:
    json.dump(cumu_elo_res, json_file)