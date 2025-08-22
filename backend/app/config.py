import os
from datetime import timedelta

class Settings:
    APP_ENV: str = os.getenv("APP_ENV", "dev")
    DB_URL: str = os.getenv("DB_URL", "sqlite:///./data.db")
    REFRESH_MINUTES: int = int(os.getenv("REFRESH_MINUTES", "60"))
    ALLOWED_ORIGINS = [o.strip() for o in os.getenv("ALLOWED_ORIGINS", "*").split(",")]
    DEFAULT_ISSUERS = [
        {"ticker": "AAPL", "name": "Apple Inc."},
        {"ticker": "MSFT", "name": "Microsoft Corporation"},
        {"ticker": "TSLA", "name": "Tesla, Inc."},
        {"ticker": "T", "name": "AT&T Inc."}
    ]
    LOOKBACK_DAYS = 120
    SHORT_WINDOW = 14
    LONG_WINDOW = 60

settings = Settings()