from fastapi import FastAPI
import pandas as pd
import joblib
from pathlib import Path
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse

from api.schemas import ChurnRequest, ChurnResponse


app = FastAPI(
    title="Customer Churn Prediction API",
    description="Predicts churn probability for SaaS customers.",
    version="1.0"
)

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "model" / "churn_model.pkl"

@app.on_event("startup")
def load_model():
    global model
    model = joblib.load(MODEL_PATH)



@app.get("/")
def health_check():
    return {"status": "API is running"}


from pathlib import Path

UI_PATH = BASE_DIR / "ui" / "index.html"

@app.get("/ui")
def serve_ui():
    return FileResponse(UI_PATH)



@app.post("/predict", response_model=ChurnResponse)
def predict_churn(request: ChurnRequest):

    
    input_df = pd.DataFrame([request.dict()])

    
    probability = model.predict_proba(input_df)[0][1]

    prediction = int(probability >= 0.5)

    return ChurnResponse(
        churn_probability=round(float(probability), 4),
        churn_prediction=prediction
    )
