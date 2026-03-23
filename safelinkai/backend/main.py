from fastapi import FastAPI
from backend.scanner import scan_url

app = FastAPI()

@app.get("/scan")

def scan(url: str):

    result = scan_url(url)

    return result