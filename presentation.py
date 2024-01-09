# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#import the Data set
import pandas as pd
#import numpy as np
from sklearn.linear_model import LogisticRegression
testdata = pd.read_csv('C:/Users/Dell/FYP/modelTest.csv')
testdata.rename(columns={'Unnamed: 0':'index'},inplace=True)
testdata1 = testdata.drop(['index'], axis=1)
x_col = ['IA PPG', 'ScoreVal', 'MP', 'OBPM', 'FTA/100']
x1 = testdata[x_col]
y1 = testdata['allStar']

Data = pd.read_csv('C:/Users/Dell/FYP/modelFit.csv')
Data = Data.drop(Data.query('allStar < 1').sample(frac=.62).index)#drop xtra non allStar
x_col = ['IA PPG', 'ScoreVal', 'MP', 'OBPM', 'FTA/100']
x = Data[x_col]
y = Data['allStar']
    
#function of defining model and fitting in data, return model
def model(x, y):
    model = LogisticRegression(C=0.0001, max_iter=100, penalty='l2', solver='lbfgs')
    model.fit(x,y)
    return model
#function of printout the players to be predict
def start():
    dropcol = ['allStar','1stAS_yr','yr2AS']
    testprint = testdata1.drop(dropcol, axis=1)
    print('Players to predict available: ')
    print(testprint)
#ask for user input and perform prediction  
def predict():
    pName = input('Enter player name to predict:\n')
    for i in range (8): 
        if pName == testdata.iloc[i, 1]:
            if results.iloc[i,0]==1:
                print('Selected Player is projected to become All-Star.')
                print('Probabilty of selected player becoming All-Star: ', prob.iloc[i,1])
            else:
                print('Selected Player is NOT projected to become All-Star.')
                print('Probabilty of selected player becoming All-Star: ', prob.iloc[i,1])
                break;

#initiate the model and prepare results
model = model(x,y)
results = pd.DataFrame(model.predict(x1))
prob = pd.DataFrame(model.predict_proba(x1))

#run the user interface
decision = 'y'
while decision!='n':
    start()
    predict()
    decision = input('Do you want to select another player? (y/n): ')
    
    
