🚀 FastAPI CRUD API with Supabase

A complete REST API built with FastAPI, featuring full CRUD operations connected to a Supabase (PostgreSQL) database — deployed live on Railway.

🔗 Live Demo

👉 https://fastapi-demo-production-6ef5.up.railway.app/docs

🛠️ Tech Stack


FastAPI — Backend framework
Supabase (PostgreSQL) — Database
Pydantic — Request validation
Python
Uvicorn — ASGI server
Railway — Deployment (auto-redeploys on every push)


✅ Features — Full CRUD

MethodEndpointDescriptionGET/itemsFetch all items from databasePOST/itemsAdd new item to databasePATCH/items/{item_id}Update an existing itemDELETE/items/{item_id}Delete an item


Environment variables (.env) used for Supabase credentials — never hardcoded
Interactive Swagger docs auto-generated at /docs
Connected to Supabase using supabase-py


⚙️ Setup Locally

bash# 1. Clone the repo
git clone https://github.com/AkashRag/fastapi-demo.git
cd fastapi-demo

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create .env file
SUPABASE_URL=your_url
SUPABASE_KEY=your_key

# 4. Run server
python -m uvicorn main:app --reload

# 5. Open
http://127.0.0.1:8000/docs

📦 Related Project

For JWT-based authentication (register, login, protected routes with bcrypt), check out jwt-auth-demo.


Built by Akash Raghuwanshi | Part of AI Automation Engineering portfolio
