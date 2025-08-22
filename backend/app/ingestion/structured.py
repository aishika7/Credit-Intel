import pandas as pd
import datetime as dt
import requests
import yfinance as yf
from typing import Dict, Any

# World Bank: e.g., USA CPI YOY: FP.CPI.TOTL.ZG.USA
WB_BASE = "https://api.worldbank.org/v2/country/{country}/indicator/{indicator}?format=json"

def fetch_prices(ticker: str, lookback_days: int = 180) -> pd.DataFrame:
    end = dt.datetime.utcnow()
    start = end - dt.timedelta(days=lookback_days)
    df = yf.download(ticker, start=start, end=end, auto_adjust=True, progress=False)
    df = df.rename(columns={"Adj Close": "adj_close"})
    return df

def fetch_world_bank(indicator: str, country: str = "USA", max_records: int = 100) -> pd.DataFrame:
    url = WB_BASE.format(country=country, indicator=indicator)
    r = requests.get(url)
    r.raise_for_status()
    data = r.json()
    if not isinstance(data, list) or len(data) < 2:
        return pd.DataFrame()
    rows = data[1]
    df = pd.DataFrame(rows)
    df = df[["date", "value"]].dropna()
    df["date"] = pd.to_datetime(df["date"])  # year granularity
    df = df.sort_values("date")
    return df

def basic_financial_features(ticker: str) -> Dict[str, Any]:
    t = yf.Ticker(ticker)
    info = t.fast_info if hasattr(t, "fast_info") else {}
    fin = {
        "market_cap": getattr(t, "info", {}).get("marketCap", None),
        "beta": getattr(t, "info", {}).get("beta", None),
        "ten_day_avg_vol": getattr(t, "fast_info", {}).get("ten_day_average_volume", None),
        "year_high": getattr(t, "fast_info", {}).get("year_high", None),
        "year_low": getattr(t, "fast_info", {}).get("year_low", None),
    }
    return fin