# Credit-Intel

> An AI-powered credit monitoring and intelligence platform for analyzing financial data, detecting anomalies, and providing actionable insights in real-time.  

Credit-Intel helps users track their financial health through intuitive dashboards, scorecards, and event feeds. It leverages AI/ML models for anomaly detection and credit scoring — all built with open-source, free-to-use tools.

## 🚀 Features

- 📊 **Credit Score Dashboard** – Visualize trends, distributions, and insights.  
- 🔍 **Feature Analysis** – Interactive charts explaining model decisions.  
- 📈 **Trends & Events** – Timeline of significant financial changes.  
- ⚠️ **Alerts System** – Real-time notifications for anomalies and risks.  
- 📥 **Data Ingestion** – Supports both structured (CSV, Excel, DB) and unstructured (PDF, docs) inputs.  
- 🤖 **ML Models** – Built with scikit-learn, free & interpretable models (no paid APIs).  
- 🖥️ **Frontend** – Sleek modern UI with React + Tailwind + Vite.  
- 🐳 **Containerized** – Run via Docker Compose for easy deployment.  


## 🏗️ Tech Stack

### Backend
- **FastAPI** – REST API for ingestion, processing, and serving predictions  
- **SQLite** – Lightweight database for storing data & results  
- **Scikit-learn** – ML models (open-source, free)  
- **APScheduler** – Background tasks & scheduled jobs  

### Frontend
- **React (Vite + TypeScript)** – Modern fast UI  
- **TailwindCSS** – Utility-first styling  
- **Recharts** – Beautiful interactive charts  

### DevOps
- **Docker & Docker Compose** – Containerized deployment  
- **Python 3.10+** & **Node.js 18+**  


## ⚡ Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/credit-intel.git
cd credit-intel
````

### 2️⃣ Backend Setup (FastAPI)

#### Option A: Run locally with virtualenv

```bash
cd backend
python -m venv venv
venv\Scripts\activate   # (Windows)
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Backend will start at: [http://localhost:8000](http://localhost:8000)

#### Option B: Run with Docker

```bash
docker-compose up --build
```

---

### 3️⃣ Frontend Setup (React + Vite)

```bash
cd frontend
npm install
npm run dev
```

Frontend will start at: [http://localhost:5173](http://localhost:5173)

---

## 🔗 API Endpoints (Backend)

* `POST /ingest/structured` → Upload structured data (CSV, Excel)
* `POST /ingest/unstructured` → Upload PDFs/docs for parsing
* `GET /score` → Get latest credit score
* `GET /features` → Model feature importance
* `GET /alerts` → Active risk alerts
* `GET /events` → Timeline of significant events

Swagger Docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 Testing

Run backend tests:

```bash
cd backend
pytest
```

Run frontend lint/tests:

```bash
cd frontend
npm run lint
npm run test
```

---

## 📊 Future Improvements

* 🌐 Multi-user authentication & roles
* 🏦 Real-time integration with external credit APIs (when budget allows)
* 📱 Mobile-first responsive UI
* 🧠 Advanced ML models (deep learning, explainable AI)
* ☁️ Deployment on AWS/GCP with CI/CD

---

## 🙌 Acknowledgements

* [FastAPI](https://fastapi.tiangolo.com/) for blazing-fast backend APIs
* [React + Vite](https://vitejs.dev/) for frontend development
* [TailwindCSS](https://tailwindcss.com/) for styling
* [Scikit-learn](https://scikit-learn.org/) for ML algorithms
