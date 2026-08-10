from fastapi import FastAPI, UploadFile, File
import shutil
import os
from resume_analyzer import analyze_resume


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World", "status": "FastAPI Server Running Securely"}

@app.post("/analyze-resume")
async def web_analyze_resume(file: UploadFile = File(...)):
    temp_path = f"temp_{file.filename}"

    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        category, skills = analyze_resume(temp_path)

        return {
            "filename": file.filename,
            "status": "Success",
            "predicted_category": category,
            "extracted_skills": skills
        }

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

