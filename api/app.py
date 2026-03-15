import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

# загрузка модели
model = joblib.load("model.pkl")

app = FastAPI()

class ClientData(BaseModel):
    age: int
    balance: int
    duration: int
    campaign: int

@app.get("/")
def home():
    return {"message": "API working"}

@app.post("/predict")
def predict(data: ClientData):

    features = np.array([[ 
        data.age,
        data.balance,
        data.duration,
        data.campaign
    ]])

    prediction = model.predict(features)

    return {"prediction": int(prediction[0])}