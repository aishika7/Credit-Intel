from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal
from app.models import Issuer, Score, FeatureSnapshot, NewsEvent
from app.schemas import IssuerOut, ScoreOut, FeatureImportanceOut, EventOut, TrainResult
from app.features import build_feature_vector
from app.model import MODEL, FEATURES
from app.explain import shap_explain
import json

router = APIRouter(prefix="/api", tags=["Credit-Intel"])

# Dependency for DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --------------------------
# Health check
# --------------------------
@router.get("/health")
def health_check():
    return {"status": "ok"}

# --------------------------
# Issuers
# --------------------------
@router.get("/issuers", response_model=List[IssuerOut])
def list_issuers(db: Session = Depends(get_db)):
    issuers = db.query(Issuer).all()
    return [{"ticker": i.ticker, "name": i.name} for i in issuers]

# --------------------------
# Credit Scores
# --------------------------
@router.get("/scores/{ticker}", response_model=List[ScoreOut])
def get_scores(ticker: str, db: Session = Depends(get_db)):
    rows = db.query(Score).filter(Score.ticker == ticker).order_by(Score.ts.desc()).limit(50).all()
    return rows

# --------------------------
# Feature Importance (SHAP)
# --------------------------
@router.get("/features/{ticker}", response_model=FeatureImportanceOut)
def get_features(ticker: str, db: Session = Depends(get_db)):
    snap = db.query(FeatureSnapshot).filter(FeatureSnapshot.ticker == ticker).order_by(FeatureSnapshot.ts.desc()).first()
    if not snap:
        raise HTTPException(status_code=404, detail="No features found for ticker")
    feats = json.loads(snap.features)
    shap_vals = shap_explain(feats)
    return {"ticker": ticker, "ts": snap.ts, "shap": shap_vals}

# --------------------------
# News / Events
# --------------------------
@router.get("/events/{ticker}", response_model=List[EventOut])
def get_events(ticker: str, db: Session = Depends(get_db)):
    events = db.query(NewsEvent).filter(NewsEvent.ticker == ticker).order_by(NewsEvent.published_at.desc()).limit(50).all()
    return events

# --------------------------
# Train / Retrain Model
# --------------------------
@router.post("/train", response_model=TrainResult)
def train_model(db: Session = Depends(get_db)):
    snaps = db.query(FeatureSnapshot).all()
    if not snaps:
        raise HTTPException(status_code=400, detail="No training data available")
    rows = []
    for s in snaps:
        feats = json.loads(s.features)
        feats["target"] = 0.0  # 🔹 placeholder: define proper label if you have default/credit event info
        rows.append(feats)
    import pandas as pd
    df = pd.DataFrame(rows)
    result = MODEL.fit(df)
    return result

# --------------------------
# Score On Demand
# --------------------------
@router.get("/score-now/{ticker}")
def score_now(ticker: str):
    feats = build_feature_vector(ticker)
    score = MODEL.score_row({k: feats.get(k, 0.0) for k in FEATURES})
    return {"ticker": ticker, "score": score, "features": feats}
               