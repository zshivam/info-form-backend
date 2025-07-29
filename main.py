from fastapi import FastAPI, Depends, Form, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
import models
import os
import database

# Create DB tables
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://info-form-frontend.vercel.app"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


app.mount("/uploads", StaticFiles(directory=UPLOAD_FOLDER), name="uploads")

# Dependency for DB session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


#submit
@app.post("/submit/")
def submit_form(
    name: str = Form(...),
    address: str = Form(...),
    contact: str = Form(...),
    image: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    
    image_path = os.path.join(UPLOAD_FOLDER, image.filename)
    with open(image_path, "wb") as f:
        f.write(image.file.read())

    # Save form data
    form_data = models.FormData(
        name=name,
        address=address,
        contact=contact,
        image=image.filename
    )
    db.add(form_data)
    db.commit()

    return {"message": "Data saved successfully"}


@app.get("/records/")
def get_records(db: Session = Depends(get_db)):
    return db.query(models.FormData).all()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)