import csv
import streamlit as st
filename = "Cleaning/SortedElo.csv"


def getHistogramData():
    with open(filename, "r") as csvfile:
        csvreader = csv.reader(csvfile)
        data = {}
        for interval in range(2350, 3200, 50):
            data[interval] = 0
        
        prevRating = 2350
        prevValue = 0
        for rating, prefix in csvreader:
            rating = int(rating)
            prefix = int(prefix)
            if rating in data:
                data[prevRating] = prefix-prevValue
                prevValue = prefix
                prevRating = rating
        db = {
            "elo_ranges" : list(data.keys()),
            "values" : list(data.values())
        }
    return db




