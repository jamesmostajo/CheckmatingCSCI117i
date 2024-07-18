import json

jsonfilename = "Cleaning/EloGameResults.json"

def getPieGameresults(ratingFilter1, ratingFilter2):

    with open(jsonfilename, 'r') as jsonfile:
        cumu_elo_res = json.load(jsonfile)

    ratingFilter1 -= 1

    r1, r2 = str(ratingFilter1), str(ratingFilter2)

    results = ["Checkmate", "Draw", "Others"]
    res_in_range = []

    for res in results:
        res_in_range.append(cumu_elo_res[r2][res] - cumu_elo_res[r1][res])
    
    return res_in_range