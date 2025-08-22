from pydantic import BaseModel
from typing import List, Optional, Dict, Any
import datetime as dt

class IssuerOut(BaseModel):
    ticker: str
    name: str

class ScoreOut(BaseModel):
    ticker: str
    ts: dt.datetime
    score: float
    model_version: str

class FeatureImportanceOut(BaseModel):
    ticker: str
    ts: dt.datetime
    shap: Dict[str, float]

class EventOut(BaseModel):
    ticker: str
    source: str
    title: str
    url: str
    published_at: dt.datetime
    sentiment: float
    event_type: str
    impact: float
    summary: str

class TrainResult(BaseModel):
    model_version: str
    n_samples: int
    features: List[str]