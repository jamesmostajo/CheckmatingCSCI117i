import csv
import streamlit as st

filename = "Cleaning/EloInfo.csv"

@st.cache_data
def getGamesNum(ratingFilter1, ratingFilter2):
    count = 0
    
    with open(filename, "r") as csvfile:
        csvreader = csv.reader(csvfile)
    
        for row in csvreader:
            rating1, rating2 = row[1], row[2]
            if int(rating1) < int(ratingFilter1) or int(rating2) > int(ratingFilter2):
                continue
            count += 1
    
    return count


