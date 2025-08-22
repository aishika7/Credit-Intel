import json
import pandas as pd
import numpy as np
from typing import List, Dict, Tuple
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import Score, FeatureSnapshot, Issuer
from app.config import settings
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
import lightgbm as lgb

FEATURES = [
    "ret_5d","ret_20d","vol_20d","ma_diff","market_cap","beta","ten_day_avg_vol","year_high","year_low"
]

class CreditModel:
    def __init__(self):
        # Start with a simple, interpretable baseline
        self.pipe = Pipeline([
            ("scaler", StandardScaler(with_mean=False)),
            ("clf", LogisticRegression(max_iter=1000))
        ])
        self.version = "v1"
        self.fitted = False

    def _prepare(self, df: pd.DataFrame) -> Tuple[pd.DataFrame, pd.Series]:
        X = df[FEATURES].fillna(0.0)
        # Synthetic label: use forward 20d drawdown as proxy risk (demo)
        y = (df["target"] > 0.1).astype(int)  # 1 = risky
        return X, y

    def fit(self, df: pd.DataFrame) -> Dict:
        if df.empty:
            return {"model_version": self.version, "n_samples": 0, "features": FEATURES}
        X, y = self._prepare(df)
        Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.25, random_state=42)
        self.pipe.fit(Xtr, ytr)
        self.fitted = True
        proba = self.pipe.predict_proba(Xte)[:,1]
        auc = roc_auc_score(yte, proba) if len(set(yte)) > 1 else None
        return {"model_version": self.version, "n_samples": int(len(df)), "features": FEATURES, "auc": auc}

    def score_row(self, row: Dict) -> float:
        import pandas as pd
        X = pd.DataFrame([row], columns=FEATURES).fillna(0.0)
        p = self.pipe.predict_proba(X)[:,1][0] if self.fitted else 0.5
        # Convert to 0-100 score (higher is better creditworthiness): invert risk
        return float(100.0 * (1.0 - p))

MODEL = CreditModel()