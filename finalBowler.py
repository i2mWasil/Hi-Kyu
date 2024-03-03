# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 20:37:34 2024

@author: prite
"""

import pandas as pd
import numpy as np 
import os 

import csv

# function for loading data
file_path = os.path.join(os.getcwd(), "data")


def load_data(filename, file_path=file_path):
    csv_path = os.path.join(file_path, filename)
    return pd.read_csv(csv_path)

#BOWLER

def wicketsBowler(score, wkt):
    if(wkt == 0):
        score += 0
    elif(wkt == 1):
        score += 10
    elif(wkt == 2):
        score += 20
    elif(wkt == 3):
        score += 30
    else:
        score += 40
    return score

def economyBowler(score, econ, over):
    if(econ <= 5 and over > 2):
        score += 20
    elif(econ <= 6):
        score += 17.5
    elif(econ > 6 and econ <= 7):
        score += 12.5
    elif(econ > 7 and econ <= 8):
        score += 5
    elif(econ > 8 and econ < 10):
        score += 0
    else:
        score += -5
    return score

def averageBowler(score, avg):
    if(avg < 10):
        score += 20
    elif(avg >= 10 and avg <= 20):
        score += 20 - 0.5*(avg - 10)
    elif(avg > 20 and avg <= 30):
        score += 15 - (avg - 20)
    elif(avg > 30):
        score += 2
    else:
        score += 0
    return score

def teamContributionBowler(score, contri):
    if(contri >= 0 and contri <=20):
        score += 0.25*(contri)
    elif(contri > 20 and contri <= 40):
        score += 5 + 0.25*(contri - 20)
    elif(contri > 40 and contri <= 60):
        score += 10 + 0.25*(contri - 40)
    else:
        score += 20
    return score


def totalPointsBowler(wkt, over, econ, avg, contri):
    score = 0
    score = wicketsBowler(score, wkt)
    score = economyBowler(score, econ, over)
    score = averageBowler(score, avg)
    score = teamContributionBowler(score, contri)
    return score


bowling=load_data("C:/Users/prite/Downloads/bowlers (2).csv")
print(bowling)

row_indices1= [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75]

# Initialize an empty list to store the scores
bowling_scores1 = []

# Iterate over the row indices
for index in row_indices1:
    # Calculate the score for the current row
    score = totalPointsBowler(bowling.at[index, 'Wickets'], bowling.at[index, 'Over'], float(bowling.at[index, 'Economy']), bowling.at[index, 'Average'], bowling.at[index, 'Contri'])
    # Append the score to the list
    bowling_scores1.append(score)

row_indices2= [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76]

bowling_scores2 = []

# Iterate over the row indices
for index in row_indices2:
    # Calculate the score for the current row
    score = totalPointsBowler(bowling.at[index, 'Wickets'], bowling.at[index, 'Over'], float(bowling.at[index, 'Economy']), bowling.at[index, 'Average'], bowling.at[index, 'Contri'])
    # Append the score to the list
    bowling_scores2.append(score)
    
row_indices3= [2,7,12,17,22,27,32,37,42,47,52,57,62,67,72,77]

bowling_scores3 = []

# Iterate over the row indices
for index in row_indices3:
    # Calculate the score for the current row
    score = totalPointsBowler(bowling.at[index, 'Wickets'], bowling.at[index, 'Over'], float(bowling.at[index, 'Economy']), bowling.at[index, 'Average'], bowling.at[index, 'Contri'])
    # Append the score to the list
    bowling_scores3.append(score)

row_indices4= [3,8,13,18,23,28,33,38,43,48,53,58,63,68,73,78]

bowling_scores4 = []

# Iterate over the row indices
for index in row_indices4:
    # Calculate the score for the current row
    score = totalPointsBowler(bowling.at[index, 'Wickets'], bowling.at[index, 'Over'], float(bowling.at[index, 'Economy']), bowling.at[index, 'Average'], bowling.at[index, 'Contri'])
    # Append the score to the list
    bowling_scores4.append(score)
    
row_indices5= [4,9,14,19,24,29,34,39,44,49,54,59,64,69,74,79]
bowling_scores5 = []

# Iterate over the row indices
for index in row_indices5:
    # Calculate the score for the current row
    score = totalPointsBowler(bowling.at[index, 'Wickets'], bowling.at[index, 'Over'], float(bowling.at[index, 'Economy']), bowling.at[index, 'Average'], bowling.at[index, 'Contri'])
    # Append the score to the list
    bowling_scores5.append(score)




    
player_name = ['Bumrah','Shami','Kuldeep','Starc','Santner','Mohit','Cummins','Rabada','Nortje','Vivek','Chahal','Archer','Ashwin','Siraj','Arshdeep','Saini']
dic={'Player':player_name,'Match1':bowling_scores1,'Match2':bowling_scores2,'Match3':bowling_scores3,'Match4':bowling_scores4,'Match5':bowling_scores5}
df=pd.DataFrame(dic)
d=df.T
d.to_csv("bowlers.csv")
