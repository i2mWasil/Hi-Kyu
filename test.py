import pandas as pd
import numpy as np
import os


# function for loading data
file_path = os.path.join(os.getcwd(), "data")


def load_data(filename, file_path=file_path):
    csv_path = os.path.join(file_path, filename)
    return pd.read_csv(csv_path)


# read the data
points_table = load_data("points_table.csv")
points_table["Net R/R"] = points_table["Net R/R"].round(3)
print(points_table)

wins_losses = load_data("wins_losses.csv")
wins_losses.sort_values(by=["Titles", "Win %"], ascending=[False, False], inplace=True)
wins_losses.drop("Span", axis=1, inplace=True)
print(wins_losses)

# read batting data
batting = load_data("batting.csv")
batting.iloc[batting[batting["PLAYER"] == "Rohit Sharma"].index, 16] = "Mumbai Indians"
#batting_players_list = list(batting["PLAYER"].unique())
print(batting)

# batting aggregated data
batting_agg = load_data("batting_all_time.csv")
print(batting_agg)


# read bowling data
bowling = load_data("bowling.csv")
bowling = bowling.rename(columns={"Maid": "Maiden"})
#bowling_players_list = list(bowling["PLAYER"].unique())
print(bowling)
# create a new column
bowling["Runs/Inns"] = (bowling["Runs"] / bowling["Inns"]).round(2)
print(bowling)

# read bowling aggregated data
bowling_agg = load_data("bowling_all_time.csv")
print(bowling_agg)

# copy the data that is not avialable in aggregated csv
bowling_subset = bowling[["PLAYER", "Dots", "Maiden"]].copy()
# calculate aggregates and join
bs_groupby = bowling_subset.groupby("PLAYER").sum().reset_index()
bowling_agg = pd.merge(
    left=bowling_agg, right=bs_groupby, left_on="PLAYER", right_on="PLAYER"
)
# delete un-necessary column
bowling_agg.drop("Player Link", axis=1, inplace=True)
# create a new column
bowling_agg["Runs/Inns"] = (bowling_agg["Runs"] / bowling_agg["Inns"]).round(2)


batting_metrics_list = [
    "Runs",
    "HS",
    "Avg",
    "BF",
    "SR",
    "100",
    "50",
    "4s",
    "6s",
    "Mat",
    "Inns",
    "NO",
]

bowling_metrics_list = [
    "Wkts",
    "Econ",
    "Avg",
    "SR",
    "Runs/Inns",
    "Dots",
    "4w",
    "5w",
    "Maiden",
    "Ov",
]

team_list = [
    "All Teams",
    "Sunrisers Hyderabad",
    "Kings Xi Punjab",
    "Mumbai Indians",
    "Delhi Capitals",
    "Kolkata Knight Riders",
    "Royal Challengers Bangalore",
    "Chennai Super Kings",
    "Rajasthan Royals",
]