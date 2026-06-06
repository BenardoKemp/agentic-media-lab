from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {
        "message": "AgenticMediaLab API running"
    }

