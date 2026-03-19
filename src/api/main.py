from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="EGGF Control Plane")

class InputText(BaseModel):
    text: str

@app.get("/")
def health():
    return {"status": "EGGF Control Plane Active"}

@app.post("/infer")
def infer(data: InputText):
    return {
        "message": "Control plane initialized",
        "input": data.text
    }
