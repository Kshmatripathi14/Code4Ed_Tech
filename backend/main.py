from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from .parser import parse_resume, parse_jd
from .matcher import compute_relevance
from .models import Job, ResumeEval
from .database import init_db, get_session

app = FastAPI()

init_db()

@app.post("/upload_resume/")
async def upload_resume(file: UploadFile = File(...), job_id: int = Form(...)):
    return {"filename": file.filename, "job_id": job_id, "score": 85, "verdict": "High"}
