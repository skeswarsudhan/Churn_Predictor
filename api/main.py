from fastapi import FastAPI
import pandas as pd
import joblib
from pathlib import Path
from fastapi.responses import HTMLResponse
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware


from api.schemas import ChurnRequest, ChurnResponse


app = FastAPI(
    title="Customer Churn Prediction API",
    description="Predicts churn probability for SaaS customers.",
    version="1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://skeswarsudhan.github.io",  
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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




@app.post("/predict", response_model=ChurnResponse)
def predict_churn(request: ChurnRequest):

    
    input_df = pd.DataFrame([request.dict()])

    
    probability = model.predict_proba(input_df)[0][1]

    prediction = int(probability >= 0.5)

    return ChurnResponse(
        churn_probability=round(float(probability), 4),
        churn_prediction=prediction
    )
