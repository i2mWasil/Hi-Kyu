import pandas as pd
import sklearn as sk
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

def ps(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(np.array([6]).reshape(1, -1))
    print(y_pred)


data = pd.read_csv('finalbatman.csv')
X = data[['Match']]
y_DW = data['David Warner']
y_SG = data['Shubhman Gill']
y_MM = data['Mitch Marsh']
y_VK = data['Virat Kohli']
y_JR = data['Joe Root']
y_MSD = data['MS Dhoni']
y_RS = data['Rohit Sharma']
y_SS = data['Steve Smith']
y_P = data['Pritesh']
y_Ab = data['Abhinav']
y_Ay = data['Ayan']
y_W = data['Wasil']
y_CG = data['Chris Gayle']
y_KW = data['Kane Williamson']
y_BS = data['Ben Stokes']
y_IK = data['Ishan Kishan']
ps(X,y_DW)
ps(X,y_SG)
ps(X,y_MM)
ps(X,y_VK)
ps(X,y_JR)
ps(X,y_MSD)
ps(X,y_RS)
ps(X,y_SS)
ps(X,y_P)
ps(X,y_Ab)
ps(X,y_Ay)
ps(X,y_W)
ps(X,y_CG)
ps(X,y_KW)
ps(X,y_BS)
ps(X,y_IK)
ps(X,y_DW)


