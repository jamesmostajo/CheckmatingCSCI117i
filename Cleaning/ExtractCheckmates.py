filenames = []
fileouts = []
base = "ChessData/lichess_elite_2023-"
for i in range(1, 12+1):
    if i < 10: 
        filenames.append("Games/0"+str(i)+"GamesChessMoves.csv")
        fileouts.append("Checkmates/0"+str(i)+"Checkmates.csv")
    else:
        filenames.append("Games/"+str(i)+"GamesChessMoves.csv")
        fileouts.append("Checkmates/"+str(i)+"Checkmates.csv")

for i in range(12):
    filepath = filenames[i]
    fileout = fileouts[i]
    f = open(filepath, "r")
    s = open(fileout,"w")

    data = "empty_data"
    while (data):
        data = f.readline()
        data = [token for token in str(data).split(",")]
        game_id = data[0]
        moves = data[1:]
        if len(moves) == 1: break
        if moves[-2][-1] == "#":
            print(*[game_id, *moves], sep=",", file=s, end='')

    f.close()
    s.close()