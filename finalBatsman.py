# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 09:17:00 2024

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


def runsBatsman(score, run):
    if(run >= 0 and run <=10):
        score += run*1
    elif(run > 10 and run <= 30):
        score += 10 + 0.5*(run - 10)
    elif(run > 30 and run <= 50):
        score += 20 + 0.5*(run - 30)
    else:
        score += 40
    return score

def strikeRateBatsman(score, strike, ball):
    if(strike <= 50 and ball > 5):
        score -= 5
    elif(strike > 50 and strike <= 100):
        score += 0.1*(strike)
    elif(strike > 100 and strike <= 150):
        score += 5 + 0.1*(strike - 100)
    elif(strike > 150 and strike <= 200):
        score += 10 + 0.1*(strike - 150)
    else:
        score += 20
    return score

def boundariesBatsman(score, boundr):
    if(boundr >= 0 and boundr <=3):
        score += 0
    elif(boundr > 3 and boundr <= 7):
        score += 1.25*(boundr - 3)
    elif(boundr > 7 and boundr <= 10):
        score += 5 + (5/3)*(boundr - 7)
    elif(boundr > 10 and boundr <= 15):
        score += boundr
    else:
        score += 20
    return score

def teamContributionBatsman(score, contri):
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


def totalPointsBatsman(run, ball, strike, boundr, contri):
    score = 0
    score = runsBatsman(score, run)
    score = strikeRateBatsman(score, strike, ball)
    score = boundariesBatsman(score, boundr)
    score = teamContributionBatsman(score, contri)
    return score


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



#ALL ROUNDER

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
    score = teamContributionBowler(score, contri)
    return score


batting=load_data("C:/Users/prite/Downloads/Batsman - Sheet1 (6).csv")
print(batting)



row_indices1= [0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75]

# Initialize an empty list to store the scores
batting_scores1 = []

# Iterate over the row indices
for index in row_indices1:
    # Calculate the score for the current row
    score = totalPointsBatsman(batting.at[index, 'run'], batting.at[index, 'ball'], float(batting.at[index, 'strike']), batting.at[index, 'boundr'], batting.at[index, 'contri'])
    # Append the score to the list
    batting_scores1.append(score)

row_indices2= [1, 6, 11, 16, 21, 26, 31, 36, 41, 46, 51, 56, 61, 66, 71, 76]

# Initialize an empty list to store the scores
batting_scores2 = []

# Iterate over the row indices
for index in row_indices2:
    # Calculate the score for the current row
    score = totalPointsBatsman(batting.at[index, 'run'], batting.at[index, 'ball'], float(batting.at[index, 'strike']), batting.at[index, 'boundr'], batting.at[index, 'contri'])
    # Append the score to the list
    batting_scores2.append(score)
    
row_indices3= [2,7,12,17,22,27,32,37,42,47,52,57,62,67,72,77]

# Initialize an empty list to store the scores
batting_scores3 = []

# Iterate over the row indices
for index in row_indices3:
    # Calculate the score for the current row
    score = totalPointsBatsman(batting.at[index, 'run'], batting.at[index, 'ball'], float(batting.at[index, 'strike']), batting.at[index, 'boundr'], batting.at[index, 'contri'])
    # Append the score to the list
    batting_scores3.append(score)
    
row_indices4= [3,8,13,18,23,28,33,38,43,48,53,58,63,68,73,78]
    
batting_scores4 = []

# Iterate over the row indices
for index in row_indices4:
    # Calculate the score for the current row
    score = totalPointsBatsman(batting.at[index, 'run'], batting.at[index, 'ball'], float(batting.at[index, 'strike']), batting.at[index, 'boundr'], batting.at[index, 'contri'])
    # Append the score to the list
    batting_scores4.append(score)

row_indices5= [4,9,14,19,24,29,34,39,44,49,54,59,64,69,74,79]
    
batting_scores5 = []

# Iterate over the row indices
for index in row_indices5:
    # Calculate the score for the current row
    score = totalPointsBatsman(batting.at[index, 'run'], batting.at[index, 'ball'], float(batting.at[index, 'strike']), batting.at[index, 'boundr'], batting.at[index, 'contri'])
    # Append the score to the list
    batting_scores5.append(score)
    
player_name=['David Warner','Shubhman Gill','Mitch Marsh','Virat Kohli','Joe Root','MS Dhoni','Rohit Sharma','Steve Smith','Pritesh','Abhinav','Ayan','Wasil','Chris Gayle','Kane Williamson','Ben Stokes','Ishan Kishan']
dic={'Player':player_name,'Match1':batting_scores1,'Match2':batting_scores2,'Match3':batting_scores3,'Match4':batting_scores4,'Match5':batting_scores5}
df=pd.DataFrame(dic)
d=df.T

d.to_csv("batsmen.csv")








              




