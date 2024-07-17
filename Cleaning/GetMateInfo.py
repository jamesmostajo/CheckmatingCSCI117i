filenames = []
for i in range(1, 12+1):
    if i < 10: 
        filenames.append("Checkmates/0"+str(i)+"Checkmates.csv")
    else:
        filenames.append("Checkmates/"+str(i)+"Checkmates.csv")

fileout = "./../MatePieces.csv"
won = ["White", "Black"]

def get_matingpiece(pieceCode):
    pieceName = {
        "Q" : "Queen",
        "R" : "Rook",
        "B" : "Bishop",
        "N" : "Knight",
        "K" : "King",
        "O" : "King"
    }
    if pieceCode.islower():
        return "Pawn"
    return pieceName[pieceCode]

def get_square(moveNotation, color):
    if "O" in moveNotation:
        side = "1" if color == "White" else "8"
        if len(moveNotation) == 6:
            return "c"+side
        elif len(moveNotation) == 4:
            return "g"+side
    if "=" in moveNotation:
        return moveNotation[-5:-3]
    
    return mate_move[-3:-1]

    

s = open(fileout,"w")
for i in range(12):
    filepath = filenames[i]
    f = open(filepath, "r")

    data = "1"
    while (data):
        data = f.readline()
        data = [token for token in str(data).split(",")]
        game_id = data[0]
        moves = data[1:]

        if len(moves) == 0:
            break
        mate_move = moves[-2]
        
        color = won[len(moves)%2]
        capture = True if "x" in mate_move else False
        promoted = True if "=" in mate_move else False

        capture_message = "Capture" if capture else "Not Capture"
        promote_message = "Promotion" if promoted else "Not Promotion"
        mating_piece = get_matingpiece(mate_move[0])

        square = get_square(mate_move, color)

        print(*[game_id, mate_move, mating_piece, square, color, capture_message, promote_message], sep=",", file=s)

    f.close()
s.close()