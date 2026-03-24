from fastapi import FastAPI
from scanner import scan_url
import os
import uvicorn

app = FastAPI()

@app.get("/scan")
def home()
    return {"status": "server is running"}
def scan(url: str):
    result = scan_url(url)
    return result

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
