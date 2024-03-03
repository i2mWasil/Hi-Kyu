# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 20:12:04 2024

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


def runsAllRounder(score, run):
    if(run >= 0 and run <= 5):
        score += 0
    elif(run > 5 and run <= 15):
        score += run - 5
    elif(run > 15 and run <= 30):
        score += 10 + (2/3)*(run - 15)
    else:
        score += 20
    return score

def wicketsAllRounder(score, wkt):
    if(wkt == 0):
        score += 0
    elif(wkt == 1):
        score += 5
    elif(wkt == 2):
        score += 10
    elif(wkt == 3):
        score += 15
    else:
        score += 20
    return score


def strikeRateAllRounder(score, strike, ball):
    if(strike <= 100 and ball > 5):
        score = 0
    elif(strike > 100 and strike <= 125):
        score += 0.2*(strike - 100)
    elif(strike > 125 and strike <= 175):
        score += 5 + 0.1*(strike - 125)
    elif(strike > 175 and strike <= 250):
        score += 10 + (1/15)*(strike - 175)
    else:
        score += 20
    return score


def economyAllRounder(score, econ, over):
    if(econ <= 5 and over > 2):
        score += 20
    elif(econ > 5 and econ <= 7):
        score += 15
    elif(econ > 7 and econ <= 9):
        score += 10
    elif(econ > 9 and econ <= 10):
        score += 5
    else:
        score += -5
    return score


def teamContributionAllRounder(score, contri):
    if(contri >= 0 and contri <=20):
        score += 0.25*(contri)
    elif(contri > 20 and contri <= 40):
        score += 5 + 0.25*(contri - 20)
    elif(contri > 40 and contri <= 60):
        score += 10 + 0.25*(contri - 40)
    elif(contri > 60):
        score += 20
    else:
        score += 20
    return score


def totalPointsAllRounder(run, ball, strike, wkt, over, econ, contri):
    score = 0
    score = runsAllRounder(score, run)
    score = wicketsAllRounder(score, wkt)
    score = strikeRateAllRounder(score, strike, ball)
    score = economyAllRounder(score, econ, over)
    score = teamContributionAllRounder(score, contri)
    return score

all_rounder=load_data("Project\\data\\allRounders.csv")

row_indices1= [0,5,10,15,20,25,30,35,40,45,50,55]

# Initialize an empty list to store the scores
all_rounder_scores1 = []

# Iterate over the row indices
for index in row_indices1:
    # Calculate the score for the current row
    score = totalPointsAllRounder(all_rounder.at[index, 'Runs'], all_rounder.at[index, 'Ball'], float(all_rounder.at[index, 'Strike']), all_rounder.at[index, 'Wicket'], all_rounder.at[index, 'Over'],all_rounder.at[index, 'Economy'],all_rounder.at[index, 'Contri'])
    # Append the score to the list
    all_rounder_scores1.append(score)
    
row_indices2= [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56]

# Initialize an empty list to store the scores
all_rounder_scores2 = []

# Iterate over the row indices
for index in row_indices2:
    # Calculate the score for the current row
    score = totalPointsAllRounder(all_rounder.at[index, 'Runs'], all_rounder.at[index, 'Ball'], float(all_rounder.at[index, 'Strike']), all_rounder.at[index, 'Wicket'], all_rounder.at[index, 'Over'],all_rounder.at[index, 'Economy'],all_rounder.at[index, 'Contri'])
    # Append the score to the list
    all_rounder_scores2.append(score)
    
    
row_indices3= [2,7,12,17,22,27,32,37,42,47,52,57]
# Initialize an empty list to store the scores
all_rounder_scores3 = []

# Iterate over the row indices
for index in row_indices3:
    # Calculate the score for the current row
    score = totalPointsAllRounder(all_rounder.at[index, 'Runs'], all_rounder.at[index, 'Ball'], float(all_rounder.at[index, 'Strike']), all_rounder.at[index, 'Wicket'], all_rounder.at[index, 'Over'],all_rounder.at[index, 'Economy'],all_rounder.at[index, 'Contri'])
    # Append the score to the list
    all_rounder_scores3.append(score)
    


row_indices4= [3,8,13,18,23,28,33,38,43,48,53,58]
   
# Initialize an empty list to store the scores
all_rounder_scores4 = []

# Iterate over the row indices
for index in row_indices4:
    # Calculate the score for the current row
    score = totalPointsAllRounder(all_rounder.at[index, 'Runs'], all_rounder.at[index, 'Ball'], float(all_rounder.at[index, 'Strike']), all_rounder.at[index, 'Wicket'], all_rounder.at[index, 'Over'],all_rounder.at[index, 'Economy'],all_rounder.at[index, 'Contri'])
    # Append the score to the list
    all_rounder_scores4.append(score)
     
row_indices5= [4,9,14,19,24,29,34,39,44,49,54,59]
# Initialize an empty list to store the scores
all_rounder_scores5 = []

# Iterate over the row indices
for index in row_indices5:
    # Calculate the score for the current row
    score = totalPointsAllRounder(all_rounder.at[index, 'Runs'], all_rounder.at[index, 'Ball'], float(all_rounder.at[index, 'Strike']), all_rounder.at[index, 'Wicket'], all_rounder.at[index, 'Over'],all_rounder.at[index, 'Economy'],all_rounder.at[index, 'Contri'])
    # Append the score to the list
    all_rounder_scores5.append(score)
 
player_name = ['Shakib','Rashid','Maxwell','Jadeja','Jansen','Rachin','Hasranga','Pandya','Holder','Zampa','Head','Green']
dic={'Player':player_name,'Match1':all_rounder_scores1,'Match2':all_rounder_scores2,'Match3':all_rounder_scores3,'Match4':all_rounder_scores4,'Match5':all_rounder_scores5}
df=pd.DataFrame(dic)
d=df.T

d.to_csv("Project\\data\\finalAllRounder.csv")
    




