import csv
filename = "MatePieces.csv"

def getHeatmapData(pieceFilter):
    with open(filename, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        
        data = [[0 for _ in range(8)] for _ in range(8)]
        rows = "12345678"
        columns = "abcdefgh"
        notationToIndex = {}

        # a1 is 00 b1 is 01 c1 is 02
        # a2 is 10 b2 is 11 c2 is 12
        for i in range(8):
            for j in range(8):
                notationToIndex[columns[j]+rows[i]] = (i, j)

        for row in csvreader:
            piece = row[2]; square = row[3]
            if piece != pieceFilter and pieceFilter != "No Filter": continue
            i, j = notationToIndex[square]
            data[i][j] += 1
    
    return data


