[![CI Pipeline](https://github.com/icy2701/Titanic-ML-API/actions/workflows/ci.yml/badge.svg)](https://github.com/icy2701/Titanic-ML-API/actions/workflows/ci.yml)
![Docker](https://img.shields.io/docker/pulls/aisi27/titanic-api)

# 🚢 Titanic ML API

End-to-end ML pipeline: Random Forest (82%) + MLflow tracking → 
FastAPI REST API → Docker containerized → CI/CD with GitHub Actions

---

## Problem
Predict whether a Titanic passenger would survive based on 
their details — class, age, sex, fare, and family size.

## Solution
Trained a Random Forest classifier on 891 passengers with 
MLflow experiment tracking. Served the best model (82% accuracy) 
via a FastAPI REST API. Containerized with Docker. 
Automated testing with pytest and CI with GitHub Actions.

## Architecture

Raw Data → Feature Engineering → Model Training (MLflow) 
→ FastAPI /predict → Docker Container → GitHub Actions CI

## How to Run

### Option 1 — Docker (recommended)
docker pull USERNAME/titanic-api:v1.0
docker run -p 8000:8000 USERNAME/titanic-api:v1.0

### Option 2 — Local
git clone https://github.com/icy2701/titanic-ml-api.git
cd titanic-ml-api
pip install -r requirements.txt
uvicorn src.main:app --reload

Open: http://localhost:8000/docs

## Run Tests
pytest tests/ -v

## MLflow Experiments
cd notebooks
mlflow ui --port 5001
Open: http://localhost:5001
