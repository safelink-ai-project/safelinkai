import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.concurrency import run_in_threadpool
from scanner import scan_url

app = FastAPI(title="SafeLinkAI API")

# ------------------------------
# ✅ CORS CONFIG (IMPORTANT)
# ------------------------------
origins = [
    "*",  # 🔥 For testing (allow all)
    # Replace later with your frontend domain:
    # "https://your-frontend-domain.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ------------------------------
# ROUTES
# ------------------------------
@app.get("/")
async def home():
    return {"status": "server is running"}

@app.get("/scan")
async def scan(url: str):
    if not url.startswith(("http://", "https://")):
        raise HTTPException(status_code=400, detail="Invalid URL")

    try:
        result = await run_in_threadpool(scan_url, url)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# ------------------------------
# RUN SERVER
# ------------------------------
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
