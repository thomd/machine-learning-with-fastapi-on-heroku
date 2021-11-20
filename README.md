# Train ML Model for FastAPI and Deploy on Heroku

* [FastAPI](https://fastapi.tiangolo.com) is a Web framework for developing RESTful APIs in Python.
* [Heroku](https://www.heroku.com) is a cloud platform as a service supporting several programming languages.

## Setup

Create Environment

    conda env create --file environment.yaml
    conda activate ml-fastapi-heroku

## 1. Data Analysis and Cleaning

Data is from the [Pima Indians Diabetes Database](https://data.world/data-society/pima-indians-diabetes-database).

Analyse and clean the data: [data-analysis.ipynb](./data-analysis.ipynb)

Compare original dataset with cleaned dataset with

    npx daff --www data/original/diabetes.csv data/diabetes.csv

## 2. Train Prediction Model

Traing of a model using a **random forest classifier**: [train-model.ipynb](./train-model.ipynb)

Test model with:

    import pickle
    model = pickle.load(open('model/model.pkl', 'rb'))
    p = model.predict_proba([[2,150,100,23,125,28,1,42]])
    print(p)

## 3. FastAPI Application

Start API server with

    uvicorn app:app --reload

Open Swagger UI:

    open http://localhost:8000/docs

