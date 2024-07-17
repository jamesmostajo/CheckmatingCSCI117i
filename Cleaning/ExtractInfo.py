filenames = []
# fileouts = []
base = "ChessData/lichess_elite_2023-"
for i in range(1, 12+1):
    if i < 10: 
        filenames.append(base+"0"+str(i)+".pgn")
        # fileouts.append("Info/0"+str(i)+"GameInfo.csv")
    else:
        filenames.append(base+str(i)+".pgn")
        # fileouts.append("Info/"+str(i)+"GamesInfo.csv")

def get(searchSpace, toFind):
    startInd = searchSpace.find(toFind) + len(toFind) + 1
    returnString = ""
    index = startInd
    while searchSpace[index] != "\"":
        returnString += searchSpace[index]
        index += 1
    return returnString

    
fileout = "EloInfo.csv"
s = open(fileout,"w")
game_id = 0
for i in range(12):
    filepath = filenames[i]
    # fileout = fileouts[i]
    f = open(filepath, "r")
    data = f.read()

    data = str(data)
    raw_data = data.split("[Event ")

    del raw_data[0]

    games = []
    for game_index in range(len(raw_data)):
        game = raw_data[game_index]
        whiteElo = get(game, "WhiteElo ")
        blackElo = get(game, "BlackElo ")
        info = [game_id, min(whiteElo, blackElo), max(whiteElo, blackElo)]
        print(*info, sep=',', file=s)
        game_id+=1

    f.close()
s.close()