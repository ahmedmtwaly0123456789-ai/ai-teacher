from fastapi import FastAPI
import os

app = FastAPI(title="AI Teacher")

@app.get("/")
async def root():
    return {"status": "running", "service": "AI Teacher"}

@app.get("/health")
async def health():
    return {"status": "ok"}

@app.get("/env-check")
async def env_check():
    """التحقق من توفر المفاتيح"""
    return {
        "groq": bool(os.getenv("GROQ_API_KEY")),
        "google": bool(os.getenv("GOOGLE_API_KEY")),
        "cohere": bool(os.getenv("COHERE_API_KEY")),
        "supabase": bool(os.getenv("SUPABASE_URL")),
    }
