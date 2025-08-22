from apscheduler.schedulers.background import BackgroundScheduler
from sqlalchemy.orm import Session
from app.config import settings
from app.database import SessionLocal
from app.models import Issuer, Score, FeatureSnapshot, NewsEvent
from app.features import build_feature_vector
from app.ingestion.unstructured import fetch_rss
from app.model import MODEL
import json
import datetime as dt

sched = BackgroundScheduler(timezone="UTC")


def refresh_structured():
    db: Session = SessionLocal()
    try:
        issuers = db.query(Issuer).all()
        now = dt.datetime.utcnow()
        for iss in issuers:
            feats = build_feature_vector(iss.ticker)
            snap = FeatureSnapshot(ticker=iss.ticker, ts=now, features=json.dumps(feats))
            db.add(snap)
            score = MODEL.score_row({k: feats.get(k, 0.0) for k in MODEL.pipe.feature_names_in_}) if MODEL.fitted else 50.0
            db.add(Score(ticker=iss.ticker, ts=now, score=score, model_version=MODEL.version))
        db.commit()
    finally:
        db.close()


def refresh_unstructured():
    db: Session = SessionLocal()
    try:
        df = fetch_rss()
        now = dt.datetime.utcnow()
        for _, r in df.iterrows():
            event = NewsEvent(
                ticker="*",  # generic; mapping to issuer can be improved via NER + ticker dictionary
                source=r["source"],
                title=r["title"],
                url=r["url"],
                published_at=r["published_at"],
                sentiment=float(r["sentiment"]),
                event_type=r["event_type"],
                impact=float(r["impact"]),
                summary=r.get("summary", r["title"]) if isinstance(r.get("summary", ""), str) else r["title"],
            )
            db.add(event)
        db.commit()
    finally:
        db.close()


def start_scheduler():
    sched.add_job(refresh_structured, "interval", minutes=settings.REFRESH_MINUTES, id="structured")
    sched.add_job(refresh_unstructured, "interval", minutes=settings.REFRESH_MINUTES, id="unstructured", next_run_time=None)
    sched.start()