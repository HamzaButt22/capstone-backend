from fastapi import FastAPI, UploadFile, File, HTTPException
import shutil
import os
from resume_analyzer import analyze_resume
from image_analyzer import analyze_image


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World", "status": "FastAPI Server Running Securely"}

@app.post("/analyze-resume")
async def web_analyze_resume(file: UploadFile = File(...)):
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDF documents are permitted.")

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

@app.post("/analyze-image")
async def web_analyze_image(file: UploadFile = File(...)):
    allowed_extensions = ('.png', '.jpg', '.jpeg')
    if not file.filename.lower().endswith(allowed_extensions):
        raise HTTPException(status_code=400, detail="Invalid image type. Only PNG, JPG, or JPEG formats are permitted.")

    temp_path = f"temp_{file.filename}"

    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        result = analyze_image(temp_path)

        return {
            "filename": file.filename,
            "status": "Success",
            "analysis": result
        }

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)
