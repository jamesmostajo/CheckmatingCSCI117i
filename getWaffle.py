import csv
import streamlit as st
filename = "Cleaning/MateElo.csv"

@st.cache_data
def getWaffleData(ratingFilter1, ratingFilter2):
    with open(filename, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        data = [[ 5 for _ in range(100)] for _ in range(100)]
        pieceCheckmateFrequency = {
            "Pawn" : 0,
            "Knight" : 0,
            "Bishop" : 0,
            "Rook" : 0,
            "Queen" : 0,
            "King" : 0,
        }
        
        pieceToIndex = {
            "Pawn" : 0,
            "Knight" : 1,
            "Bishop" : 2,
            "Rook" : 3,
            "Queen" : 4,
            "King" : 5,
        }
        pieceDistribution = [0 for _ in range(6)]
        total_checkmates = 0

        for row in csvreader:
            piece = row[2]
            rating1, rating2 = row[7], row[8]
            if (int(rating1) < int(ratingFilter1) or int(rating2) > int(ratingFilter2)):
                continue
            pieceCheckmateFrequency[piece] += 1
            total_checkmates += 1
        
        if  total_checkmates == 0:
            return -1
            
        for piece in pieceCheckmateFrequency:
            pieceDistribution[pieceToIndex[piece]] = round(pieceCheckmateFrequency[piece]/total_checkmates * 10000)
        
        currPieceInd = 0
        for i in range(100):
            for j in range(100):
                it = 99-j if (i%1) else j
                if pieceDistribution[currPieceInd] == 0:
                    currPieceInd += 1
                    if sum(pieceDistribution) == 0: break
                pieceDistribution[currPieceInd] -= 1
                data[i][it] = currPieceInd
            if sum(pieceDistribution) == 0: break

    return data




