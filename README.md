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
