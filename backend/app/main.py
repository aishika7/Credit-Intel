from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app import routes
from app.database import init_db
from app.scheduler import start_scheduler
from app.config import settings

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize DB
init_db()

# Create app
app = FastAPI(
    title="Credit Intel API",
    description="Backend service for Credit Risk Intelligence dashboard",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS if settings.ALLOWED_ORIGINS != ["*"] else ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(routes.router)

@app.on_event("startup")
def startup_event():
    start_scheduler()

@app.get("/")
def root():
    return {"message": "Welcome to Credit Intel API!"}
