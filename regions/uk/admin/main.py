from fastapi import FastAPI
app = FastAPI(title="RMY Regional Admin (UK)")

@app.get("/health")
def health():
    return {"ok": True}
