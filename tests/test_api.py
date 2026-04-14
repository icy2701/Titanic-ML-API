from urllib import response

from fastapi.testclient import TestClient
from src.main import app

#Pytest is the standard Python testing framework. It finds your test files automatically and runs them.
#FastAPI's TestClient uses httpx under the hood to make fake HTTP requests to your API without actually starting a real server.
#Without it, TestClient won't work.

##Creates the fake browser connected to your app.
client=TestClient(app)

#pytest automatically finds any function that starts with test_. This tests the happy path — everything correct.
def test_predict_returns_200():
    payload={
        "Pclass":1,
        "Sex":1,
        "Age":28.0,
        "SibSp":1,
        "Parch":0,
        "Fare":71.28,
        "Embarked_C":1,
        "Embarked_Q":0,
        "Embarked_S":0,
        "FamilySize":2       

    }

    #Sends a POST request to your /predict endpoint with that data.

    response=client.post('/predict',json=payload)
    assert response.status_code==200
    assert "survived" in response.json()
    assert "probability" in response.json()

#This tests the sad path — what happens when bad data is sent.
def testing_missing_fields_returns_422():
    payload = {
        "Pclass":1
    }

    response=client.post('/predict',json=payload)
    assert response.status_code==422

