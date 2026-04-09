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


