import csv
import streamlit as st
filename = "Cleaning/MateElo.csv"


def getPieData(ratingFilter1, ratingFilter2):
    with open(filename, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        piecesNames = ["Pawn", "Knight", "Bishop", "Rook", "Queen", "King"]
        pieceCheckmateFrequency = [0 for _ in range(6)]

        pieceToIndex = {
            "Pawn" : 0,
            "Knight" : 1,
            "Bishop" : 2,
            "Rook" : 3,
            "Queen" : 4,
            "King" : 5,
        }
        total_checkmates = 0
        for row in csvreader:
            piece = row[2]
            rating1, rating2 = row[7], row[8]
            if (int(rating1) < int(ratingFilter1) or int(rating2) > int(ratingFilter2)):
                continue
            pieceCheckmateFrequency[pieceToIndex[piece]] += 1
            total_checkmates += 1
        if  total_checkmates == 0:
            return -1
        data = {
            'piece' : piecesNames,
            'pieceCount' : pieceCheckmateFrequency
        }
    return data




