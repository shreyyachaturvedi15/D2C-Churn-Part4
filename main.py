
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Load model
model = joblib.load("fresh_model.pkl")

app = FastAPI(title="Churn Prediction API")


class CustomerData(BaseModel):
    gross_amount: float
    quantity: int
    returned: float
    rating: float
    discount_pct: float
    delivery_days: float
    city_tier: int
    age_group: int
    acquisition_channel: int
    loyalty_tier: int
    preferred_category: int
    skin_type: int
    marketing_consent: int


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/predict")
def predict(data: CustomerData):

    df = pd.DataFrame([data.dict()])

    prediction = int(model.predict(df)[0])

    probability = float(model.predict_proba(df)[0][1])

    risk = "High Risk" if probability > 0.5 else "Low Risk"

    return {
        "churn_prediction": prediction,
        "churn_probability": round(probability, 4),
        "risk_level": risk
    }


@app.post("/batch_predict")
def batch_predict(data: list[CustomerData]):

    df = pd.DataFrame([item.dict() for item in data])

    predictions = model.predict(df)

    probabilities = model.predict_proba(df)

    results = []

    for pred, prob in zip(predictions, probabilities):

        results.append({
            "prediction": int(pred),
            "probability": round(float(prob[1]), 4)
        })

    return results
