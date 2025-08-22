import feedparser
import pandas as pd
import datetime as dt
from typing import List, Dict
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
from app.utils import map_event

try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')

SOURCES = {
    "reuters": "http://feeds.reuters.com/reuters/businessNews",
    "yahoo_fin": "https://finance.yahoo.com/news/rssindex",
}

sia = SentimentIntensityAnalyzer()

# You can append issuer-specific PR feeds if available

def fetch_rss() -> pd.DataFrame:
    rows: List[Dict] = []
    now = dt.datetime.utcnow()
    for name, url in SOURCES.items():
        feed = feedparser.parse(url)
        for e in feed.entries:
            title = e.get("title", "")
            link = e.get("link", "")
            published = e.get("published_parsed")
            ts = dt.datetime(*published[:6]) if published else now
            sent = sia.polarity_scores(title)["compound"]
            etype, impact = map_event(title)
            rows.append({
                "source": name,
                "title": title,
                "url": link,
                "published_at": ts,
                "sentiment": sent,
                "event_type": etype,
                "impact": impact,
                "summary": title
            })
    df = pd.DataFrame(rows)
    return df