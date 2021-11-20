from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn
import pickle
from pydantic import BaseModel

app = FastAPI()

model = pickle.load(open("model/model.pkl", "rb"))


class Women(BaseModel):
    pregnancies: int
    glucose: int
    bp: int
    skinthickness: int
    insulin: int
    bmi: float
    dpf: float
    age: int


@app.get("/")
def docs():
    return RedirectResponse(url="/docs")


@app.post("/predict")
def predict(req: Women):
    preg = req.pregnancies
    glucose = req.glucose
    bp = req.bp
    skinthickness = req.skinthickness
    insulin = req.insulin
    bmi = req.bmi
    dpf = req.dpf
    age = req.age
    features = list([preg, glucose, bp, skinthickness, insulin, bmi, dpf, age])
    predict = model.predict([features])
    prob = model.predict_proba([features])
    if predict == 1:
        return {"prediction": f"positive with {prob[0][1]} probability"}
    else:
        return {"prediction": f"negative with {prob[0][0]} probability"}


if __name__ == "__main__":
    uvicorn.run(app)
