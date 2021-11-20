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
    p = model.predict_proba([[7,100,72,23,30.5,30.0,0.484,32]])
    print(p)

## 3. FastAPI Application

For local testing, start server with

    uvicorn app:app --reload

and open Swagger-UI:

    open http://localhost:8000/docs

## 4. Deploy on Heroku

    pip list --format=freeze > requirements.txt
    heroku login
    heroku create predict-diabetes-1
    git push heroku main
    heroku ps:scale web=1
    heroku logs --tail
    heroku open

## 5. Use API

    curl -s 'https://predict-diabetes-1.herokuapp.com/predict' \
         -H 'Content-Type: application/json' \
         -d '{"pregnancies":1,"glucose":89,"bp":66,"skinthickness":23,"insulin":94,"bmi":43,"dpf":0.167,"age":21}'
