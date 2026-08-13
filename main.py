from fastapi import FastAPI, UploadFile, File, HTTPException
import shutil
import os
from resume_analyzer import analyze_resume
from image_analyzer import analyze_image
import models
from database import engine
from database import SessionLocal
from sqlalchemy.orm import Session
from fastapi import Depends


app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hello World", "status": "FastAPI Server Running Securely"}

@app.post("/analyze-resume")
async def web_analyze_resume(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDF documents are permitted.")

    temp_path = f"temp_{file.filename}"

    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        category, skills = analyze_resume(temp_path)

        skills_string = ", ".join(skills)

        db_transaction = models.FileTransaction(
            filename=file.filename,
            file_type="resume",
            status="Success",
            result_summary=f"Category: {category} | Skills: {skills_string}"
        )

        db.add(db_transaction)
        db.commit()
        db.refresh(db_transaction)


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
async def web_analyze_image(file: UploadFile = File(...), db: Session = Depends(get_db)):
    allowed_extensions = ('.png', '.jpg', '.jpeg')
    if not file.filename.lower().endswith(allowed_extensions):
        raise HTTPException(status_code=400, detail="Invalid image type. Only PNG, JPG, or JPEG formats are permitted.")

    temp_path = f"temp_{file.filename}"

    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        result = analyze_image(temp_path)
        
        face_detected = result.get("face_detected", False)
        face_count = result.get("count", 0)

        db_transaction = models.FileTransaction(
            filename=file.filename,
            file_type="image",
            status="Success",
            result_summary=f"Face Detected: {face_detected} | Count: {face_count}"
        )

        db.add(db_transaction)
        db.commit()
        db.refresh(db_transaction)


        return {
            "filename": file.filename,
            "status": "Success",
            "analysis": result
        }

    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)
