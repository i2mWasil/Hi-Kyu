import pandas as pd
import numpy as np
import os 
import csv

file_path = os.path.join(os.getcwd(), "data")


def load_data(filename, file_path=file_path):
    csv_path = os.path.join(file_path, filename)
    return pd.read_csv(csv_path)


ball = pd.read_csv("finalBowler.csv")

def prediction(ball, name):
    score = 0
    for i in range(1, 6, 1):
        
        score += i * ball.at[i-1, name]
    score /= 15
    return score

def predictedBall():

    predictedBowler = []
    predictedBowler.append(prediction(ball, "Bumrah"))
    predictedBowler.append(prediction(ball, "Shami"))
    predictedBowler.append(prediction(ball, "Kuldeep"))
    predictedBowler.append(prediction(ball, "Starc"))
    predictedBowler.append(prediction(ball, "Santner"))
    predictedBowler.append(prediction(ball, "Mohit"))
    predictedBowler.append(prediction(ball, "Cummins"))
    predictedBowler.append(prediction(ball, "Rabada"))
    predictedBowler.append(prediction(ball, "Nortje"))
    predictedBowler.append(prediction(ball, "Vivek"))
    predictedBowler.append(prediction(ball, "Chahal"))
    predictedBowler.append(prediction(ball, "Archer"))
    predictedBowler.append(prediction(ball, "Ashwin"))
    predictedBowler.append(prediction(ball, "Siraj"))
    predictedBowler.append(prediction(ball, "Arshdeep"))
    predictedBowler.append(prediction(ball, "Saini"))

    player_namePred = ['Bumrah','Shami','Kuldeep','Starc','Santner','Mohit','Cummins','Rabada','Nortje','Vivek','Chahal','Archer','Ashwin','Siraj','Arshdeep','Saini']
    dicPredBow = {'Player': player_namePred, 'Match 6': predictedBowler}

    df_predBow = pd.DataFrame(dicPredBow)
    return df_predBow

predictedBall()
