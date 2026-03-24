import os
from fastapi import FastAPI, HTTPException
from fastapi.concurrency import run_in_threadpool
from scanner import scan_url  # Your scanner.py

app = FastAPI(title="SafeLinkAI Async")

@app.get("/")
async def home():
    return {"status": "server is running"}

@app.get("/scan")
async def scan(url: str):
    """
    Asynchronous scanning endpoint.
    Runs scan_url() in a separate thread to avoid blocking.
    """
    if not url.startswith(("http://", "https://")):
        raise HTTPException(status_code=400, detail="URL must start with http:// or https://")

    try:
        # Run the synchronous scan_url in a threadpool
        result = await run_in_threadpool(scan_url, url)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Scan failed: {str(e)}")

    return result

# ------------------------------
# Run Uvicorn with dynamic PORT
# ------------------------------
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")
