import pandas as pd
import numpy as np
import os 
import csv

file_path = os.path.join(os.getcwd(), "data")


def load_data(filename, file_path=file_path):
    csv_path = os.path.join(file_path, filename)
    return pd.read_csv(csv_path)


allround = pd.read_csv("finalAllRounder.csv")

def prediction(allround, name):
    score = 0
    for i in range(1, 6, 1):
        
        score += i * allround.at[i-1, name]
    score /= 15
    return score



def predictedAllRound():
    predictedAllRounder = []
    predictedAllRounder.append(prediction(allround, "Shakib"))
    predictedAllRounder.append(prediction(allround, "Rashid"))
    predictedAllRounder.append(prediction(allround, "Maxwell"))
    predictedAllRounder.append(prediction(allround, "Jadeja"))
    predictedAllRounder.append(prediction(allround, "Jansen"))
    predictedAllRounder.append(prediction(allround, "Rachin"))
    predictedAllRounder.append(prediction(allround, "Hasranga"))
    predictedAllRounder.append(prediction(allround, "Pandya"))
    predictedAllRounder.append(prediction(allround, "Holder"))
    predictedAllRounder.append(prediction(allround, "Zampa"))
    predictedAllRounder.append(prediction(allround, "Head"))
    predictedAllRounder.append(prediction(allround, "Green"))

    player_namePred = ['Shakib','Rashid','Maxwell','Jadeja','Jansen','Rachin','Hasranga','Pandya','Holder','Zampa','Head','Green']
    dicPredAll = {'Player': player_namePred, 'Match 6': predictedAllRounder}
    
    df_predAll = pd.DataFrame(dicPredAll)
    return df_predAll


z = predictedAllRound()
print(z)