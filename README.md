# FastAPI Items API

A REST API built with FastAPI and Supabase (PostgreSQL) backend.

## Tech Stack
- FastAPI
- Supabase (PostgreSQL)
- Python
- Uvicorn

## Features
- GET /items — Fetch all items
- POST /items — Add new item

## Setup

1. Clone the repo
2. Install dependencies:
   pip install -r requirements.txt
3. Create .env file:
   SUPABASE_URL=your_url
   SUPABASE_KEY=your_key
4. Run server:
   python -m uvicorn main:app --reload

## API Docs
Visit http://127.0.0.1:8000/docs for Swagger UI
