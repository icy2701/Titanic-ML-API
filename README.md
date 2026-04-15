[![CI Pipeline](https://github.com/icy2701/Titanic-ML-API/actions/workflows/ci.yml/badge.svg)](https://github.com/icy2701/Titanic-ML-API/actions/workflows/ci.yml)

# 🚢 Titanic ML API

A machine learning project to predict Titanic survival, served via a FastAPI web API.

---

## 📁 Project Structure


titanic-ml-api/
├── data/         → stores the Titanic CSV files
├── notebooks/    → stores Jupyter notebooks for analysis
├── src/          → stores Python source code
├── tests/        → stores test files
└── requirements.txt


## ⚙️ Phase 1 — Project Setup

### Dependencies (`requirements.txt`)

| Package        | Purpose                        |
|----------------|--------------------------------|
| `pandas`       | Read and manipulate data       |
| `scikit-learn` | Build ML model                 |
| `mlflow`       | Track experiments              |
| `fastapi`      | Build the API                  |
| `uvicorn`      | Run the API server             |
| `joblib`       | Save/load the trained model    |
| `pytest`       | Write and run tests            |

### Virtual Environment

python3 -m venv venv
source venv/bin/activate        # Mac/Linux

### Install Dependencies

pip install -r requirements.txt

### Git & GitHub Setup

# Initialize git
git init
git add .
git commit -m "chore: initial project structure"

# Push to GitHub
Created new repository in GitHub - Titanic-ml-api
git remote add origin https://github.com/icy2701/titanic-ml-api.git
git branch -M main
git push -u origin main

## 📊 Phase 2 — EDA (Exploratory Data Analysis)

### Setup Jupyter

pip install jupyter
jupyter notebook


### Notebook Created
- Navigated to `notebooks/` folder in Jupyter
- Clicked **File → New → Notebook**
- Selected **Python 3** as kernel
- Renamed to `01_eda.ipynb`

### Key Findings from EDA

| Column     | Finding                              |
|------------|--------------------------------------|
| `Age`      | 177 missing values                   |
| `Cabin`    | 687 missing values                   |
| `Embarked` | 2 missing values                     |
| `Sex`      | Females had 74% survival rate        |
| `Pclass`   | 1st class had 63% survival rate      |


git add .
git commit -m "feat: EDA notebook — missing values + distributions"
git push


## 🛠️ Phase 3 — Feature Engineering

Raw Data                      Clean Data
──────────────────────────    ──────────────────────────────
Age: 177 missing         →    Filled with median (28.0)
Sex: male/female         →    Encoded to 0/1
Embarked: S/C/Q          →    One-hot encoded (3 columns)
  + 2 missing            →    Filled with mode (S)
Name, Ticket,            →    Dropped (useless columns)
  Cabin, PassengerId
SibSp + Parch            →    Combined into FamilySize


git add .
git commit -m "feat: feature engineering — encoding + new FamilySize feature"
git push

## Phase 4 — Model Training + MLflow Experiment Tracking

MLflow is a lab notebook for ML experiments. It automatically tracks:

Parameters → settings you chose (n_estimators, max_depth)
Metrics → results you got (accuracy, f1 score)
Artifacts → the actual saved model files

891 passengers
│
├── 712 passengers (80%) → TRAINING
│     ├── X_train → their details (age, sex, class...)
│     └── y_train → their actual survival answers
│
└── 179 passengers (20%) → TESTING
      ├── X_test  → their details (age, sex, class...)
      └── y_test  → their actual survival answers

X_train -> 712 pratice questions 
y_train -> 712 pratice answers

X_test -> 179 real exam questions
Y_test -> the answer key for 179 questions which is hidden from model.

TRAINING PHASE (model is studying):
──────────────────────────────────
X_train → model looks at passenger details
y_train → model checks if its guess was right
          keeps adjusting until it gets better
          (like studying with answer key)


TESTING PHASE (model is being examined):
─────────────────────────────────────────
X_test  → model sees NEW passenger details
          and makes predictions → called y_pred

y_test  → we compare y_pred vs y_test
          to see how accurate the model is
          (like marking the exam)
    
y_pred = model.predict(X_test)

We give the model X_test (179 exam questions)
It gives back y_pred (its 179 guesses)


The model predicted for each one: survived (1) or died (0).
We then compared its answers to the real answers and calculated:
Correct predictions: 145 out of 179
Accuracy = 145 ÷ 179 = 81% ✅
81% means out of every 100 passengers, it correctly predicted 81 of them.
F1 Score - is the model reliable at finding survivors specifically?
Our score: 0.77 → decent! ✅

Exp 1 → 100 detectives, medium experience  → 81% accuracy
Exp 2 → 50 detectives,  high experience   → 80% accuracy
Exp 3 → 200 detectives, low experience    → 79% accuracy
Exp 4 → 300 detectives, high experience   → 83% accuracy ← BEST!

Think of it like a metal detector:

Accuracy = how often it beeps correctly overall
F1 = how good it is specifically at finding actual metal

# Always run from notebooks/ folder
cd titanic-ml-api/notebooks
source ../venv/bin/activate
mlflow ui --port 5001

git add .
git commit -m "feat: MLflow experiment tracking — 4 runs logged"
git push

## 🌐 Phase 5 — FastAPI Prediction Endpoint

### What We Built
A web API that takes passenger details and returns
survival prediction + probability.

### Folder Created
- `model/` → stores the saved model file `rf_best.pkl`

### Save Best Model - 03.model.ipynb
import joblib
joblib.dump(model, '../model/rf_best.pkl')


### Complete src/main.py

### Run the API

uvicorn src.main:app --reload

### Test in Browser 
http://localhost:8000/docs

### Test — 1st class female (should survive)
```json
{
    "Pclass": 1,
    "Sex": 1,
    "Age": 28.0,
    "SibSp": 1,
    "Parch": 0,
    "Fare": 71.28,
    "Embarked_C": 1,
    "Embarked_Q": 0,
    "Embarked_S": 0,
    "FamilySize": 2
}
```
Response:
```json
{
    "survived": 1,
    "probability": 0.96
}
```

### Test — 3rd class male (should not survive)
```json
{
    "Pclass": 3,
    "Sex": 0,
    "Age": 22.0,
    "SibSp": 1,
    "Parch": 0,
    "Fare": 7.25,
    "Embarked_C": 0,
    "Embarked_Q": 0,
    "Embarked_S": 1,
    "FamilySize": 2
}
```
Response:
```json
{
    "survived": 0,
    "probability": 0.18
}
```

### Commit

git add .
git commit -m "feat: FastAPI /predict endpoint with Pydantic validation"
git push

# 🐳 Phase 6 — pytest + Docker

---

## What We Built
Automated tests to verify the API works, and a Docker container so the API runs on any machine identically.

---

## 🧪 Part 1 — pytest (Automated Testing)

### Install Dependencies

pip install pytest httpx
pip freeze > requirements.txt

pytest → runs the tests
httpx → lets TestClient make fake requests to the API without starting a real server

### Folder and Files Created

mkdir -p tests
touch tests/__init__.py
touch tests/test_api.py


tests/ → folder that holds all test files
__init__.py → empty file that makes tests/ a Python package so imports work
test_api.py → where we write the actual tests

### tests/test_api.py

### What Each Test Does

| Test | What it sends | What it checks |
|---|---|---|
| test_predict_returns_200 | Complete valid passenger | Status 200 + survived + probability keys exist |
| test_missing_fields_returns_422 | Only one field | Status 422 (Pydantic rejects incomplete data) |

### Run Tests

pytest tests/ -v

### Expected Output

tests/test_api.py::test_predict_returns_200 PASSED
tests/test_api.py::test_missing_fields_returns_422 PASSED

2 passed in 1.23s

## 🐳 Part 2 — Docker (Containerization)

### What Docker Does

Without Docker:
Your laptop → needs Python installed → needs venv → needs packages → maybe works

With Docker:
Any machine → has Docker → run one command → always works

### Files Created

titanic-ml-api/
├── Dockerfile        → instructions to build the container
└── .dockerignore     → files to exclude from the container


### Dockerfile

### .dockerignore

### Why Each Line is Excluded

venv/          → 200-500MB, Docker installs packages fresh from requirements.txt
__pycache__/   → Python auto-generated files, not needed
*.pyc          → compiled Python bytecode, not needed
.git/          → git history, container doesn't need it
mlruns/        → MLflow experiment logs, container only needs rf_best.pkl
notebooks/     → Jupyter notebooks, container only runs the API
.pytest_cache/ → pytest temporary files, not needed in production

### Build the Image

docker build -t titanic-api .

docker build   → read Dockerfile and build an image
-t titanic-api → name the image "titanic-api"
.              → look for Dockerfile in current folder

First time takes 2-3 minutes. After that much faster because of caching.

### Run the Container


docker run -p 8000:8000 titanic-api

docker run      → start a container from the image
-p 8000:8000    → connect port 8000 on your laptop to port 8000 inside container
titanic-api     → name of the image to run



### Test It

Open browser → http://localhost:8000/docs
Same API, same predictions, but now running inside Docker

### Useful Docker Commands

# See all running containers
docker ps

# Stop a container
docker stop <container_id>

# Run in background (so terminal stays free)
docker run -d -p 8000:8000 titanic-api

# See all images you have built
docker images


## Commit

git add tests/ Dockerfile .dockerignore requirements.txt
git commit -m "feat: Dockerfile + pytest tests passing"
git push origin main
