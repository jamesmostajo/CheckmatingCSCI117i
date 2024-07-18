import csv, json

# sample data output
# db = {
#     2300 : {
#         "P" : 0,
#         "R" : 0,
#         "N" : 0,
#         "B" : 0,
#         "Q" : 0,
#         "K" : 0,
#     },
#     2301 : {
#         "P" : 0,
#         "R" : 0,
#         "N" : 0,
#         "B" : 0,
#         "Q" : 0,
#         "K" : 0,
#     },
# }

elo_takes = {elo : {piece:0 for piece in "PRNBQK"} for elo in range(2299, 4001)}

elofile = "EloInfo.csv"
game_elo = [] # gameid - elo

with open(elofile, 'r') as elof:
    filereader = csv.reader(elof)

    for row in filereader:
        r1, r2 = int(row[1]), int(row[2])
        elo = (r1+r2)//2
        game_elo.append(elo)


filenames = []
for i in range(1, 12+1):
    if i < 10: 
        filenames.append("Games/0"+str(i)+"GamesChessMoves.csv")
    else:
        filenames.append("Games/"+str(i)+"GamesChessMoves.csv")

for i in range(12):
    with open(filenames[i], 'r') as file:
        filereader = csv.reader(file)

        for row in filereader:
            cur_elo = game_elo[int(row[0])]
            moves = row[1:-1]

            for move in moves:
                if 'x' in move:
                    capturing_piece = move[move.index('x') - 1]
                    if capturing_piece not in "RNBQK":
                        capturing_piece = "P"
                    
                    elo_takes[cur_elo][capturing_piece] += 1

    print(f"Done with File {i}.")

cumu_elo_takes = {elo : {piece:0 for piece in "PRNBQK"} for elo in range(2299, 4001)}

for elo in range(2300, 4001):
    for piece in "PRNBQK":
        cumu_elo_takes[elo][piece] = cumu_elo_takes[elo-1][piece] + elo_takes[elo][piece]


json_file = "EloPieceTakes.json"
with open(json_file, 'w') as json_file:
    json.dump(cumu_elo_takes, json_file)

            

