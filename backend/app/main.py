from fastapi import FastAPI

app = FastAPI(
    title="SheetPilot AI",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "message": "Welcome to SheetPilot AI 🚀",
        "status": "running"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }