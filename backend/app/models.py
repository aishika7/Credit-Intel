from sqlalchemy import Column, Integer, String, Float, DateTime, Text
from app.database import Base
import datetime as dt

class Issuer(Base):
    __tablename__ = "issuers"
    id = Column(Integer, primary_key=True)
    ticker = Column(String, unique=True, index=True)
    name = Column(String)

class Score(Base):
    __tablename__ = "scores"
    id = Column(Integer, primary_key=True)
    ticker = Column(String, index=True)
    ts = Column(DateTime, default=dt.datetime.utcnow, index=True)
    score = Column(Float)
    model_version = Column(String, default="v1")

class FeatureSnapshot(Base):
    __tablename__ = "feature_snapshots"
    id = Column(Integer, primary_key=True)
    ticker = Column(String, index=True)
    ts = Column(DateTime, default=dt.datetime.utcnow, index=True)
    features = Column(Text)  # JSON string of features

class NewsEvent(Base):
    __tablename__ = "news_events"
    id = Column(Integer, primary_key=True)
    ticker = Column(String, index=True)
    source = Column(String)
    title = Column(String)
    url = Column(String)
    published_at = Column(DateTime)
    sentiment = Column(Float)
    event_type = Column(String)  # e.g., governance, liquidity, leverage
    impact = Column(Float)  # -1..+1
    summary = Column(Text)