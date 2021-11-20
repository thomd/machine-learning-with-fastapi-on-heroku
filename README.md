# Train ML Model for FastAPI and Deploy on Heroku

* [FastAPI](https://fastapi.tiangolo.com) is a Web framework for developing RESTful APIs in Python.
* [Heroku](https://www.heroku.com) is a cloud platform as a service supporting several programming languages.

## Setup

Create Environment

    conda env create --file environment.yaml
    conda activate ml-fastapi-heroku

## Data Analysis and Cleaning

We use the [Pima Indians Diabetes Database](https://data.world/data-society/pima-indians-diabetes-database) to create a prediciton model.

First we analyse and clean the data: [data-analysis.ipynb](./data-analysis.ipynb)

Compare original dataset with cleaned dataset with

    npx daff --www data/original/diabetes.csv data/diabetes.csv


