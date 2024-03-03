import pandas as pd
import numpy as np
import os 
import csv

file_path = os.path.join(os.getcwd(), "data")


def load_data(filename, file_path=file_path):
    csv_path = os.path.join(file_path, filename)
    return pd.read_csv(csv_path)


bat = pd.read_csv("Project\\data\\finalBatsman.csv")

def prediction(bat, name):
    score = 0
    for i in range(1, 6, 1):
        
        score += i * bat.at[i-1, name]
    score /= 15
    return score

def predictedBat():
    
    predictedBatsman = []
    predictedBatsman.append(prediction(bat, "David Warner"))
    predictedBatsman.append(prediction(bat, "Shubhman Gill"))
    predictedBatsman.append(prediction(bat, "Mitch Marsh"))
    predictedBatsman.append(prediction(bat, "Virat Kohli"))
    predictedBatsman.append(prediction(bat, "Joe Root"))
    predictedBatsman.append(prediction(bat, "MS Dhoni"))
    predictedBatsman.append(prediction(bat, "Rohit Sharma"))
    predictedBatsman.append(prediction(bat, "Steve Smith"))
    predictedBatsman.append(prediction(bat, "Pritesh"))
    predictedBatsman.append(prediction(bat, "Abhinav"))
    predictedBatsman.append(prediction(bat, "Ayan"))
    predictedBatsman.append(prediction(bat, "Wasil"))
    predictedBatsman.append(prediction(bat, "Chris Gayle"))
    predictedBatsman.append(prediction(bat, "Kane Williamson"))
    predictedBatsman.append(prediction(bat, "Ben Stokes"))
    predictedBatsman.append(prediction(bat, "Ishan Kishan"))

    player_namePred = ['David Warner','Shubhman Gill','Mitch Marsh','Virat Kohli','Joe Root','MS Dhoni','Rohit Sharma','Steve Smith','Pritesh','Abhinav','Ayan','Wasil','Chris Gayle','Kane Williamson','Ben Stokes','Ishan Kishan']
    dicPred = {'Player': player_namePred, 'Match 6': predictedBatsman}

    df_pred = pd.DataFrame(dicPred, index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
    return df_pred

