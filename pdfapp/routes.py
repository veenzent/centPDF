from fastapi import APIRouter, UploadFile, File



pdf = APIRouter()


@pdf.post("/upload-file")
async def upload_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        # Do something with the file contents
        return {"filename": file.filename, "contents": contents}
    except Exception as e:
        return {"error": str(e)}
