import csv
import streamlit as st

filename = "Cleaning/MateElo.csv"

@st.cache_data
def getHeatmapData(pieceFilter, ratingFilter1, ratingFilter2, winnerFilter):
    with open(filename, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        
        data = [[0 for _ in range(8)] for _ in range(8)]
        rows = "87654321"
        columns = "abcdefgh"
        notationToIndex = {}

        # a1 is 00 b1 is 01 c1 is 02
        # a2 is 10 b2 is 11 c2 is 12
        for i in range(8):
            for j in range(8):
                notationToIndex[columns[j]+rows[i]] = (i, j)

        for row in csvreader:
            piece = row[2]
            square = row[3]
            rating1, rating2 = row[7], row[8]
            winner = row[4]
            if (pieceFilter != "No Filter" and piece != pieceFilter) or (int(rating1) < int(ratingFilter1) or int(rating2) > int(ratingFilter2)) or (winnerFilter != "No Filter" and winner != winnerFilter):
                continue
            i, j = notationToIndex[square]
            data[i][j] += 1
    
    return data


