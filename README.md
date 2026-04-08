Phase 1 — Project Setup

--Project Structure--

data/ → stores the Titanic CSV files
notebooks/ → stores Jupyter notebooks for analysis
src/ → stores Python source code
tests/ → stores test files

--Requirements.txt--

pandas  - Read and manipulate data
scikit  - learnBuild ML model
mlflow  - Track experiments
fastapi - Build the API
uvicorn - Run the API server
joblib  - Save/load the trained model
pytest  - Write and run tests

--Created Virtual Environment--

python3 -m venv venv
source venv/bin/activate

--Installed Dependencies--

pip install -r requirements.txt

--Github--

git init
git add .
git commit -m "initial project structure"

Created new repository in GitHub - Titanic-ml-api
git remote add origin https://github.com/icy2701/titanic-ml-api.git
git branch -M main
git push -u origin main

Phase 2 — EDA (Exploratory Data Analysis)

--Installed Jupyter and Opened It--

bashpip install jupyter
jupyter notebook

--Created the Notebook--

Went to notebooks/ folder in Jupyter
Clicked File → New → Notebook
Selected Python 3 as kernel
Renamed it to 01_eda.ipynb





