from pydantic import BaseModel, Field
from typing import Literal


class ChurnRequest(BaseModel):

    tenure_months: int = Field(..., ge=0)
    avg_session_duration: float = Field(..., ge=0)
    sessions_last_30_days: int = Field(..., ge=0)
    feature_usage_score: float = Field(..., ge=0, le=1)
    support_tickets_last_90_days: int = Field(..., ge=0)
    last_login_days_ago: int = Field(..., ge=0)
    monthly_spend_usd: float = Field(..., ge=0)
    payment_failures_last_6m: int = Field(..., ge=0)

    plan_type: Literal["free", "basic", "pro", "enterprise"]
    region: Literal["NA", "EU", "APAC", "LATAM"]

    is_annual_plan: int = Field(..., ge=0, le=1)


class ChurnResponse(BaseModel):
    churn_probability: float
    churn_prediction: int
