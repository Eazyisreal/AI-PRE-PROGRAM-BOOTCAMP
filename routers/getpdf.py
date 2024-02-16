from fastapi import  File, UploadFile, APIRouter
import os

router = APIRouter()


@router.post("/upload_pdf/")
async def upload_pdf(file: UploadFile = File(...)):
    os.makedirs("uploads", exist_ok=True)
    file_path = os.path.join("uploads", file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    return {"filename": file.filename, "file_path": file_path}
