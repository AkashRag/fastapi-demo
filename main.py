import os
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from pydantic import BaseModel
from supabase import create_client 

#supabase connect
supabase_URL = os.environ.get("supabase_URL")
supabase_key = os.environ.get("supabase_key")
supabase =create_client (supabase_URL, supabase_key)

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

@app.get("/items")
def get_items():
    response = supabase.table("items").select("*").execute()
    return {"items" : response.data}

@app.post("/items")
def add_item(item: Item):
    response = supabase.table("items").insert({"name": item.name, "price": item.price}).execute()
    return {"message": "Item added", "item": response.data}

