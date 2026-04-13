from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

#FastAPI -> Creates the web app ->The restaurant itself
#BaseModel -> Validates incoming data ->Bouncer at the door
#joblib -> Loads saved model -> Opens the saved game
#numpy -> Handles number arrays 

app=FastAPI()

model=joblib.load('model/rf_best.pkl')

class Passenger(BaseModel):
    Pclass :int
    Sex:int
    Age:float
    SibSp:int
    Parch:int
    Fare:float
    Embarked_Q:int
    Embarked_S:int
    Embarked_C:int
    FamilySize:int

@app.post('/predict')
def predict(passenger:Passenger):
    data=np.array([[
        passenger.Pclass,
        passenger.Sex,
        passenger.Age,
        passenger.SibSp,
        passenger.Parch,
        passenger.Fare,
        passenger.Embarked_Q,
        passenger.Embarked_S,
        passenger.Embarked_C,
        passenger.FamilySize
    ]])



#@          → this is called a "decorator"
#             it adds extra behaviour to the function below it
#app        → our FastAPI application
#.post      → this accepts POST requests
#"/predict" → the URL where this lives
 #            full URL = http://localhost:8000/predict


    pred=model.predict(data)

#model.predict()  → asks model to make a prediction
#data             → the passenger details we just formatted

#Returns:
#pred = [1]   → this passenger survived
#pred = [0]   → this passenger died

    prob=model.predict_proba(data)

#predict_proba()  → predict PROBABILITY
#                   not just yes/no

#Returns:
#prob = [[0.23, 0.77]]
#         ↑      ↑
#       23%    77%
#       died  survived

    return {
        'survived':int(pred[0]),
        'probability':float(prob[0][1])
    }

#predict()       → "it will rain" (yes/no)
#predict_proba() → "77% chance of rain" (confidence)