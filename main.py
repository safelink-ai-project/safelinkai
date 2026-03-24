import os
from fastapi import FastAPI
from scanner import scan_url  # Make sure scanner.py is in the same directory

app = FastAPI(title="SafeLinkAI")

@app.get("/")
def home():
    return {"status": "server is running"}

@app.get("/scan")
def scan(url: str):
    """
    Scan a URL and return risk assessment.
    Example usage: /scan?url=https://example.com
    """
    result = scan_url(url)
    return result

# ------------------------------
# Run Uvicorn via Python so PORT works
# ------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Railway sets this automatically
    uvicorn_options = {
        "app": "main:app",
        "host": "0.0.0.0",
        "port": port,
        "log_level": "info",
        "reload": False  # Disable reload for production
    }
    import uvicorn
    uvicorn.run(**uvicorn_options)
