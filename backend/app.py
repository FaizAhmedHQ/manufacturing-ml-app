from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

model = joblib.load("model/manufacturing_model.pkl")


class InputData(BaseModel):
    Injection_Temperature: float
    Injection_Pressure: float
    Cycle_Time: float
    Cooling_Time: float
    Material_Viscosity: float
    Ambient_Temperature: float
    Machine_Age: int
    Operator_Experience: int
    Maintenance_Hours: float
    Shift: str
    Machine_Type: str
    Material_Grade: str
    Day_of_Week: str

@app.post("/predict")
def predict(data: InputData):

    df = pd.DataFrame([data.dict()])

    # Add missing columns expected by model
    df["Total_Cycle_Time"] = df["Cycle_Time"] + df["Cooling_Time"]

    df["Temperature_Pressure_Ratio"] = (
        df["Injection_Temperature"] / (df["Injection_Pressure"] + 1)
    )

    df["Efficiency_Score"] = 0.75
    df["Machine_Utilization"] = 0.80
    df["Timestamp"] = "2025-01-01"

    prediction = model.predict(df)[0]

    return {"parts_per_hour": round(prediction, 2)}
