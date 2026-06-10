# FastAPI Items API

A REST API built with FastAPI and Supabase (PostgreSQL) backend.
Deployed live on Railway.

## 🔗 Live Demo
https://fastapi-demo-production-6ef5.up.railway.app/docs

## 🛠️ Tech Stack
- FastAPI
- Supabase (PostgreSQL)
- Python
- Uvicorn
- Railway (Deployment)

## ✅ Features
- GET /items — Fetch all items from database
- POST /items — Add new item to database

## ⚙️ Setup Locally

1. Clone the repo
2. Install dependencies:
   pip install -r requirements.txt
3. Create .env file:
   SUPABASE_URL=your_url
   SUPABASE_KEY=your_key
4. Run server:
   python -m uvicorn main:app --reload
5. Open: http://127.0.0.1:8000/docs
