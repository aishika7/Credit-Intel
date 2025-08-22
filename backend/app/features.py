import pandas as pd
import numpy as np
import datetime as dt
from app.config import settings
from app.ingestion.structured import fetch_prices, basic_financial_features

def rolling_features(price_df: pd.DataFrame) -> dict:
    out = {}
    if price_df.empty:
        return out
    close = price_df["Close"] if "Close" in price_df else price_df.iloc[:,0]
    out["ret_5d"] = close.pct_change(5).iloc[-1]
    out["ret_20d"] = close.pct_change(20).iloc[-1]
    out["vol_20d"] = close.pct_change().rolling(20).std().iloc[-1]
    out["ma_short"] = close.rolling(settings.SHORT_WINDOW).mean().iloc[-1]
    out["ma_long"] = close.rolling(settings.LONG_WINDOW).mean().iloc[-1]
    out["ma_diff"] = out["ma_short"] - out["ma_long"] if not np.isnan(out.get("ma_short", np.nan)) and not np.isnan(out.get("ma_long", np.nan)) else np.nan
    return out

def build_feature_vector(ticker: str) -> dict:
    prices = fetch_prices(ticker, settings.LOOKBACK_DAYS)
    f_roll = rolling_features(prices)
    f_fin = basic_financial_features(ticker)
    features = {**f_roll, **f_fin}
    # Replace NaNs
    features = {k: (0.0 if pd.isna(v) else float(v)) if isinstance(v, (int, float, np.floating)) or v is None else v for k, v in features.items()}
    return features